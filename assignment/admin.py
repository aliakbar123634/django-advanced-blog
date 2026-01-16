from django.contrib import admin
from .models import *
# Register your models here.


class AboutUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=AboutUs.objects.all().count()
        if count==0:
            return True
        else:
            return False
admin.site.register(AboutUs , AboutUsAdmin)
admin.site.register(FollowUs)