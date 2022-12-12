from django.contrib import admin

from .models import Forum
from .models import Comment

# Register your models here.


class InLineComments(admin.TabularInline):
    model = Comment

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ['created_by','title', 'created_date', 'status']
    list_filter = ['status']
    search_fields = ['title','created_date']
    prepopulated_fields = {'slug' : ('title',)}
    inlines = [InLineComments]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','created_by','body','forum']
    list_filter = ['created_by']
    search_fields = ['body']



from django.contrib import admin

# Register your models here.
