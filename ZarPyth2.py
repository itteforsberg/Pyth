# !/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


def fett():
    print("This is fat!")


print("Detta er fett")
verdi = 30

fett()

for x in range(0, 5):
    print("We're on time %d" % (x))
    print(verdi + x)

con = None

try:
    con = psycopg2.connect(database='postgres', user='PKN')
    cur = con.cursor()
    cur.execute('SELECT * FROM public."ropd_Revisjonsoppdrag"')

    rows = cur.fetchall()
    for row in rows:
        print(row)

    fett()

except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)

finally:
    if con:
        con.close()

fett()
