from django.contrib import admin
from .models import KeyPair


class KeyPairAdmin(admin.ModelAdmin):
    list_display = ('key', 'uuid',)


admin.site.register(KeyPair, KeyPairAdmin)
