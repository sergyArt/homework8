import sqlite3


#try:
conn = sqlite3.connect('weather.db')
c = conn.cursor()
#c.execute('''insert into weather_data values(?,?,?,?,?);''', (707860,'Hurzuf','2018-11-16 20:39:14.580076',9.36,707860))

conn.commit()
row = c.fetchall()
for line in c.execute('''select count(*) from weather_data where id_city=519188'''):
    print(line)
#except Exception as e:
#print('Error in database level [', str(e), ']')
#    raise SystemExit(1)
#finally:
c.close()
conn.close()
