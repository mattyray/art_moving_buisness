from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'client', 'amount', 'status', 'due_date', 'date_created')
    list_filter = ('status', 'due_date', 'date_created')
    search_fields = ('invoice_number', 'client__name')
    ordering = ('-date_created',)
    date_hierarchy = 'due_date'
    readonly_fields = ['date_created']

    fieldsets = (
        (None, {
            'fields': ('invoice_number', 'client', 'work_order', 'amount', 'status')
        }),
        ('Dates', {
            'fields': ('due_date', 'date_created', 'updated_at')
        }),
        ('Additional Info', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )
