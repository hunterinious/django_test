from django.http import HttpResponseRedirect
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    change_form_template = 'posts/admin/custom_update.html'

    def response_change(self, request, obj):
        if "comments-delete" in request.POST:
            obj.comment_set.all().delete()
            obj.save()
            self.message_user(request, "All comments deleted")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


admin.site.register(Post, PostAdmin)
