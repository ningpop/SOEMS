from django.contrib import admin
from .models import Study, Participation, Review

# Register your models here.
admin.site.register(Study)
admin.site.register(Review)
admin.site.register(Participation)

# @admin.register(Participation)
# class ParticipateAdmin(admin.ModelAdmin):
#     list_display = ("study")
#     filter_horizontal = ("applicant",)