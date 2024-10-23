import urllib.request
import json
import time

obj_fichier = open('controltower_access.log', 'r')
begin_balise = '['
end_balise = ']'

for i in range(268351):
    while True:
        ligne = obj_fichier.readline()
        pos_begin = ligne.find(begin_balise)
        pos_end = ligne.find(end_balise)
        if pos_begin != -1:
            break

    l = len(begin_balise)
    extract = ligne[pos_begin + l:pos_end]
    print (extract)

obj_fichier.close()