#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

import re

from django import forms

from oi.shipit.models import *

class TurkishIdentityNumberField(forms.Field):
    """
    A Republic of Turkey Identity number.

    Checks the following rules to determine whether the number is valid:

        * Last 2 characters of ID should validate the following algorithm.
    """
    default_error_messages = {
        'invalid': 'Lütfen geçerli bir TC kimlik numarası girin.',
    }

    def clean(self, value):
        super(TurkishIdentityNumberField, self).clean(value)
        if not value:
            return u''
        match = re.match(re.compile(r"^\d{11}$"), value)
        if not match:
            raise forms.ValidationError(self.error_messages['invalid'])

        odds, evens = 0, 0
        for i in range(9):
            if i % 2:
                evens += int(value[i])
            else:
                odds += int(value[i])

        t1 = odds * 3 + evens
        c1 = (10 - t1 % 10) % 10
        t2 = c1 + evens
        t3 = t2 * 3 + odds
        c2 = (10 - t3 % 10) % 10

        if c1 != int(value[9]) or c2 != int(value[10]):
            raise forms.ValidationError(self.error_messages['invalid'])

        return value

class CdClientForm(forms.ModelForm):
    tcidentity = TurkishIdentityNumberField(label="TC kimlik no")
    phone_area = forms.CharField(label="Telefon Numarası", max_length=3, widget=forms.TextInput(attrs={"style":"width:30px;margin-right:5px"}))
    phone_number = forms.CharField(label="Telefon Numarası", max_length=7, widget=forms.TextInput(attrs={"style":"width:130px"}))
    class Meta:
        model = CdClient
        exclude = ("sent", "taken", "hash", "confirmed", "date", "ip", "reason", "number_of_cds", "company", "postcode")

    def clean(self):
        if self.cleaned_data.has_key("number_of_cds"):
            if self.cleaned_data["number_of_cds"]>1:
                if not self.cleaned_data["reason"]:
                    raise forms.ValidationError("Birden fazla CD istiyorsanız sebebini yazmalısınız.")
        return self.cleaned_data

    def clean_phone_area(self):
        phone_area = self.cleaned_data["phone_area"]
        match = re.match(re.compile(r"^\d{3}$"), phone_area)
        if not match:
            raise forms.ValidationError("Lütfen geçerli bir alan kodu girin.")
        return phone_area

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        match = re.match(re.compile(r"^\d{7}$"), phone_number)
        if not match:
            raise forms.ValidationError("Lütfen geçerli bir telefon numarası girin.")
        return phone_number

    def clean_number_of_cds(self):
        number_of_cds = self.cleaned_data["number_of_cds"]
        if number_of_cds < 1:
            raise forms.ValidationError("Lütfen geçerli bir CD sayısı girin.")
        return number_of_cds

class CdClientChangeForm(CdClientForm):
    class Meta:
        model = CdClient
        exclude = ("ip", "hash")

class CodeForm(forms.Form):
    code = forms.IntegerField(label="Sipariş kodu")

    def clean_code(self):
        icode = self.cleaned_data["code"]
        code = str(icode)
        if len(code) < 3 or code[:3] != "700":
            raise forms.ValidationError("Girdiğiniz kod geçerli değil")
        else:
            code = code[3:]
            try:
                CdClient.objects.get(id=int(code))
            except:
                raise forms.ValidationError("Girdiğiniz kod geçerli değil")
        return icode

class CargoForm(forms.ModelForm):
    date = forms.DateField(label="Gönderme Tarihi", input_formats=("%d/%m/%Y","%Y-%m-%d"), help_text="15/08/2009 gibi")
    class Meta:
        model = Cargo
        exclude = ("cdclient")
