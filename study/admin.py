from django.contrib import admin
from .models import Study, Participation, Review

# Register your models here.
admin.site.register(Study)
admin.site.register(Review)

@admin.register(Participation)
class ParticipateAdmin(admin.ModelAdmin):
    list_display = ("study", "max_size")
    filter_horizontal = ("applicant",)