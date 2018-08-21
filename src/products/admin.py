from django import forms
from django.contrib import admin
from django.db.models import Q
from sorl.thumbnail.admin import AdminImageMixin

from .models import Make, Model, ProductType, Product, ProductPicture, Offer


class ModelInlines(admin.StackedInline):
    model = Model
    min_num = 1
    extra = 0


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'model']
    search_fields = ['name', 'model__name']
    list_filter = ['model']
    inlines = [ModelInlines]


class ProductPictureInline(AdminImageMixin, admin.TabularInline):
    model = ProductPicture
    extra = 1
    max_num = 5
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_main_picture',
        'product_name',
        'product_type',
    )
    list_display_links = ['product_main_picture', 'product_name']

    list_filter = (
        ('make', admin.RelatedOnlyFieldListFilter),
        ('model', admin.RelatedOnlyFieldListFilter),
        ('product_type', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ['make__name', 'model__name']
    inlines = [ProductPictureInline]


class OfferForm(forms.ModelForm):
    """
    This modelform is used to limit the product offer to those product that
    have no offer yet or active ones.
    """

    def __init__(self, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs:
            self.fields['product'].queryset = Product.objects.filter(Q(offer__isnull=True) | Q(offer__active=False))


@admin.register(Offer)
class OfferAdmin(AdminImageMixin, admin.ModelAdmin):
    form = OfferForm
    list_display = [
        'get_image_tag',
        'product',
        'start_date',
        'expiration_date',
        'price',
        'status_active_offer'
    ]

    list_display_links = ['get_image_tag', 'product']

    fieldsets = [
        (None, {
            'fields': ('product', 'picture', 'price', 'product_description')
        }),
        ('Offer Period', {
            'classes': ('wide',),
            'fields': ('start_date', 'expiration_date'),
        }),
        ('Reviews', {
            'classes': ('wide',),
            'fields': ('reviews', 'stars'),
        }),
    ]

    readonly_fields = ['active', ]

    list_filter = ['active', 'product']

    search_fields = ['product__make__name', 'product__model__name']


admin.site.register(ProductType)
