#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.db import models
from django import forms
from django.contrib import admin

from oi.settings import CITY_LIST

class Petitioner(models.Model):
    firstname = models.CharField("Ad", max_length=30)
    lastname = models.CharField("Soyad", max_length=30)
    city = models.CharField("Şehir", blank=True, choices=CITY_LIST, max_length=40)
    job = models.CharField("Meslek", max_length=30)
    email = models.EmailField("E-posta", max_length=50)
    homepage = models.URLField("Ana Sayfa", blank=True, verify_exists=False, unique=False)
    signed = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='İmzalama tarihi')
    activation_key = models.CharField("Etkinleştirme Anahtarı", max_length=40)
    is_active = models.BooleanField("Etkin")
    inform = models.BooleanField("Haberdar Et")

    def __unicode__(self):
        return "%s %s" % (self.firstname, self.lastname)

    class Meta:
        verbose_name = "İmzalayan"
        verbose_name_plural = "İmzalayanlar"

class PetitionerAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "job", "city", "email", "homepage", "signed", "is_active", "inform")
    ordering = ("-signed",)
    search_fields = ("firstname", "lastname", "job")

admin.site.register(Petitioner, PetitionerAdmin)

class PetitionForm(forms.Form):
    firstname = forms.CharField(label="Ad:", max_length=30)
    lastname = forms.CharField(label="Soyad:", max_length=30)
    city = forms.ChoiceField(label="Şehir:", choices=CITY_LIST)
    job = forms.CharField(label="Meslek:", max_length=30)
    email = forms.EmailField(label="E-Posta:")
    homepage = forms.URLField(label="Web Sayfası:", verify_exists=False, required=False, help_text="(zorunlu değil)")
    inform = forms.BooleanField(label="Etkinliklerden haberdar et:", required=False, help_text="Özgürlükİçin'in diğer etkinliklerinden haberdar olmak için işaretleyin.")

    def clean_email(self):
        field_data = self.cleaned_data["email"]

        if not field_data:
            return ''

        u = Petitioner.objects.filter(email=field_data)
        if len(u) > 0:
            raise forms.ValidationError(u"Bu e-posta adresi ile daha önceden kayıt yapılmış")

        return field_data
