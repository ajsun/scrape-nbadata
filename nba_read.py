import csv

with open('nba.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		