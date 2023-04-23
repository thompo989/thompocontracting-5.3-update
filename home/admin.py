from django.contrib import admin
from .models import Job, Contact, Testimonial


class JobAdmin(admin.ModelAdmin):
    list_display = ('job', 'description')

class ContactAdmin(admin.ModelAdmin):
        list_display = ('email', 'description')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Contact, ContactAdmin)
