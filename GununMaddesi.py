# -*- coding: utf-8 -*-
# !/usr/bin/python3

import pywikibot
import locale
import datetime
from random import randint

locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

site = pywikibot.Site('tr', 'wikipedia')

one_day = datetime.timedelta(days=1)
baslangic = datetime.date(2015, 9, 1) # Bu tarihten öncesinde GM sorunlu. 
bugun = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
gelecekTarih = bugun + 2*one_day # 2 gün sonrası için kontrol yap
gelecekTarihStr = gelecekTarih.strftime("%Y-%m-%d")
kaynakTarih = baslangic + randint(0, int(str(bugun - baslangic).split(' days')[0])) * one_day # Başlangıç ve Bugün arasında rasgele bir tarih seç

logPage = pywikibot.Page(site, 'User:'+site.username()+'/Log/Günün Maddesi')

YarinSayfa = pywikibot.Page(site, 'Şablon:GM/' + gelecekTarihStr)

if (YarinSayfa.text == '' or YarinSayfa.exists() == False):  # Yarının GM sayfası yok
    Summary = 'Olumsuz'
    Durum = '\n* {{Çapraz}}'

    # Kaynak sayfa bul ve içeriğini kopyala
    kaynakSayfa = pywikibot.Page(site, 'Şablon:GM/' + kaynakTarih.strftime("%Y-%m-%d"))
    while kaynakSayfa.text == '' or kaynakSayfa.exists() == False:
        kaynakTarih += one_day # Sayfa boş çıktı. Sonraki güne geç.
        kaynakSayfa = pywikibot.Page(site, 'Şablon:GM/' + kaynakTarih.strftime("%Y-%m-%d"))

    # Kaynak sayfa ile gelecek GM sayfasını oluştur
    YarinSayfa.text = kaynakSayfa.text
    YarinSayfa.save('[[Şablon:GM/' + kaynakTarih.strftime("%Y-%m-%d") + ']] sayfasından kopyalandı.')

else:  # Yarının GM sayfası oluşturulmuş. Süper.
    Summary = 'Olumlu'
    Durum = '\n* {{Tamam}}'

# Log sayfasına rapor yaz
Durum += " [[Şablon:GM/%s | %s]]" %(gelecekTarihStr,gelecekTarihStr)
logPage.text += Durum
logPage.save(Summary)
