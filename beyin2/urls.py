#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.conf.urls.defaults import *
from django.contrib.auth.views import login
# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('oi.beyin2.views',

    (r'^$', 'main'),
    url(r'^idea_(?P<idea_id>\d+)/detail/$','idea_detail', name='idea_detail'),
    url(r'^order_(?P<order>\w+)/page_(?P<page_number>\d+)/$', 'main',name='main_page'),
    url(r'^order_(?P<order>\w+)/$', 'main',name='main_order'),
    url(r'^edited_(?P<idea_id>\d+)/$', 'main',name='main_post'),
    url(r'^add(?P<phase>\d+)/$','add_new', name='add_new'),
    url(r'^select/$','select_tags', name='select_tags'),
    url(r'^idea_(?P<idea_id>\d+)/edit/$','edit_idea', name='edit_idea'),
    url(r'^idea_(?P<idea_id>\d+)/delete/$','delete_idea', name='delete_idea'),
    url(r'^idea_(?P<idea_id>\d+)/duplicate/$',"mark_duplicate",name="mark_duplicate"),
    url(r'^idea_(?P<idea_id>\d+)/vote-(?P<vote>\d+)/from_(?P<come_from>\w+)/$',"vote",name="vote"),
    url(r'^(?P<idea_id>\d+)_is_favorite/$','is_favorite', name='is_favorite'),
    url(r'^(?P<idea_id>\d+)_add_remove_favorite/$','add_remove_favorite', name='add_remove_favorite'),
    url(r'^report_(?P<idea_id>\d+)/$','vote_values_report', name='vote_values_report'),
    url(r'^remove_image_(?P<image_id>\d+)/$','image_remove', name='image_remove'),
    #url(r'^(?P<blog_id>\d+)/$',"blog_goster",name="blog_goster"),
    #url(r'^(?P<blog_id>\d+)/(?P<yazi_id>\d+)/yorum_ekle/$',"yorum_ekle",name="yorum_ekle"),
)

