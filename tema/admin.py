#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.contrib import admin
from oi.tema.models import *

class ThemeItemAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {
                "fields": ("thumbnail", "title", "slug", "origin_url", "text",
                    "changelog", "status", "deny_reason", "tags")
                }),
            ("Diğer", {
                "classes": "collapse",
                "fields": ("author", "license", "rating", "download_count", "submit", "update", "comment_enabled")
                })
            )
    list_display = ("title", "author", "license", "status")
    list_display_links = ("title",)
    list_filter = ("status", "comment_enabled")
    search_fields = ["title", "text", "changelog"]

    class Media:
        js = ("js/jquery-1.4.3.min.js", "js/temaimages.js", "js/jquery.autocomplete.js", "js/taghelper.js")
        css = {
            "all": ("css/new/autocomplete.css",),
        }

class WallpaperAdmin(ThemeItemAdmin):
    list_display = ("title", "author", "license", "status")
    fieldsets = (
            (None, {
                "fields": ("thumbnail", "title", "slug","category", "origin_url", "text",
                    "changelog", "papers", "status", "deny_reason", "tags")
                }),
            ("Diğer", {
                "classes": "collapse",
                "fields": ("author", "license", "rating", "download_count", "submit", "update", "comment_enabled")
                })
            )

class DesktopScreenshotAdmin(ThemeItemAdmin):
    list_display = ("title", "author", "license", "status")
    fieldsets = (
            (None, {
                "fields": ("thumbnail", "title", "slug", "text",
                    "changelog", "image", "status", "deny_reason", "tags")
                }),
            ("Diğer", {
                "classes": "collapse",
                "fields": ("author", "license", "rating", "download_count", "submit", "update", "comment_enabled")
                })
            )

class FontAdmin(ThemeItemAdmin):
    list_display = ("title", "version", "author", "license", "status")
    fieldsets = (
            (None, {
                "fields": ("thumbnail", "title", "slug", "version",
                    "origin_url", "text", "changelog", "font", "status",
                    "deny_reason", "tags")
                }),
            ("Diğer", {
                "classes": "collapse",
                "fields": ("author", "license", "rating", "download_count", "submit", "update", "comment_enabled")
                })
            )

class IconSetAdmin(ThemeItemAdmin):
    list_display = ("title", "author", "license", "status")

class OpenOfficeTemplateAdmin(ThemeItemAdmin):
    list_display = ("title", "version", "author", "license", "status")

class OpenOfficeExtensionAdmin(ThemeItemAdmin):
    list_display = ("title", "version", "author", "license", "status")

class PackageScreenshotAdmin(ThemeItemAdmin):
    list_display = ("title", "version", "author", "license", "status")

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ThemeItem, ThemeItemAdmin)
admin.site.register(Wallpaper, WallpaperAdmin)
admin.site.register(DesktopScreenshot, DesktopScreenshotAdmin)
admin.site.register(Font, FontAdmin)
admin.site.register(WallpaperFile, admin.ModelAdmin)
admin.site.register(License, admin.ModelAdmin)
admin.site.register(WallpaperCategory, CategoryAdmin)
admin.site.register(OpenOfficeTemplateCategory)
admin.site.register(OpenOfficeExtensionCategory)
admin.site.register(OpenOfficeTheme)
admin.site.register(OpenOfficeTemplate,OpenOfficeTemplateAdmin)
admin.site.register(OpenOfficeExtension, OpenOfficeExtensionAdmin)
admin.site.register(IconSet,IconSetAdmin)
admin.site.register(PackageScreenshot, PackageScreenshotAdmin)
