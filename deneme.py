# -*- coding: utf-8 -*-
# !/usr/bin/python3

# gerekli kütüphaneleri dahil et
import pywikibot
import locale
import json

# locale ayarı
locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

site = pywikibot.Site('tr', 'wikipedia')
page = pywikibot.Page(site, "Vikipedi:Deneme tahtası")

# Giriş denemesini sonucunu ekrana JSON ile düzenleyerek yazdır
print(page.text)

# 2 bölümü birbirinden ayır
print("\n-------------------------------------------------------------------------\n")

# Deneme sayfasına mesaj ekle.
page.text += '\n== ' + site.username() + ' test ==\nDeneme deneme 123 --~~~~'
page.save(site.username() + " ile deneme mesajı ekleniyor")

# Sonucu ekrana JSON ile düzenleyerek yazdır
print(page.text)

# Programı kapat
exit(0)