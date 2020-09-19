[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) [![Pywikibot](https://img.shields.io/badge/Pywikibot-4.3.0-green.svg)](https://www.mediawiki.org/wiki/Manual:Pywikibot) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Günün maddesi

Eğer günün maddesi oluşturulmamış ise geçmiş günlerden rastgele bir GM sayfası seçip onun içeriği ile sayfayı oluşturur.

## Kurulum

* Kullanılacak bilgisayarda/sunucuda pywikibot kütüphanesi [kurulur ve konfigüre edilir](https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation)
* ```deneme.py``` betiği çalıştırılır. [Deneme sayfası](https://tr.wikipedia.org/wiki/Vikipedi:Deneme_tahtas%C4%B1) üzerinde test yapılır
* ```GununMaddesi.py``` betiği çalıştırılır. Program test edilir
* Programı her gece otomatik çalıştırmak için [Toolforge](https://wikitech.wikimedia.org/) üzerine aşağıdaki [cron](https://en.wikipedia.org/wiki/Cron) komutu düzenlenerek kaydedilir.
  
```text
55 23 * * *   /usr/bin/jsub    -N Vikipedi-GununMaddesi        -once -quiet python3 /data/project/mavrikant/pywikibot/pwb.py /data/project/mavrikant/GununMaddesi/GununMaddesi.py
```

## Geliştiriciler

* [Mavrikant](https://tr.wikipedia.org/wiki/Kullan%C4%B1c%C4%B1:Mavrikant) (11 Ekim 2015)
* [Evrifaessa](https://tr.wikipedia.org/wiki/Kullan%C4%B1c%C4%B1:Evrifaessa) (19 Eylül 2020)

## License

* This project is licensed under the terms of the  [MIT License](https://choosealicense.com/licenses/mit/)
* Copyright © 2015 M. Serdar Karaman
