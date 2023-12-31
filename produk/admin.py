from django.contrib import admin
from .models import Buku, Penulis_Buku, Penerbit_Buku

# Register your models here.
class DataBuku(admin.ModelAdmin):
    readonly_fields = ['slug', 'updated', 'created']

admin.site.register(Buku, DataBuku)
admin.site.register(Penulis_Buku, DataBuku)
admin.site.register(Penerbit_Buku, DataBuku)