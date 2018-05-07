# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
# import urllib,re
import re
from urllib.request import urlopen
url_list = ["addeofitmke.com",
"aerialhippiemke.com",
"annabelleaerial.com",
"balancefitnesswi.com",
"barredistrict.com",
"bellaviadancestudio.com",
"brewfitnessmke.com",
"ellewellstudio.com",
"equilibriumevolution.com",
"fastforwardfitness.org",
"gethotyoga.com",
"yogamke.com",
"impactfitstudio.com",
"innerlightyogastudios.com",
"ironfistfit.com",
"mindfulmatterswellness.com",
"fueledbypower.com",
"racestartfit.com",
"revitalize-pt.com",
"studio83pilates.com",
"milwaukeefitnessasylum.com",
"urbanommke.com",
"yogasix.com",
"yogaloftmke.com"]
# for i in url_list:
#     f = urlopen(i)
#     s = f.read().decode('utf-8')
#
#     tel = re.findall(r"\+\d{2}\s?0?\d{10}",s)
#     email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
#     print([i, email])
from urllib.request import urlopen
import re

#connect to a URL
website = urlopen("http://www.sprkfitness.com")

#read html code
html = website.read().decode("utf-8")

#use re.findall to get all the links
# links = re.findall('"((http|ftp)s?://.*?)"', html)
# print(links)
for l in url_list:
    # making up the url
    main_url = "http://www." + l
    try:
        f = urlopen(main_url)
        s = f.read().decode('utf-8')
        #     tel = re.findall(r"\+\d{2}\s?0?\d{10}",s)
        email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
    except:
        email = "None"
    finally:
        print(l, email)






