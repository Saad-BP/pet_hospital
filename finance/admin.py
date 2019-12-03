from django.contrib import admin
from django.contrib import admin
from .models import *
# Register your models here.
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook
from django.http import HttpResponse


def xlsx_generator(data):
    workbook = Workbook()
    worksheet = workbook.active

    for row in data:
        worksheet.append(row)


    return workbook



class DailyExpenditureYearFilter(admin.SimpleListFilter):
    title = ('By Year')
    parameter_name = 'Year'

    def lookups(self, request, model_admin):
        items = DailyExpenditure.objects.all()
        years = []
        for item in items:
            if item.date:
                if item.date.year not in years:
                    years.append(item.date.year)
        years.sort(reverse=True)
        tuple_list = [(item, str(item)) for item in years]
        return tuple_list

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(date__year=self.value())
        else:
            return queryset


class DailyExpenditureMonthFilter(admin.SimpleListFilter):
    title = ('Month')
    parameter_name = 'Month'

    def lookups(self, request, model_admin):
        months = [(1, 'January'),
                  (2, 'February'),
                  (3, 'March'),
                  (4, 'April'),
                  (5, 'May'),
                  (6, 'June'),
                  (7, 'July'),
                  (8, 'August'),
                  (9, 'September'),
                  (10, 'October'),
                  (11, 'November'),
                  (12, 'December'),
        ]

        return months

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(date__month=self.value())
        else:
            return queryset


class DailyExpenditureAdmin(admin.ModelAdmin):

    list_display = ('item', 'total_unit', 'total_cost', 'date',)
    list_filter = [('date', DateRangeFilter), DailyExpenditureYearFilter, DailyExpenditureMonthFilter, 'date']
    actions = ('download_report', )


    def download_report(self, request, queryset):
        data = []
        first_columns = ["Item", "Total unit", "Total cost", 'Date']
        data.append(first_columns)

        total = 0
        for item in queryset:
            row = []
            row.append(item.item)
            row.append(str(item.total_unit))
            row.append(str(item.total_cost))
            row.append(str(item.date))
            data.append(row)
            total = total + item.total_cost

        last_row = ["", "", str(total), ""]
        data.append(last_row)


        wbook = xlsx_generator(data)
        response = HttpResponse(content=save_virtual_workbook(wbook))
        response['Content-Disposition'] = 'attachment; filename=report.xlsx'
        return response

admin.site.register(DailyExpenditure, DailyExpenditureAdmin)


class ElectricityBillAdmin(admin.ModelAdmin):

    list_display = ('year', 'month', 'pick_hour_unit', 'off_pick_hour_unit', 'total_bill_paid', 'date_of_payment')
    # list_filter = [('date', DateRangeFilter), DailyExpenditureYearFilter, DailyExpenditureMonthFilter, 'date']
    list_filter = ('year', 'month')

    actions = ('download_report', )


    def download_report(self, request, queryset):
        data = []
        first_columns = ['year', 'month', 'pick_hour_unit', 'off_pick_hour_unit', 'total_bill_paid', 'Date of payment']

        data.append(first_columns)

        total = 0
        for item in queryset:
            row = []
            row.append(item.year)
            row.append(str(item.get_month_display()))
            row.append(str(item.pick_hour_unit))
            row.append(str(item.off_pick_hour_unit))

            row.append(str(item.total_bill_paid))
            row.append(str(item.date_of_payment))

            data.append(row)
            total = total + item.total_bill_paid

        last_row = ["", "", "", "", str(total), ""]
        data.append(last_row)


        wbook = xlsx_generator(data)
        response = HttpResponse(content=save_virtual_workbook(wbook))
        response['Content-Disposition'] = 'attachment; filename=report.xlsx'
        return response

admin.site.register(ElectricityBill, ElectricityBillAdmin)




class WasaBillAdmin(admin.ModelAdmin):

    list_display = ('year', 'month', 'unit', 'total_bill_paid', 'date_of_payment')
    # list_filter = [('date', DateRangeFilter), DailyExpenditureYearFilter, DailyExpenditureMonthFilter, 'date']
    list_filter = ('year', 'month')

    actions = ('download_report', )


    def download_report(self, request, queryset):
        data = []
        first_columns = ['year', 'month', 'unit', 'total_bill_paid', 'Date of payment']

        data.append(first_columns)

        total = 0
        for item in queryset:
            row = []
            row.append(item.year)
            row.append(str(item.get_month_display()))
            row.append(str(item.unit))

            row.append(str(item.total_bill_paid))
            row.append(str(item.date_of_payment))

            data.append(row)
            total = total + item.total_bill_paid

        last_row = ["", "", "", str(total), ""]
        data.append(last_row)


        wbook = xlsx_generator(data)
        response = HttpResponse(content=save_virtual_workbook(wbook))
        response['Content-Disposition'] = 'attachment; filename=report.xlsx'
        return response

admin.site.register(WasaBill, WasaBillAdmin)



class CarFuelCostAdminYearFilter(admin.SimpleListFilter):
    title = ('By Year')
    parameter_name = 'Year'

    def lookups(self, request, model_admin):
        items = CarFuelCost.objects.all()
        years = []
        for item in items:
            if item.date:
                if item.date.year not in years:
                    years.append(item.date.year)
        years.sort(reverse=True)
        tuple_list = [(item, str(item)) for item in years]
        return tuple_list

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(date__year=self.value())
        else:
            return queryset



class CarFuelCostAdmin(admin.ModelAdmin):

    list_display = ('item', 'total_unit', 'total_cost', 'date',)
    list_filter = [('date', DateRangeFilter), CarFuelCostAdminYearFilter, DailyExpenditureMonthFilter, 'date']
    actions = ('download_report', )


    def download_report(self, request, queryset):
        data = []
        first_columns = ["Item", "Total unit", "Total cost", 'Date']
        data.append(first_columns)

        total = 0
        for item in queryset:
            row = []
            row.append(item.item)
            row.append(str(item.total_unit))
            row.append(str(item.total_cost))
            row.append(str(item.date))
            data.append(row)
            total = total + item.total_cost

        last_row = ["", "", str(total), ""]
        data.append(last_row)


        wbook = xlsx_generator(data)
        response = HttpResponse(content=save_virtual_workbook(wbook))
        response['Content-Disposition'] = 'attachment; filename=report.xlsx'
        return response

admin.site.register(CarFuelCost, CarFuelCostAdmin)


class CylinderBillYearFilter(admin.SimpleListFilter):
    title = ('By Year')
    parameter_name = 'Year'

    def lookups(self, request, model_admin):
        items = CylinderBill.objects.all()
        years = []
        for item in items:
            if item.date:
                if item.date.year not in years:
                    years.append(item.date.year)
        years.sort(reverse=True)
        tuple_list = [(item, str(item)) for item in years]
        return tuple_list

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(date__year=self.value())
        else:
            return queryset



class CylinderBillAdmin(admin.ModelAdmin):

    list_display = ('item', 'total_unit', 'total_cost', 'date',)
    list_filter = [('date', DateRangeFilter), CylinderBillYearFilter, DailyExpenditureMonthFilter, 'date']
    actions = ('download_report', )


    def download_report(self, request, queryset):
        data = []
        first_columns = ["Item", "Total unit", "Total cost", 'Date']
        data.append(first_columns)

        total = 0
        for item in queryset:
            row = []
            row.append(item.item)
            row.append(str(item.total_unit))
            row.append(str(item.total_cost))
            row.append(str(item.date))
            data.append(row)
            total = total + item.total_cost

        last_row = ["", "", str(total), ""]
        data.append(last_row)


        wbook = xlsx_generator(data)
        response = HttpResponse(content=save_virtual_workbook(wbook))
        response['Content-Disposition'] = 'attachment; filename=report.xlsx'
        return response

admin.site.register(CylinderBill, CylinderBillAdmin)



class UtensilsRecordAdmin(admin.ModelAdmin):

    list_display = ('name_of_the_item', 'number_of_available_items', 'allocation_area', 'note', 'date', )
    list_filter = [('date', DateRangeFilter), 'date']
    actions = ('download_report', )


    def download_report(self, request, queryset):
        data = []
        first_columns = ["name_of_the_item", "number_of_available_items", "allocation_area", 'note', "date"]
        data.append(first_columns)

        total = 0
        for item in queryset:
            row = []
            row.append(item.item)
            row.append(str(item.total_unit))
            row.append(str(item.total_cost))
            row.append(str(item.date))
            data.append(row)
            total = total + item.total_cost

        last_row = ["", "", str(total), ""]
        data.append(last_row)


        wbook = xlsx_generator(data)
        response = HttpResponse(content=save_virtual_workbook(wbook))
        response['Content-Disposition'] = 'attachment; filename=report.xlsx'
        return response

admin.site.register(UtensilsRecord, UtensilsRecordAdmin)


class SalaryRecordAdmin(admin.ModelAdmin):

    list_display = ('employee', 'amount', 'salary_year', 'salary_month', 'payment_date')
    list_filter = [('payment_date', DateRangeFilter), 'salary_year', 'salary_month']
    actions = ('download_report', )
    search_fields = ('employee__employee_id', )

    def download_report(self, request, queryset):
        data = []
        first_columns = [ 'employee', 'amount', 'salary_year', 'salary_month', 'payment_date']
        data.append(first_columns)


        total = 0
        for item in queryset:
            row = []
            row.append(str(item.employee))
            row.append(str(item.amount))
            row.append(str(item.salary_year))
            row.append(str(item.salary_month))
            row.append(str(item.payment_date))

            data.append(row)
            total = total + item.amount

        last_row = ["", str(total), "", "", "", ""]
        data.append(last_row)


        wbook = xlsx_generator(data)
        response = HttpResponse(content=save_virtual_workbook(wbook))
        response['Content-Disposition'] = 'attachment; filename=report.xlsx'
        return response

admin.site.register(SalaryRecord, SalaryRecordAdmin)