from django.urls import path
from keypair.views import generate_uuid
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'keypair'

urlpatterns = [
    path('generate_uuid/', generate_uuid, name='gen_key'),
]

urlpatterns = format_suffix_patterns(urlpatterns)