import hashlib
import os
import json
import subprocess
import urllib3
import socket
import requests
import colorama
import random
import string
from colorama import Fore, Back, Style, init
print("""
  _________  ___  _______     __ _______      ____ __  ____  __________  __
 / ___/ __ \/ _ \/ __/ _ \   / // / / / | /| / / //_/ / __ \/ __/ ___/ |/_/
/ /__/ /_/ / // / _// // /  / _  /_  _/ |/ |/ / ,<   / /_/ / _// /___>  <  
\___/\____/____/___/____/  /_//_/ /_/ |__/|__/_/|_|  \____/_/  \___/_/|_|  
               
      YouTube : HAWK DEFENDER
      Coder : H4WK OFCX
      İnstagram : hawkofcx 
      git hub : hawk-unity
""")
print("""
1-  port tarama
2 - ip tracer
3 - md5 kır(api)
4 - md5 oluştur
5 - whois kullan
6 - nmap(nmap -sS -sV)
7-  xss vuln
8 - dmitry kullan
9 - sqlmap ile db çek
10 - şifre oluştur
11 - dnsmap
12 - urlcrazy kullan 
13 - geoip
""")
veri = input("Seçenek seç => ")
if veri == "1":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    author = "coded by h4wk ofcx"
    host = input(Fore.RED + "LÜTFEN İP ADRESİNİ GİRİNİZ : ")
    port = int(input(Fore.RED + "TARATILACAK PORT ADRESİNİ GİRİNİZ : "))
    def portScanner(port):
        if s.connect_ex((host, port)):
            print(Fore.GREEN + "BU PORT KAPALI")
            input("çıkış yapmak için bir tuşa bas")
        else:
            print(Fore.GREEN + "BU PORT AÇIK")
            input("çıkış yapmak için bir tuşa bas")
    portScanner(port)
if veri == "2":

    target= input("[+]Target -> : ")
    data = subprocess.check_output(["curl",f"http://ip-api.com/json/" + target ]).decode("utf-8")
    json.loads(data)
    print("İp Adress   => " , json.loads(data)["query"])
    print("şehir => " , json.loads(data)["city"])
    print("Ülke  => " , json.loads(data)["country"])
    print("Posta Kodu  => " , json.loads(data)["zip"])
    print("Host   => " , json.loads(data)["isp"])
    print("Host   => " , json.loads(data)["org"])
    print("lat  => " , json.loads(data)["lat"])
    print("lat  => " , json.loads(data)["lon"])
    print("adres için  lat değeri ve lon değerini sayılarını google'a yazınız ")
if veri == "3" : 
    dat2 = input("Kırılacak MD5 Hash ==> ")
    print("")
    print("_______________________________")
    print("")
    response = requests.get('http://www.nitrxgen.net/md5db/' + dat2).text
    print("crack sonucu => " , response)
    print("")
    print("cracklenen hash => " ,dat2)
    print("")
    print("_______________________________")
if veri == "4":
    user = input("YAZIYI GİR :  ")
    h = hashlib.md5(user.encode())
    h2 = h.hexdigest()        
    print(h2)
if veri == "5":
    whois = input("whois için site =>")
    os.system("whois ",whois)
if veri == "6":
    portat = input("İp Adresi => ")
    os.system("sudo nmap -sS -sV ",portat)
if veri == "7":
    target = input("Hedef URL : ")
    payload = ("<script>alert(123123);</script>")
    req = requests.post(target + payload)
    if payload in req.text:
        print ("XSS Açığı keşfetildi...")
        print ("Saldırı Yükü: "+payload)
    else:
        print ("Güvenli ")
if veri == "8":
   os.system("dmitry -w ", site)
   os.system("dmitry -o ", site)
   os.system("dmitry -i ", site)
   os.system("dmitry -n ", site)
   os.system("dmitry -s ", site)
   os.system("dmitry -e ", site)
   os.system("dmitry -p ", site)
if veri == "9":
    vulnsqlk = input("URL: ")
    os.system("sqlmap -u"+vulnsqlk+"--tables --random-agent --tamper=space2comment")
if veri == "10":
    def rastgele_sifre_uret(uzunluk):
        harfler =  string.ascii_letters + string.digits + string.punctuation
        sonuc = ''.join(random.choice(harfler) for i in range(uzunluk))
        return sonuc
    try : 
        karakter_sayı = int(input("KAC KARAKTER OLSUN İSTERSİN : "))
        print("ŞİFRENİZ : " + rastgele_sifre_uret(karakter_sayı)) 
        print("ŞİFRENİZ : " + rastgele_sifre_uret(karakter_sayı))
    except ValueError:
        print("Lütfen sadece sayı girin!")
if veri == "11":
   dns = input("dnsmap çalıştırmak için url => ")
   os.system("dnsmap ",dns)
if veri == "12":
    url = input("url gir(site) => ")
    os.system("urlcrazy ",url)
if veri == "13":
    ipadres = input("ip adress => ")
    os.system("curl http://api.hackertarget.com/geoip/?q=",ipadres)