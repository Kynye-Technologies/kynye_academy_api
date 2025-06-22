from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    re_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 
                 'user_type', 'password', 're_password')
        
    def validate(self, attrs):
        """Validate that passwords match."""
        if attrs.get('password') != attrs.get('re_password'):
            raise serializers.ValidationError({"non_field_errors": ["The two password fields didn't match."]})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('re_password', None)
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                 'user_type', 'full_name', 'is_active', 'date_joined')
        read_only_fields = ('id', 'is_active', 'date_joined')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
