from selenium import webdriver
import time
import pandas as pd
from datetime import datetime

PATH = "C:\python\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://rateyourmusic.com/charts/top/album/all-time/exc:live,archival/#results")
consent = driver.find_element_by_class_name("fc-button-label")
consent.click()
time.sleep(2)
datesList = []
ratingsList = []
genreList = []
N = 10
def spaceCount(date):
	count = 0
	for i in date:
		if(i.isspace()):
			count=count+1
	return count
	
for page in range(N):
	main = driver.find_element_by_id("page_chart_main")
	releases = main.find_elements_by_class_name("chart_item_release")
	for release in releases:
		releaseDate = release.find_element_by_class_name("topcharts_item_releasedate")
		releaseDate = releaseDate.text
		datesList.append(releaseDate)
		rating = release.find_element_by_class_name("topcharts_avg_rating_stat")
		rating = rating.text
		ratingsList.append(rating)
		genre = release.find_elements_by_class_name("topcharts_item_genres")
		newlist = []
		for i in genre:
			genres = i.text
			newlist.append(genres)
		genreList.append(newlist)
	time.sleep(5)
	next = main.find_element_by_class_name("ui_pagination_next")
	next.click()

for date in datesList:
	if spaceCount(date) == 0:
		date = "2 July " + date
	if spaceCount(date) == 1:
		date = "15 " + date
data = {'Date': datesList, 'Rating': ratingsList, 'Genres': genreList}
df = pd.DataFrame(data)
df.to_csv('musicData.csv')
