from django.contrib import admin

from .models import CategoryFurniture, FurnitureProduct, Images

class CategoryFurnitureAdmin(admin.ModelAdmin):
    fields = ['category_name', 'folder_name']

class ImagesAdmin(admin.TabularInline):
    model = Images
    extra = 0

class FurnitureProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['furnproduct', 'category']}),
    ]
    inlines = [ImagesAdmin]
    #list_display = ('imagepath', 'furnproduct')
    #list_display_links = ['imagepath']
    #list_editable = ['furnproduct']

admin.site.register(CategoryFurniture, CategoryFurnitureAdmin)
admin.site.register(FurnitureProduct, FurnitureProductAdmin)