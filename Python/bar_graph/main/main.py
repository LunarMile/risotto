# type: ignore [reportUnknownMemberType]
# Imports
import pandas as pd
import matplotlib.pyplot as plt

# CSV Initialization
fatal = pd.read_csv('resources/fatal_encounters.csv', delimiter=',', low_memory=False)
segregation = pd.read_csv('resources/seg_per_city.csv', delimiter=';')

# Get the locations and dates
locations = list(fatal['Location of death (city)'])
dates = list(fatal[' Date of injury resulting in death (month/day/year)'])

# Separate top 10 highest/lowest segregation
segHead = segregation.head(10)
segTail = segregation.tail(10)

# [Detroit, ..., ...]
topCities = list(segHead['City'])
# [640354, ..., ...]
topPopulations = list(segHead['Population'])
# same old... v
topDeaths = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# | | | |
topRatio = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# [Loreto, ..., ...]
botCities = list(segTail['City'])
# [270554, ..., ...]
botPopulations = list(segTail['Population'])
# same old... v
botDeaths = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# | | | |
botRatio = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Figure adjustments, formatting basically
fig, axs = plt.subplots(2, 2)
fig.autofmt_xdate(rotation=45)
fig.tight_layout(h_pad=2)
fig.patch.set_facecolor('#e7e7e7')
plt.subplots_adjust(top=.80)


axs[0, 0].set_title('Fatal Encounters With Police'
                    '\nin the Ten Most'
                    '\nRacially Segregated Cities')
axs[0, 0].set_ylim([0, 500])
axs[0, 0].set_facecolor('#ffffff')
rects1 = axs[0, 0].bar(topCities, topDeaths, color='#7dcff4')

axs[0, 1].set_title('Fatal Encounters With Police'
                    '\nin the Ten Least'
                    '\nRacially Segregated Cities')
axs[0, 1].set_ylim([0, 500])
axs[0, 1].set_facecolor('#ffffff')
rects2 = axs[0, 1].bar(botCities, botDeaths, color='#d2b9c3')

axs[1, 0].set_title('per 200k Inhabitants')
axs[1, 0].set_ylim([0, 150])
axs[1, 0].set_facecolor('#ffffff')
rects3 = axs[1, 0].bar(topCities, topRatio, color='#224d62')

axs[1, 1].set_title('per 200k Inhabitants')
axs[1, 1].set_ylim([0, 150])
axs[1, 1].set_facecolor('#ffffff')
rects4 = axs[1, 1].bar(botCities, botRatio, color='#8c747c')

for ax in fig.get_axes():
    ax.label_outer()


# Animation loop
def animate(i):
    # Combines 'New York' and 'New York City' entries
    if locations[i] == 'New York':
        locations[i] = 'New York City'

    # Increments topDeath index of corresponding topCity
    if locations[i] in topCities:
        index = topCities.index(locations[i])
        topDeaths[index] = topDeaths[index] + 1
        topRatio[index] = topRatio[index] + (1 / topPopulations[index]) * 200000

    # Increments botDeath index of corresponding botCity
    if locations[i] in botCities:
        index = botCities.index(locations[i])
        botDeaths[index] = botDeaths[index] + 1
        botRatio[index] = botRatio[index] + (1 / botPopulations[index]) * 200000

    for index in range(10):
        rects1[index].set_height(topDeaths[index])
        rects2[index].set_height(botDeaths[index])
        rects3[index].set_height(topRatio[index])
        rects4[index].set_height(botRatio[index])

    # Add overall title and adjust it so that it doesn't overlap with subplot titles
    fig.suptitle(dates[i])
    fig.savefig('./pics/{}.png'.format(str(dates[i]).replace("/", "_")), bbox_inches='tight')
    print(str(dates[i]).replace("/", "_"))


# Does not save figure
def draw(i):

    # Combines 'New York' and 'New York City' entries
    if locations[i] == 'New York City':
        locations[i] = 'New York'

    # Increments topDeath index of corresponding topCity
    if locations[i] in topCities:
        index = topCities.index(locations[i])
        topDeaths[index] = topDeaths[index] + 1
        topRatio[index] = topRatio[index] + (1/topPopulations[index]) * 200000

    # Increments botDeath index of corresponding botCity
    if locations[i] in botCities:
        index = botCities.index(locations[i])
        botDeaths[index] = botDeaths[index] + 1
        botRatio[index] = botRatio[index] + (1/topPopulations[index]) * 200000


# Main method, goes over locations backwards and only creates a frame when the days are complete <3
def main():
    prevDate = ""
    i = len(locations) - 1

    while i > 0:
        date = dates[i]
        print(topDeaths)
        print(topRatio)

        if date == prevDate:
            draw(i)
            i -= 1

        else:
            animate(i)
            prevDate = date
            i -= 1


if __name__ == '__main__':
    main()
