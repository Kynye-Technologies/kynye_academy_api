import pytest
from django.contrib.auth import get_user_model
from apps.accounts.serializers import UserCreateSerializer, UserSerializer

User = get_user_model()

@pytest.mark.django_db
class TestUserCreateSerializer:
    def test_user_creation(self, user_factory):
        """Test that UserCreateSerializer creates a user correctly"""
        user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpass123',
            're_password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User',
            'user_type': 'student'
        }
        
        serializer = UserCreateSerializer(data=user_data)
        assert serializer.is_valid()
        user = serializer.save()
        
        assert user.email == user_data['email']
        assert user.username == user_data['username']
        assert user.first_name == user_data['first_name']
        assert user.last_name == user_data['last_name']
        assert user.user_type == user_data['user_type']
        assert user.check_password(user_data['password'])

    def test_password_mismatch(self):
        """Test that passwords must match"""
        user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpass123',
            're_password': 'wrongpass123',
            'first_name': 'Test',
            'last_name': 'User',
            'user_type': 'student'
        }
        
        serializer = UserCreateSerializer(data=user_data)
        assert not serializer.is_valid()
        assert 'non_field_errors' in serializer.errors

    def test_invalid_user_type(self):
        """Test that only valid user types are accepted"""
        user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpass123',
            're_password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User',
            'user_type': 'invalid_type'
        }
        
        serializer = UserCreateSerializer(data=user_data)
        assert not serializer.is_valid()
        assert 'user_type' in serializer.errors

@pytest.mark.django_db
class TestUserSerializer:
    def test_user_serialization(self, base_user):
        """Test that UserSerializer serializes a user correctly"""
        serializer = UserSerializer(base_user)
        data = serializer.data
        
        assert data['email'] == base_user.email
        assert data['username'] == base_user.username
        assert data['first_name'] == base_user.first_name
        assert data['last_name'] == base_user.last_name
        assert data['user_type'] == base_user.user_type
        assert data['full_name'] == UserSerializer().get_full_name(base_user)
        assert 'password' not in data

    def test_user_update(self, base_user):
        """Test that UserSerializer updates a user correctly"""
        update_data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'email': 'updated@example.com'
        }
        
        serializer = UserSerializer(base_user, data=update_data, partial=True)
        assert serializer.is_valid()
        updated_user = serializer.save()
        
        assert updated_user.first_name == update_data['first_name']
        assert updated_user.last_name == update_data['last_name']
        assert updated_user.email == update_data['email']
        # Get the serialized data to check full_name
        serializer = UserSerializer(updated_user)
        assert serializer.data['full_name'] == f"{update_data['first_name']} {update_data['last_name']}"

    def test_email_unique_validation(self, base_user, user_factory):
        """Test that duplicate emails are not allowed"""
        # Create another user
        other_user = user_factory.create()
        
        # Try to update base_user with other_user's email
        update_data = {'email': other_user.email}
        serializer = UserSerializer(base_user, data=update_data, partial=True)
        
        assert not serializer.is_valid()
        assert 'email' in serializer.errors

    def test_username_unique_validation(self, base_user, user_factory):
        """Test that duplicate usernames are not allowed"""
        # Create another user
        other_user = user_factory.create()
        
        # Try to update base_user with other_user's username
        update_data = {'username': other_user.username}
        serializer = UserSerializer(base_user, data=update_data, partial=True)
        
        assert not serializer.is_valid()
        assert 'username' in serializer.errors

    def test_read_only_fields(self, base_user):
        """Test that read-only fields cannot be updated"""
        original_id = base_user.id
        original_date_joined = base_user.date_joined
        
        update_data = {
            'id': 'new-uuid',
            'date_joined': '2024-01-01T00:00:00Z'
        }
        
        serializer = UserSerializer(base_user, data=update_data, partial=True)
        assert serializer.is_valid()
        updated_user = serializer.save()
        
        assert updated_user.id == original_id
        assert updated_user.date_joined == original_date_joined
