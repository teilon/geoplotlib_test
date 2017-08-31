import psycopg2


def fill_region():
	conn = psycopg2.connect('dbname=manfred user=manfred')
	cur = conn.cursor()

	regions = [
		'Карагандинская область',
		'Акмолинская область',
		'Западно-Казахстанская область',
		'Павлодарская область',
		'Мангистауская область',
		'Актюбинская область',
		'Алматы',
		'Кызылординская область',
		'Костанайская область',
		'Южно-Казахстанская область',
		'Столица',
		'Атырауская область',
		'Восточно-Казахстанская область',
		'Арендуется',
		'Северо-Казахстанская область',
		'Алматинская область',
		'Жамбыльская область'
	]

	sql = 'INSERT INTO region (name) VALUES (\'{}\');'

	for reg in regions:

		print(sql.format(reg))
		cur.execute(sql.format(reg))

	conn.commit()

	cur.close()
	conn.close()


def fill_state_status():
	conn = psycopg2.connect('dbname=manfred user=manfred')
	cur = conn.cursor()

	state_status = [
		'City of republican importance',
		'Regional center',
		'City of regional subordination',
		'District center',
		'City of district subordination'
	]

	sql = 'INSERT INTO state_status (name) VALUES (\'{}\');'

	for st in state_status:

		print(sql.format(st))
		cur.execute(sql.format(st))

	conn.commit()

	cur.close()
	conn.close()

def main():

	print('start')

	# fill_state_status()
	# fill_region()
	
	print('end.')




if __name__ == '__main__':
	main()