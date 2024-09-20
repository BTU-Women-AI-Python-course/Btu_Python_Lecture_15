from import_export import resources, fields

from product.models import Product


class ProductResource(resources.ModelResource):
    tags = fields.Field()

    @staticmethod
    def dehydrate_tags(product):
        print(product.tag_titles)
        return product.tag_titles

    class Meta:
        model = Product
        fields = ['id', 'title', 'active', 'brand__title', 'tags']
