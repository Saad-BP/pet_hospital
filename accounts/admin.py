from django.contrib import admin
from .models import *
from .models import CustomUser, CustomGroup
from django.contrib.auth.admin import UserAdmin, GroupAdmin

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('username', 'role', 'is_staff')

    search_fields = ("username",)

    list_filter = ['role', ]



    def save_model(self, request, obj, form, change):

        if 'password' in form.changed_data:
            obj.set_password(obj.password)
            obj.save()
        else:
            pass



        super(CustomUserAdmin, self).save_model(request, obj, form, change)


admin.site.register(CustomUser, CustomUserAdmin)


class CustomGroupAdmin(GroupAdmin):
    list_display = ('name',)
    exclude = ('last_modified_by', 'created_by')


admin.site.unregister(Group)
admin.site.register(CustomGroup, CustomGroupAdmin)




from django.contrib import admin

# Register your models here.
