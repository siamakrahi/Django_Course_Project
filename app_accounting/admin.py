from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_accounting.models import User, MessagingModel, ConsultingModel, NewsletterModel
from django.utils.translation import gettext_lazy as _

class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
            "fields": (
                ("firstname", "lastname"),
                "email",
                "avatar",
                "about",
            ),
        }),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "email", "avatar", "about") 


class MessagingAdmin(admin.ModelAdmin):
    title = 'messaging'
    list_display = ("user", "email", "phone_number")
    readonly_fields = ("user",)
    def get_queryset(self, request):
        current_user = request.user
        qs = super().get_queryset(request)
        return qs.filter(user=current_user)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class ConsultingAdmin(admin.ModelAdmin):
    title = 'consulting'
    list_display = ("user", "email")
    readonly_fields = ("user",)
    def get_queryset(self, request):
        current_user = request.user
        qs = super().get_queryset(request)
        return qs.filter(user=current_user)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class NewsletterAdmin(admin.ModelAdmin):
    title = 'newsletter'
    list_display = ("email",)
    def get_queryset(self, request):
        current_user = request.user
        qs = super().get_queryset(request)
        return qs.filter(user=current_user)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)
admin.site.register(MessagingModel,MessagingAdmin)  
admin.site.register(ConsultingModel,ConsultingAdmin) 
admin.site.register(NewsletterModel,NewsletterAdmin)
