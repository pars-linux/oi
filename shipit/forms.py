#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

import re

from django import forms

from oi.shipit.models import *

class CdClientForm(forms.ModelForm):
    class Meta:
        model = CdClient
        exclude = ("sent", "taken", "hash", "confirmed", "date", "ip")

    def clean_postcode(self):
        postcode = self.cleaned_data["postcode"]
        if postcode:
            match = re.match(re.compile(r"^\d{5}$"), postcode)
            if not match:
                raise forms.ValidationError("Lütfen geçerli bir posta kodu girin veya boş bırakın.")
        return postcode

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
