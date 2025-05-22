'''
Прочитати всі email з файлу І вивести статистику по доменам які зустрічалися у файлі по частоті від найбільшої кількості листів до найменшого.

mbox.txt mbox.txt
'''

import re
from collections import Counter

def count_domains(filename):
    with open(filename, 'r') as f:
        data = f.read()

    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data)
    domains = [email.split('@')[1] for email in emails]
    domain_count = Counter(domains)

    for domain, count in domain_count.most_common():
        print(f'{domain}: {count}')

count_domains('mbox.txt')


print(count_domains)

# collab.sakaiproject.org: 10782
# iupui.edu: 2241
# umich.edu: 2104
# nakamura.uits.iupui.edu: 1797
# indiana.edu: 736
# caret.cam.ac.uk: 667
# vt.edu: 442
# uct.ac.za: 408
# media.berkeley.edu: 231
# ufp.pt: 114
# gmail.com: 100
# txstate.edu: 70
# et.gatech.edu: 68
# whitman.edu: 68
# bu.edu: 60
# lancaster.ac.uk: 57
# stanford.edu: 54
# loi.nl: 45
# rsmart.com: 39
# unicon.net: 36
# asu.edu: 7
# utoronto.ca: 5
# ucdavis.edu: 4
# fhda.edu: 4
# berkeley.edu: 1

## Круто.
# [A-Z|a-z] — тільки оце якось... не дуже, бо це означає, що символ | теж рахується.
# Також хороше питання, скільки точно літер має бути в домені верхнього рівня.
# Але тут у нас достатньо цивільні дані, там електронні адреси не злипаються раптово з наступними словами тощо. Тому 2+ — це хороша ідея.