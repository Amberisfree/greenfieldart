#from django.contrib import admin

#from .models import Post
# Register your models here.

#admin.site.register(Post)



from django.contrib import admin 
from .models import Post, Review

class ReviewInline(admin.TabularInline): 
	model = Review
class BookAdmin(admin.ModelAdmin): 
	inlines = [
        ReviewInline,
    ]
	list_display = ("title", "author", "body",)

admin.site.register(Post, BookAdmin)
