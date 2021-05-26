from rest_framework import serializers
from .models import KeyPair
import uuid


class KeySerializer(serializers.ModelSerializer):

    class Meta:
        model = KeyPair
        fields = ('key', 'uuid', )

    def create(self, validated_data):
        gen_uuid = uuid.uuid4()
        key = KeyPair.objects.create(uuid=gen_uuid)
        return key