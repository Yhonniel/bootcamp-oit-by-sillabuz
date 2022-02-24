from django.contrib import admin

# Register your models here.
from .models import Profile, Testimony


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     pass
    # list_display = [  '_user', 'gender', 'document', 'avatar']

    # @admin.display(empty_value='????')
    # def _user(self, obj):
    #     print(obj)
    #     return obj.user

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('id', '_email', 'message', 'rate')

# admin.site.register(Testimony, TestimonyAdmin)

admin.site.register(Profile)

