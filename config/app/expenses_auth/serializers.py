from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'confirm_password',
            'date_of_birth',
            'mobile_number',
            'address',
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            date_of_birth=validated_data.get('date_of_birth'),
            mobile_number=validated_data.get('mobile_number'),
            address=validated_data.get('address'),
        )
        return user
