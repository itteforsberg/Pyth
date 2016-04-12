# !/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import csv


def fett() -> object:
    print("This is fat!")


print("Detta er fett")
verdi = 30

fett()

str = "0000000this is string example....wow!!!0000000";
print(str.strip('e'))

for x in range(0, 5):
    y = 39
    print("We're on time %d" % x)
    print(verdi + x)

con = None

try:
    con = psycopg2.connect(database='postgres', user='PKN')
    cur = con.cursor()

    cur.execute('SELECT * FROM public."ropd_Revisjonsoppdrag"')
    cur.execute('SELECT "ropdOppdragsnavn" FROM public."ropd_Revisjonsoppdrag"')

    rows = cur.fetchall()
    for row in rows:
        print(row)

    #cur.execute('CREATE TABLE public."employment" (year integer PRIMARY KEY, age integer, alternative varchar(4), '
    #            'people integer)')
    #con.commit()

    fett()

except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)

finally:
    if con:
        con.close()

with open('/Users/PKN/Downloads/MMMM3.csv', 'r') as f:
    firstline = f.readline()
    firstwords = firstline.split(';')

    data = f.readlines()
    words = data.split(';')

    for line in range(0, 5):


        print(words[0].replace('"', ''))

        #cur.execute("INSERT INTO employment VALUES(1,'Audi',52642)")

fett()
