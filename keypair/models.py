from django.db import models
import uuid


class KeyPair(models.Model):
    key = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)