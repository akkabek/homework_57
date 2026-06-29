from django.contrib.auth.mixins import PermissionRequiredMixin

class ProjectPermissionMixin(PermissionRequiredMixin):

    def has_permission(self):
        if not super().has_permission():
            return False

        if self.request.user.is_superuser:
            return True

        return self.get_object().users.filter(
            pk=self.request.user.pk
        ).exists()