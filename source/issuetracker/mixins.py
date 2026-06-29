from django.contrib.auth.mixins import PermissionRequiredMixin

class ProjectPermissionMixin(PermissionRequiredMixin):

    def has_permission(self):
        if not super().has_permission():
            return False

        return self.request.user in self.get_object().users.all()