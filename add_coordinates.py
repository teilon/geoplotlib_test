import psycopg2


def fetch_coordinate():

	f = open('cities_coordinates.txt', 'r')
	for r in f:
		arr = r.split(';')
		name = arr[0]
		lat = arr[1]
		lon = arr[2]

		save_to_db(name, lat, lon)


def save_to_db(name, lat, lon):
	conn = psycopg2.connect('dbname=manfred user=manfred')
	cur = conn.cursor()

	sql = 'UPDATE cities SET latitude = {}, longitude = {} where name = \'{}\';'

	# print(sql.format(lat, lon, name))
	cur.execute(sql.format(lat, lon, name))

	conn.commit()

	cur.close()
	conn.close()


def main():
	fetch_coordinate()

	print('end')



if __name__ == '__main__':
	main()


