from __future__ import absolute_import

from django.core.exceptions import PermissionDenied

from rest_framework.filters import BaseFilterBackend

from acls.models import AccessEntry
from permissions.models import Permission


class nucleosObjectPermissionsFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        required_permission = getattr(view, 'nucleos_object_permissions', {}).get(request.method, None)

        if required_permission:
            try:
                Permission.objects.check_permissions(request.user, required_permission)
            except PermissionDenied:
                return AccessEntry.objects.filter_objects_by_access(required_permission[0], request.user, queryset)
            else:
                return queryset
        else:
            return queryset
