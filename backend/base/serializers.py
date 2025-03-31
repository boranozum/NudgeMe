from rest_framework import serializers

from accounts.serializers.user import BriefUserSerializer
from base.models import AbstractBaseModel


class BaseModelSerializer(serializers.ModelSerializer):
    created_by = BriefUserSerializer(read_only=True)
    updated_by = BriefUserSerializer(read_only=True)

    def __init__(self, *args, **kwargs):
        if hasattr(self.Meta, "model") and not issubclass(self.Meta.model, AbstractBaseModel):
            raise TypeError(f"{self.Meta.model.__name__} must inherit `AbstractBaseModel`")

        if kwargs.get("brief") and hasattr(self.Meta, 'brief_fields'):
            kwargs.pop("brief")
            self.Meta.fields = ["id"] + self.Meta.brief_fields
        super().__init__(*args, **kwargs)

    class Meta:
        abstract = True

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['created_by'] = request.user
        validated_data['updated_by'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        validated_data['updated_by'] = request.user
        return super().update(instance, validated_data)
