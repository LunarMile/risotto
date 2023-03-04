# Imports
import pandas as pd
import matplotlib.pyplot as plt

# CSV Initialization
fatal = pd.read_csv('resources/fatal_encounters.csv', delimiter=',', low_memory=False)
segregation = pd.read_csv('resources/seg_per_city.csv', delimiter=';')

# Reverse the locations and dates
locations = list(fatal['Location of death (city)'])  # .reverse() does not work!!
dates = list(fatal[' Date of injury resulting in death (month/day/year)'])
# Separate top 10 highest/lowest segregation
segHead = segregation.head(10)
segTail = segregation.tail(10)

# [Detroit, ..., ...]
topCities = list(segHead['City'])
# [640354, ..., ...]
topPopulations = list(segHead['Population'])

# [Loreto, ..., ...]
botCities = list(segTail['City'])
# [270554, ..., ...]
botPopulations = list(segTail['Population'])

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

axs[0, 1].set_title('Fatal Encounters With Police'
                    '\nin the Ten Least'
                    '\nRacially Segregated Cities')
axs[0, 1].set_ylim([0, 500])
axs[0, 1].set_facecolor('#ffffff')

axs[1, 0].set_title('per 200k Inhabitants')
axs[1, 0].set_ylim([0, 150])
axs[1, 0].set_facecolor('#ffffff')

axs[1, 1].set_title('per 200k Inhabitants')
axs[1, 1].set_ylim([0, 150])
axs[1, 1].set_facecolor('#ffffff')

for ax in fig.get_axes():
    ax.label_outer()


# Animation loop
def animate(i, topC, botC):
    topD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # | | | |
    topR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # same old... v
    botD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # | | | |
    botR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Initialize num deaths per city
    for location in locations[i:]:

        # Combines 'New York' and 'New York City' entries
        if location == 'New York City':
            location = 'New York'

        # Increments topDeath index of corresponding topCity
        if location in topC:
            index = topC.index(location)
            topD[index] += 1
            topR[index] += (1/topPopulations[index]) * 200000

        # Increments botDeath index of corresponding botCity
        if location in botC:
            index = botC.index(location)
            botD[index] += 1
            botR[index] += (1/botPopulations[index]) * 200000

    # Plot the bars
    axs[0, 0].bar(topC, topD, color='#7dcff4')
    axs[0, 1].bar(botC, botD, color='#d2b9c3')
    axs[1, 0].bar(topC, topR, color='#224d62')
    axs[1, 1].bar(botC, botR, color='#8c747c')

    # add overall title and adjust it so that it doesn't overlap with subplot titles
    fig.suptitle(dates[i])
    fig.savefig('./pics/{}.png'.format(str(str(dates[i]).split('/'))), bbox_inches='tight')


# Main method, goes over locations backwards and only creates a frame when the days are complete <3
if __name__ == '__main__':
    prevDate = ""
    i = len(locations) - 1

    while i > 0:
        date = dates[i]

        if date == prevDate:
            i -= 1

        else:
            animate(i, topCities, botCities)
            prevDate = date
            i -= 1
