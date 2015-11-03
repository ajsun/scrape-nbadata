from bs4 import BeautifulSoup
import urllib2
import re
import csv

url = "http://www.basketball-reference.com/leagues/NBA_2015_games.html#games::none"

baseurl = "http://www.basketball-reference.com"

response = urllib2.urlopen(url)
html = response.read()

soup = BeautifulSoup(html, "lxml")

link_list = []

links = soup.find_all('a')
for i in links:
	if (i.string == "Box Score"):
		string = i['href']
		string = string.replace("/boxscores/", "/boxscores/shot-chart/")
		link_list.append(string);

def write(text1, text2):
	with open('nba2015.csv', 'a') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerow([text1, text2])
for j in link_list:
	new_url = baseurl + j
	response1 = urllib2.urlopen(new_url)
	html1 = response1.read()
	soup1 = BeautifulSoup(html1, "lxml")

	ids = soup1.find_all(id=re.compile('shot_chart-'))

	teams = []
	for x in ids:
		teams.append(x['id'].replace("shot_chart-", ""))

	write(teams[0], teams[1])

	stats = soup1.find_all(class_="stat_total");
	#print stats
	values = []
	for stat in stats:
		elements = stat.find_all('td')
		for element in elements:
			values.append(element.contents[0])
	x= int(values[4])*1+int(values[7])*2
	y= int(values[17])*1+int(values[20])*2
	write(x, y)
