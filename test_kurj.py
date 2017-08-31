import csv
from decor import nice
import re



def fetch_data():
	
	with open(r'./kurj_log.csv', 'w', encoding='utf-8') as dest:

		writer = csv.writer(dest)
		writer.writerow(('lon', 'lat'))
		src = open('kurj_log.txt', 'r', encoding='utf-8')
		for i, line in enumerate(src):
			
			line = re.search('[\d,.;]+', line).group(0)
			# coords = line.strip().replace(',', '.').split(';')
			# coords = [float(x) for x in line.strip().replace(',', '.').split(';')]
			coords = line.split(';')
			writer.writerow((coords[0], coords[1]))
			print(i, coords[1], coords[0])
			
			# if i > 5000:
			# 	break

@nice
def main():

	fetch_data()
	

if __name__ == '__main__':
	main()