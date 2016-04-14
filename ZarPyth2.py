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
    print("We're on time %d %d" % (x, x))
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

#finally:
    #if con:
    #    con.close()

with open('/Users/PKN/Downloads/MMMM3.csv', 'r') as f:
    firstline = f.readline()
    print(firstline)
    firstwords = firstline.split(';')
    print(int(firstwords[2].replace('"', '')))
    data = f.readlines()

    i = 0

    for line in data:
        words = line.split(';')
        label = ('age_%d' %i)
        print(label)

        query = "ALTER TABLE employment ADD %s INT" % (label)
        cur.execute(query)
        con.commit()

        #print(words[0].replace('"', ''))

        for year in range(2014, 2101, 1):
            antall = words[year - 2014]
            #print('%s: %s' %(year, antall))

            #cur.execute("INSERT INTO employment VALUES(%d, %s, 'MMMM', %d)" % (int(year), label, int(antall)))
            #con.commit()

        i += 1

fett()
