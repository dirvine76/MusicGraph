import pandas as pd

def loopGenre (genres):
	for genre in genres:
		genreStr = ""
		for i in genre:
			i = chooseGenre(i)
			genreStr = genreStr + i
		newGenre = chooseGenre(genreStr)
	return newGenre
	if "Pop" in genre:
		return "Pop"
		
def chooseGenre(genre):
	if "Pop" in genre:
		return "Pop"
	elif "Punk" in genre:
		return "Punk"
	elif "Bop" in genre:
		return "Jazz"
	elif "Jazz" in genre:
		return "Jazz"
	elif "Metal" in genre:
		return "Metal"
	elif "Rap" in genre:
		return "Rap/Hip Hop"
	elif "Hip Hop" in genre:
		return "Rap/Hip Hop"
	elif "IDM" in genre:
		return "Electronic"
	elif "Electronic" in genre:
		return "Electronic"
	elif "Techno" in genre:
		return "Electronic"
	elif "Rock" in genre:
		return "Rock"
	elif "rock" in genre:
		return "Rock"
	else:
		return "Other"

df = pd.read_csv('musicData.csv', index_col = 0)
genres = df['Genres']
print(genres)
BIGLIST = []
for list in genres:
	list = chooseGenre(list)
	BIGLIST.append(list)
	
df.iloc[:, -1] = BIGLIST

df.to_csv('newMusicData.csv')