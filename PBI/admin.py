from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from PBI.models import * 
from .forms import UserAdminCreationForm, UserAdminChangeForm
# Register your models here.

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm #edit view
    add_form = UserAdminCreationForm #create view

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('USUARIO', 'admin','staff')
    list_filter = ('admin', 'staff', 'DNI')
    fieldsets = (
        (None, {'fields': ('USUARIO', 'NOMBRE_APELLIDO', 'DNI', 'password')}),
        ('Datos Personales', {'fields': ('NOMBRE_APELLIDO', 'DNI',)}),
        ('Permisos', {'fields': ('admin', 'staff', 'active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('USUARIO', 'NOMBRE_APELLIDO', 'DNI', 'password1', 'password2')}
        ),
    )
    search_fields = ('USUARIO',)
    ordering = ('USUARIO',)
    filter_horizontal = ()
admin.site.register(User, UserAdmin)

admin.site.register(Tipo)
admin.site.register(Padrones)
admin.site.register(DatosComunes)
admin.site.register(Domicilio)
admin.site.register(Automotores)
admin.site.register(Comercio)
admin.site.register(DatosEspecificos)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
