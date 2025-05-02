# -*- coding: utf-8 -*-
#!/usr/bin/python3

try:
    import pywikibot
except ImportError:
    print("Pywikibot not found. Please install it using: pip3 install pywikibot")
    exit(1)

try:
    site = pywikibot.Site('tr', 'wikipedia')
    site.login()  # Explicitly login
    
    page = pywikibot.Page(site, "Vikipedi:Deneme tahtası")
    
    username = site.username()
    page.text = '\n== ' + username + ' test ==\nDeneme deneme 123 --~~~~'
    page.save(username + " ile deneme mesajı ekleniyor")
    
    print(page.text)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

exit(0)