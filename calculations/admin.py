from django.contrib import admin
from .models import CalculationHistory




@admin.register(CalculationHistory)
class CalculationHistoryAdmin(admin.ModelAdmin):
    list_display = ["operation", "input_numbers", "result", "created_at"]
    list_filter = ["operation", "created_at"]
    search_fields = ["operation", "input_numbers"]
    ordering = ["-created_at"]
    readonly_fields = ["operation", "input_numbers", "result", "created_at"]
    fieldsets = (
        (None, {
            "fields": ("operation", "input_numbers", "result", "created_at")
        }),
    )