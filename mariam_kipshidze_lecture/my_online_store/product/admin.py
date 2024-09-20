from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from product.models import Product, Category, Cart, Brand, Tag, Attribute
from product.resource import ProductResource

# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Brand)
admin.site.register(Tag)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass


class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 1


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_classes = [ProductResource]
    list_display = ("title", 'slug', 'price', 'brand', 'create', 'updated', 'active')
    list_filter = ('brand', 'active', 'categories')
    search_fields = ('title', 'description')
    list_editable = ('active', 'price')
    list_select_related = ('brand',)
    # readonly_fields = ('title',)
    filter_horizontal = ('categories', 'tags')
    # filter_vertical = ('categories',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Main Info', {
            'fields': ('title', 'slug', 'price', 'active', 'brand')
        }),
        ('Additional Info', {
            'fields': ('description', 'categories', 'tags')
        }),
    )
    save_on_top = True
    # exclude = ('brand',)
    list_per_page = 5

    inlines = [AttributeInline]

@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
