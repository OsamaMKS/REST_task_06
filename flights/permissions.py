from rest_framework.permissions import BasePermission
from datetime import date

class IsOwner(BasePermission):
    message = "You must be the Owner of this Booking."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False


class IsChangable(BasePermission):
	message = "You can't cancelled or modified"

	def has_object_permission(self, request, view, obj):
		days_left = (obj.date - date.today()).days
		if  days_left > 3:
			return True
		else:
			return False
