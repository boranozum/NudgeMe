from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from rest_framework import status

from accounts.models import UserVerification, User
from accounts.serializers.user import UserSerializer
from accounts.utils.functions import generate_verification_token
from base.response import Response
from base.utils import send_email


class RegisterView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        try:
            user_serializer = UserSerializer(data=request.data)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()

            username_field = get_user_model().USERNAME_FIELD
            request.user = get_user_model().objects.get_by_natural_key(user_serializer.initial_data[username_field])

            verification_token = generate_verification_token(request.user)
            send_email(
                request.user.email,
                "[NudgeMe] Email Verification",
                f"""
                    Here is your verification code: {verification_token}
                """
            )
        except ValidationError as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                message="Failed to register user",
                content=e.detail
            )
        finally:
            del request.data["confirm_password"]

        return Response(
            status=status.HTTP_201_CREATED,
            message=f"Registration successful. An email is sent to {request.data['email']} for verification.",
            content=user_serializer.data
        )

class UserVerificationViewSet(GenericViewSet):
    permission_classes = ()
    authentication_classes = ()

    @action(detail=False, methods=["post"])
    def verify(self, request, *args, **kwargs):
        token = request.data['token']
        user_id = request.data['user_id']

        user_verification = UserVerification.objects.filter(token=token, user_id=user_id).first()
        if user_verification is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                message="Invalid verification token"
            )

        elif user_verification.is_expired:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                message="Verification token has expired"
            )

        user_instance = user_verification.user
        user_instance.verified_at = timezone.now()
        user_instance.save()

        return Response(
            status=status.HTTP_200_OK,
            message=f"Verification successful."
        )

    @action(detail=False, methods=["post"])
    def resend(self, request, *args, **kwargs):
        user_id = request.data['user_id']
        user = User.objects.get(pk=user_id)

        UserVerification.objects.filter(user=user).delete()
        verification_token = generate_verification_token(user)
        send_email(
            user.email,
            "[NudgeMe] Email Verification",
            f"""
                Here is your verification code: {verification_token}
            """
        )

        return Response(
            status=status.HTTP_200_OK,
            message=f"Sending another verification email to {user.email} is successful."
        )




class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            request.user = get_user_model().objects.get_by_natural_key(serializer.initial_data[serializer.username_field])
            if not request.user.is_verified:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    message="User not verified"
                )

        except TokenError as e:
            raise InvalidToken(e.args[0])
        except Exception as e:
            raise e
        finally:
            del request.data["password"]

        return Response(
            status=status.HTTP_200_OK,
            message="Login successful",
            content=serializer.validated_data,
        )


class LoginRefreshView(TokenRefreshView):
    pass


class LogoutView(TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        try:
            request.user = get_user_model().objects.get_by_natural_key(request.data["username"])
        except:
            pass
        return super().post(request, *args, **kwargs)