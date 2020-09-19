# -*- coding: utf-8 -*-
# !/usr/bin/python3

# gerekli kütüphaneleri dahil et
import pywikibot
import locale

# locale ayarı
locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

site = pywikibot.Site('tr', 'wikipedia')
page = pywikibot.Page(site, "Vikipedi:Deneme tahtası")

# Deneme sayfasına mesaj ekle.
page.text += '\n== ' + site.username() + ' test ==\nDeneme deneme 123 --~~~~'
page.save(site.username() + " ile deneme mesajı ekleniyor")

# Sayfanın son halini ekrana yazdır
print(page.text)

# Programı kapat
exit(0)