from django.contrib import auth

#  from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
# \\from django.db import models


class User(auth.models.user, auth.models.PermissionsMixin):

    def __str__(self):  # __unicode__(self):
        # return self.uniname
        return "@{}".format(self.username)
        # return self.title + 'by' + self.authors

    # \\class Colleges(models.Model):
    # \\objects = models.TextField(max_length=50)
    # \\cllgname = models.FileField(max_length=50)
    # \\uniname = models.FileField(max_length=100)
    # \\stname = models.FileField(max_length=100, blank=True, null=True)
    # \\dat = models.DateTimeField(auto_now=True)

    # \\def __str__(self):  # __unicode__(self):
    # \\return self.uniname
