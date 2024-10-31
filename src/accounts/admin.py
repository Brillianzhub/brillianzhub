from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Profile, GroupExtend, Contact, EmailActivation

# from .models import Profile
User = get_user_model()
# Register your models here.


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'admin', 'id_referrer')
    list_filter = ('admin',  'staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal info', {'fields': ('firstname', 'designation', 'lastname', 'country', 'contact',)}),
        ('Permissions', {'fields': ('admin', 'staff', 'is_active', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'firstname')
    ordering = ('email',)
    filter_horizontal = ()

# class GroupExtendAdmin(admin.ModelAdmin):
#     # list_display = ['user', 'date_of_birth', 'photo']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']


admin.site.register(User, UserAdmin)
# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(GroupExtend)


admin.site.register(Contact)


class EmailActivationAdmin(admin.ModelAdmin):
    search_fields = ['email']

    class Meta:
        model = EmailActivation


admin.site.register(EmailActivation, EmailActivationAdmin)
