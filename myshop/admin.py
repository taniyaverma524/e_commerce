from django.contrib import admin
from .models import Categorie ,Sub_Categorie, Product , Size_quantity , Upload_images
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('categories_name',)}
    list_display = ['categories_name','slug','updated','created']

admin.site.register(Categorie,CategorieAdmin)




class Sub_CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ['categories','product_name','slug']


admin.site.register(Sub_Categorie,Sub_CategorieAdmin)


def get_picture_preview(obj):


    if obj.pk:
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (obj.image)
        # return mark_safe("""<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
        #     src=obj.picture.url,
        #     title=obj.product_id,
        # )
        )

    return _("(choose a picture and save and continue editing to see the preview)")

get_picture_preview.short_description = _("Picture Preview")

class Upload_imagesInline(admin.TabularInline):
    model = Upload_images
    extra = 1
    fields = ['image',get_picture_preview]
    readonly_fields = [get_picture_preview]
    raw_id_fields = ["image_id"]

class Size_quantityInline(admin.TabularInline):
    model = Size_quantity
    extra = 0
    raw_id_fields = ["product"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id','brand_name']
    inlines = [Upload_imagesInline,Size_quantityInline ]


admin.site.register(Product ,ProductAdmin)