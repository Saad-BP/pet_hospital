from django.contrib import admin
from .models import *
# Register your models here.


class PetOwnerAdmin(admin.ModelAdmin):

    list_display = ('name', 'gender', 'address', 'phone', 'email', 'date_of_birth', )


admin.site.register(PetOwner, PetOwnerAdmin)


class PetAdmin(admin.ModelAdmin):

    list_display = ('owner', 'name', 'animal_type', 'color', 'date_of_birth', 'seven_day_vaccinated', 'forty_five_day_vaccinated', 'yearly_vaccinated')


admin.site.register(Pet, PetAdmin)


class ForumCommentInline(admin.StackedInline):
    model = ForumComment



class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'details', 'author')

    search_fields = ('id', 'author__username')
    inlines = [ForumCommentInline, ]

admin.site.register(ForumPost, ForumPostAdmin)


