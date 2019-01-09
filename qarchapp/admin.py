from django.contrib import admin
from .models import Post, Information

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")

admin.site.register(Post, PostAdmin)


class InformationAdmin(admin.ModelAdmin):
   
   def has_add_permission(self, request):
       return False

   def has_delete_permission(self, request, obj=None):
       return False    

admin.site.register(Information, InformationAdmin)