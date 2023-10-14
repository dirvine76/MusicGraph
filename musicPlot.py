import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import datetime
color = '#ffffff'
fig, ax = plt.subplots()
def spaceCount(date):
	count = 0
	for i in date:
		if(i.isspace()):
			count=count+1
	return count

df = pd.read_csv('newMusicData.csv')
newDates = []
dates = df['Date']
ConvDates = []
for date in dates:
	if spaceCount(date) == 0:
		newDate = "2 July " + date
	elif spaceCount(date) == 1:
		newDate = "15 " + date
	else:
		newDate = date
	newDates.append(newDate)
for release in newDates:
	timeconv = datetime.datetime.strptime(release, "%d %B %Y")
	ConvDates.append(timeconv)

colors = {'Rock':'#fe2f4b', 'Pop':'#0d3bc9', 'Electronic':'#2fad52', 'Jazz':'#9c379f', 'Rap/Hip Hop':'#34bbe7', 'Metal':'#fc98de', 'Other':'#b3a4b5', 'Punk':'#d86926'}
df['Date'] = ConvDates
#plt.scatter(ConvDates, df['Rating'], c=df['Genres'].map(colors), label = df['Genres'])

grouped = df.groupby('Genres')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='Date', y='Rating', label=key, color=colors[key], s = 8)
ax.legend(loc="center left", bbox_to_anchor= (1,0.5))
ax.set_title('Top 400 Music Releases of all Time', color = 'white')
ax.set_xlabel('Release Date', color = 'white')
ax.set_ylabel('Rating (out of 5)', color = 'white')
ax.set_xlim([datetime.date(1955, 1, 1), datetime.date(2025,1,1)])
fig.set_facecolor('#181a1a')
ax.set_facecolor('#181a1a')
ax.spines['bottom'].set_color('#ffffff')
ax.spines['top'].set_color('#ffffff')
ax.spines['right'].set_color('#ffffff')
ax.spines['left'].set_color('#ffffff')
ax.tick_params(axis = 'x', colors = color)
ax.tick_params(axis = 'y', colors = color)
ax.set_aspect('auto')

fig.savefig('musicPlot.png', dpi = 500, bbox_inches = 'tight', pad_inches = 0.5)