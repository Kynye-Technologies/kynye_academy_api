from rest_framework import permissions

class IsInstructorOrReadOnly(permissions.BasePermission):
    """Allow only instructors to edit their own profile, others read-only."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.user_type == 'instructor' and obj.user == request.user

class IsStudentOrReadOnly(permissions.BasePermission):
    """Allow only students to edit their own profile, others read-only."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.user_type == 'student' and obj.user == request.user

class IsAuthenticatedOrInstructorListOnly(permissions.BasePermission):
    """Allow unauthenticated users to view instructor list/detail, but not student profiles."""
    def has_permission(self, request, view):
        if view.__class__.__name__ in ['InstructorProfileList', 'InstructorProfileDetail']:
            return True
        return request.user and request.user.is_authenticated
