import psycopg2
import numpy as np
import matplotlib.pyplot as mp

#conn
con = psycopg2.connect("dbname=g484-serebryakov user=postgres host=127.0.0.1 port=5432")
cur = con.cursor()
cur.execute("set search_path='lab_view';")
cur.execute("select x, y from positive order by x;")
arr = cur.fetchall()
cur.close()
con.close()

x, y = np.array(arr).T
mp.plot(x, y, marker='o')
mp.title('sin wave')
mp.xlabel('x')
mp.ylabel('sinx')
mp.grid(True, which='both')
mp.axhline(y=0, color='k')
mp.show()