#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django import forms
from oi.beyin2.models import Idea, ScreenShot

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'description', 'status', 'category' )

class IdeaDuplicateForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('duplicate',)

class ScreenShotForm(forms.ModelForm):
    class Meta:
        model = ScreenShot
        fields = ('image',)
