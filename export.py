import psycopg2


#conn
con = psycopg2.connect("dbname=g484-serebryakov user=postgres host=127.0.0.1 port=5432")
cur = con.cursor()
cur.execute("set search_path='lab_view';")
cur.execute("select x, y from fn order by x;")
arr = cur.fetchall()
cur.close()
con.close()
f = open("sine.csv", "w")
for row in arr:
 f.write(f"{row[0]},{row[1]}\n")
f.close()
