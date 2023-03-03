import pandas as pd
import matplotlib.pyplot as plt

fatal = pd.read_csv('resources/fatal_encounters.csv', delimiter=',', low_memory=False)
segregation = pd.read_csv('resources/seg_per_city.csv', delimiter=';')

segHead = segregation.head(10)
segTail = segregation.tail(10)

topDeaths = []
topPopulations = []
topRatio = []
bottomDeaths = []
bottomPopulations = []
bottomRatio = []

topTen = {}
bottomTen = {}


for city, population in zip(segHead['City'], segHead['Population']):
    topTen[city] = [population, 0]

for city, population in zip(segTail['City'], segTail['Population']):
    bottomTen[city] = [population, 0]


for location in fatal['Location of death (city)']:

    if location == 'New York City':
        location = 'New York'

    for key in topTen:
        if location == key:
            topTen.get(key)[1] += 1

    for key in bottomTen:
        if location == key:
            bottomTen.get(key)[1] += 1


for key in topTen.keys():
    topPopulations.append(topTen.get(key)[0])
    topDeaths.append(topTen.get(key)[1])
    topRatio.append((topTen.get(key)[1]/topTen.get(key)[0]) * 200000)

for key in bottomTen.keys():
    bottomPopulations.append(bottomTen.get(key)[0])
    bottomDeaths.append(bottomTen.get(key)[1])
    bottomRatio.append((bottomTen.get(key)[1]/bottomTen.get(key)[0]) * 200000)


fig, axs = plt.subplots(2, 2)
fig.autofmt_xdate(rotation=45)

axs[0, 0].bar(topTen.keys(), topDeaths)
axs[0, 0].set_title('Fatal Encounters With Police in the Ten Most \n Racially Segregated Cities')
axs[0, 0].set_ylim([0, 500])

axs[0, 1].bar(bottomTen.keys(), bottomDeaths)
axs[0, 1].set_title('Fatal Encounters With Police in the Ten Least \n Racially Segregated Cities')
axs[0, 1].set_ylim([0, 500])

axs[1, 0].bar(topTen.keys(), topRatio)
axs[1, 0].set_title('Fatal Encounters With Police in the Ten Most \n Racially Segregated Cities per 200k Inhabitants')
axs[1, 0].set_ylim([0, 150])

axs[1, 1].bar(bottomTen.keys(), bottomRatio)
axs[1, 1].set_title('Fatal Encounters With Police in the Ten Least \n Racially Segregated Cities per 200k Inhabitants')
axs[1, 1].set_ylim([0, 150])


for ax in fig.get_axes():
    ax.label_outer()


if __name__ == '__main__':
    plt.show()
    print(topTen)
    print(bottomTen)




