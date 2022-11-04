from django.contrib import admin
from .models import Yarn, Fiber, Company
from .enums import FiberTypes


@admin.register(Yarn)
class YarnAdmin(admin.ModelAdmin):
    list_filter = ('weight',)
    list_display = ('id', 'name',
                    'weight',
                    'texture',
                    'grams',
                    'yardage',
                    'min_gauge',
                    'max_gauge',
                    'gauge_divisor', 'company_name')
    search_fields = ['name']

    def company_name(self, obj):
        return obj.company.name


class FiberTypesListFilter(admin.SimpleListFilter):
    title = 'kind'

    parameter_name = 'kind'

    def lookups(self, request, model_admin):
        return (
            (0, 'ANIMAL_FIBER'),
            (1, 'ANIMAL_DERIVED'),
            (2, 'SYNTHETIC'),
            (3, 'PLANT_FIBERS')
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(kind=self.value())

        return queryset


@admin.register(Fiber)
class FiberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fiber_kind')
    list_filter = (FiberTypesListFilter,)
    search_fields = ['name']

    def fiber_kind(self, obj):
        return FiberTypes(obj.kind).name


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linde_hobby', 'hobbii')
    list_filter = ('linde_hobby', 'hobbii')
    search_fields = ['name']
