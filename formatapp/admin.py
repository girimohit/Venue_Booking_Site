from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Auditorium)
# admin.site.register(Amphitheatre)
# admin.site.register(SeminarHall)
# admin.site.register(SportsGround)
#admin.site.register(Your_Activity)

@admin.register(Auditorium)
class AuditorimAdmin(admin.ModelAdmin):
    list_display = ('day', 'time', 'eventType', 'user_id')

@admin.register(Amphitheatre)
class AmphitheatreAdmin(admin.ModelAdmin):
    list_display=('day','time', 'eventType', 'user_id')

@admin.register(SeminarHall)
class Semi(admin.ModelAdmin):
    list_display=('day','time', 'eventType','user_id')

@admin.register(SportsGround)
class sg(admin.ModelAdmin):
    list_display=('day','time', 'eventType','user_id')



# @admin.register(models.Collection)
# class CollectionAdmin(admin.ModelAdmin):
#     list_display = ["title", "products_count"]
#     list_per_page = 10
#     ordering = ["title"]
#     search_fields = ["title"]

# @admin.display(ordering="products_count")
# def products_count(self, collection):
#     url = (
#     reverse("admin:store_product_changelist") # app_model_page
#     + "?"  
#     + urlencode({"collection__id": collection.id})
#     )
#     return format_html('<a href="{}">{}</a>', url, collection.products_count)

# def get_queryset(self, request):
# return super().get_queryset(request).annotate(products_count=Count("product"))
