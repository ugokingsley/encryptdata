from django.db import models
from django.contrib.auth.hashers import make_password


class EncryptData(models.Model):
    text = models.CharField(max_length=256, unique=True, default=None)
    original = models.CharField(max_length=256, unique=True, default=None, null=True, blank="True")
    pub_date = models.DateTimeField('date published', null=True)

    def save(self, *args, **kwargs):
    	self.original = self.text
    	some_salt = 'h-4^44m!6=hk&6g(2np57)-i80_p4ws!o_8&ajvo7le9nao2r'
    	self.text = make_password(self.text, some_salt)
    	super().save(*args, **kwargs)

    def __str__(self):
       return self.text

