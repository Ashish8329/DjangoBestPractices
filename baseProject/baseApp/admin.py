from django.contrib import admin

from base.base_admin import BaseAdmin
from baseApp.models import User


@admin.register(User)
class User(BaseAdmin):
    list_display = ["username", "created_at"]  # display at the outside main page
    fields = ["username", "created_at", "updated_at"]  # inside the instance
    exclude = []
    list_filter = []
    # readonly_fields = ['created_at',"updated_at"]

    empty_value_display = "-empty-"

    def save_model(
        self, request, obj, form, change
    ):  # execute whenewher we update or create
        return super().save_model(request, obj, form, change)
