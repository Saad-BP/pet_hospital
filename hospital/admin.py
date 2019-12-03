from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib import admin
from .models import *
# Register your models here.
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook
from django.http import HttpResponse
from django.utils.html import *



class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['employee_id', ]
    list_display = ('employee_id', 'employee_image', 'employee_type', 'user', 'name', 'phone', 'joining_date')

    list_filter = ('employee_type', 'joining_date')

    def employee_image(self, obj):

        if obj.image and obj.image.url:
            return format_html(mark_safe("<a href='{}'><img src='{}' height='100' width='100' /></a>".format(obj.image.url, obj.image.url)))
        else:
            return None


admin.site.register(Employee, EmployeeAdmin)



class BlogAdmin(admin.ModelAdmin):
    search_fields = ['employee_id', ]
    list_display = ('title', 'blog_image', 'short_description', 'date')
    list_filter = ('title', 'date')

    def blog_image(self, obj):

        if obj.image and obj.image.url:
            return format_html(mark_safe("<a href='{}'><img src='{}' height='100' width='100' /></a>".format(obj.image.url, obj.image.url)))
        else:
            return None


admin.site.register(Blog, BlogAdmin)



class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'designation', 'details', 'phone', 'active', 'order')
    list_filter = ('designation',)
    search_fields = ['name']

    def team_image(self, obj):

        if obj.image and obj.image.url:
            return format_html(mark_safe("<a href='{}'><img src='{}' height='100' width='100' /></a>".format(obj.image.url, obj.image.url)))
        else:
            return None


admin.site.register(TeamMember, TeamMemberAdmin)



class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone')
    search_fields = ['name']

    autocomplete_fields = ['user']


admin.site.register(Doctor, DoctorAdmin)



class PescriptionInline(admin.StackedInline):
    model = Prescription
    list_display = ('observation', 'treatment', )
    fieldsets = (
       (None, {
            'fields': ('observation', 'treatment',)
        }),
    )


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet', 'id' , 'service_type', 'assigned_doctor', 'appointment_date', 'details', 'phone', 'active',  'attended', 'payment_amount', )
    inlines = [PescriptionInline, ]

    list_filter = [('appointment_date', DateRangeFilter), 'attended', 'assigned_doctor']

    search_fields = ['pet__name', 'assigned_doctor__name', 'id', 'phone']

    def get_queryset(self, request):
        print("asdsad")

        if request.user.role:
            if request.user.role == "doctor":
                doctor = request.user.doctor
                return Appointment.objects.filter(assigned_doctor=doctor).order_by('attended', 'appointment_date')

        return Appointment.objects.all().order_by('attended', 'appointment_date')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if request.user.role:
            if request.user.role == "doctor":
                if db_field.name == "assigned_doctor":
                    kwargs["queryset"] = Doctor.objects.filter(id=request.user.doctor.id)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)




admin.site.register(Appointment, AppointmentAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_image', 'details', 'url', 'is_available', )

    list_filter = ['is_available']

    search_fields = ['name', 'url', ]

    def product_image(self, obj):

        if obj.image and obj.image.url:
            return format_html(mark_safe("<a href='{}'><img src='{}' height='100' width='100' /></a>".format(obj.image.url, obj.image.url)))
        else:
            return None

admin.site.register(Product, ProductAdmin)
