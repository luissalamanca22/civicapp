"""Circle serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from core.models import Circle


class ProfileSerializer(serializers.ModelSerializer):
    """Circle model serializer."""

    members_limit = serializers.IntegerField(
        required=False,
        min_value=10,
        max_value=32000
    )
    is_limited = serializers.BooleanField(default=False)

    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'user', 'biography', 'age'
        )
        read_only_fields = (
            'created',
        )

    # def validate(self, data):
    #     """Ensure both members_limit and is_limited are present."""
    #     members_limit = data.get('members_limit', None)
    #     is_limited = data.get('is_limited', False)
    #     if is_limited ^ bool(members_limit):
    #         raise serializers.ValidationError('If circle is limited, a member limit must be provided')
    #     return data
