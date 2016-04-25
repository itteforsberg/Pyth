# !/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import csv
import fett
from sas7bdat import SAS7BDAT

def fet() -> object:
    print("This is fat!")

fet()

with SAS7BDAT('/Users/PKN/Documents/Source/tabe.sas7bdat') as f:
    for row in f:
        print(row)

fett.fettpy()

#con = None

try:
    con = psycopg2.connect(database='postgres', user='PKN')
    cur = con.cursor()

    cur.execute('SELECT * FROM public."ropd_Revisjonsoppdrag"')
    # cur.execute('SELECT "ropdOppdragsnavn" FROM public."ropd_Revisjonsoppdrag"')

    rows = cur.fetchall()
    for row in rows:
        words = row[1]
        print(words)

    # cur.execute('CREATE TABLE public."employment" (year integer PRIMARY KEY, age integer, alternative varchar(4), '
    #            'people integer)')
    # con.commit()

    fet()

except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)

# finally:
# if con:
#    con.close()

"""
with open('/Users/PKN/Downloads/MMMM3.csv', 'r') as f:
    firstline = f.readline()
    print(firstline)
    firstwords = firstline.split(';')
    print(int(firstwords[2].replace('"', '')))
    data = f.readlines()

    i = 0

    for line in data:
        words = line.split(';')
        label = ('age_%d' % i)
        print(label)

        # query = "ALTER TABLE employment ADD %s INT" % (label)

        # cur.execute(query)
        # con.commit()

        # print(words[0].replace('"', ''))

        for year in range(2014, 2101, 1):
            antall = words[year - 2014]
            # print('%s: %s' %(year, antall))
            # cur.execute("INSERT INTO employment VALUES(%d, %s, 'MMMM', %d)" % (int(year), label, int(antall)))
            # con.commit()

            cur.execute("UPDATE employment SET %s = %d WHERE year = %d" %(label, int(antall), int(year)))
            con.commit()

        i += 1
"""

cur.execute('SELECT sum_ages(age_1, age_1) FROM employment WHERE year = 2030')

rows = cur.fetchall()
for row in rows:
    print(row)

fett.fettpy()
