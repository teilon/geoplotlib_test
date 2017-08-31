import psycopg2

import csv

from decor import nice


def fetch_data():
	conn = psycopg2.connect('dbname=manfred user=manfred')
	cur = conn.cursor()

	sql = 'SELECT * FROM cities'

	cur.execute(sql)
	rows = cur.fetchall()


	conn.commit()

	cur.close()
	conn.close()


	# with open(r'/home/ubba/Documents/cities/city/data.csv', 'w', encoding='utf-8') as f:
	with open(r'./data.csv', 'w', encoding='utf-8') as f:	
		writer = csv.writer(f)

		writer.writerow(('name', 'lat', 'lon'))

		for r in rows:
			writer.writerow((r[1], r[5], r[6]))


@nice
def main():

	fetch_data()
	

if __name__ == '__main__':
	main()