from django.db import models
from .utils import code_generator, create_shotcode
# Create your models here.

class KirrUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrUrlManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=False)
        return qs
    def refresh_shotcode(self, items=100):
        print(items)
        qs = KirrUrl.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]

        new_code = 0
        for q in qs:
            q.shotcode = create_shotcode(q)
            print(q.id)
            q.save()
            new_code += 1
        return "New codes made: {i}".format(i=new_code)

class KirrUrl(models.Model):
    url = models.CharField(max_length=220)
    shotcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    #emty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = KirrUrlManager()
    some_random = KirrUrlManager()

    def save(self, *args, **kwargs):
        if self.shotcode is None or self.shotcode =="":
            self.shotcode = create_shotcode(self)
        super(KirrUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
