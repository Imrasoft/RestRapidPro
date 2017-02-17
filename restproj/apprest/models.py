from __future__ import unicode_literals
from temba_client.v2 import TembaClient

from django.db import models


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=128, unique=True)
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    @classmethod
    def fetch(cls, domain_name, token_id):
        client = TembaClient(domain_name, token_id)
        for page_data in client.get_groups().iterfetches(retry_on_rate_exceed=True):
            for group1 in page_data:
                cls.objects.create(name=group1.name, count=group1.count)

        return True


contact_groups = Group.fetch('http://localhost:8000', '9af0741e535fe308b6f529aac764babfe19ee091')
