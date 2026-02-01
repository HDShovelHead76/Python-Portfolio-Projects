from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "middle_name", "last_name",
            		"email", "phone", "occupation")
    search_fields = ("first_name", "middle_name", "last_name",
        			"email", "phone", "occupation")
    list_filter = ("last_name", "occupation")
    ordering = ("first_name",) # comma makes it a tuple
    readonly_fields = ("email", "occupation",)

admin.site.register(Form, FormAdmin)