#! usr/bin/env python3
#! encoding=utf-8

import os

folder = "www.dni.gov"
Ph**** = "/home/devja3128/PROGRAMOWANIE/Ph****"
zapis = "/home/devja3128/study/webscraping/"

#adres = '{}/{}/{}'.format(Ph****,folder,nazwa_pliku)
#print(adres)

def sprawdzenie_folderu_zapisu(zapis, folder):
# Sprawdza czy folder istnieje, jeśli nie tworzy go
    lista = os.listdir(zapis)
    if folder in lista:
        pass #print("\nTen folder już istnieje\n")
    else:
        os.mkdir("{}/{}".format(zapis,folder))

#print("Pliki w folderze", zapis, ":")
#for item in lista:
    #print("/p",item)
sprawdzenie_folderu_zapisu(zapis, folder)
#tekst, który ma zostać dopisany
dodaj = "https://www.dni.gov/"
nazwa_pliku = "files.txt"

def dopisywanie(folder, nazwa_pliku, dodaj):
# otwiera plik, pobiera linie, dopisuje tekst + linie do innego pliku

    plik = open('/home/devja3128/Ph****/{}/{}'.format(folder,nazwa_pliku), 'r+')
    file = open('/home/devja3128/study/webscriping/{}/{}'.format(folder, nazwa_pliku), 'a+')


    for line in plik:
        if line.startswith('http'):
            file.write(line)
        else:
            file.write(dodaj+line)

    plik.close()
    file.close()

dopisywanie(folder, nazwa_pliku, dodaj)
