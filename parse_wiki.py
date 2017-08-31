import requests
from bs4 import BeautifulSoup

import psycopg2

import re


def grab_site():

	# source = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD%D0%B0'
	# r = requests.get(source)
	# parse(r.text)

	html = open('cities.html').read()
	parse(html)

def parse(html):

	soup = BeautifulSoup(html, 'lxml')
	div = soup.find('div', class_='mw-parser-output')

	table = div.find('table', class_='wikitable sortable jquery-tablesorter')
	
	tbody = table.contents[2]
	trs = tbody.find_all('tr')

	print('length {}'.format(len(trs)))

	pattern='\d+'
	
	for tr in trs:

		tds = tr.find_all('td')

		data = {
			'name' : tds[1].text,
			'population' : re.search(pattern, tds[8].text).group(0),
			'status' : tds[9].text,
			'parent' : tds[10].find('a').text	
		}		

		to_db(data)

	print('end')


def to_db(data):
	
	sql_select_region = 'SELECT id FROM region WHERE name = \'{}\';'
	sql_insert = 'INSERT INTO cities (name, population, status, region) VALUES (\'{}\', {}, {}, {});'
	sql_upsert = 'execute procedure upsert_to_cities(name, population, status, region) VALUES (\'{}\', {}, {}, {});'

	conn = psycopg2.connect('dbname=manfred user=manfred')
	cur = conn.cursor()

	cur.execute(sql_select_region.format(data['parent']))
	region = cur.fetchone()[0]
	
	cur.callproc('upsert_to_cities', (data['name'], data['population'], data['status'], region))
	# cur.execute(sql_insert.format(data['name'], data['population'], data['status'], region))
	# print(sql_insert.format(data['name'], data['population'], data['status'], region))

	conn.commit()

	cur.close()
	conn.close()

	





def main():
	grab_site()

if __name__ == '__main__':
	main()