from django.contrib import admin

# Register your models here.

from userreview.models import Review

# Create your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_review', 'ratings')


admin.site.register(Review, ReviewAdmin)
