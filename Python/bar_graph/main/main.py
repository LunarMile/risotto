# Imports
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# CSV Initialization
fatal = pd.read_csv('resources/fatal_encounters.csv', delimiter=',', low_memory=False)
segregation = pd.read_csv('resources/seg_per_city.csv', delimiter=';')


# Reverse the locations and dates
locations = list(fatal['Location of death (city)']) # .reverse() does not work!!


# Seperate top 10 highest/lowest segregation
segHead = segregation.head(10)
segTail = segregation.tail(10)

# [Detroit, ..., ...]
topCities = segHead['City']
# [640354, ..., ...]
topPopulations = segHead['Population']
# you know... v
topDeaths = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
topRatio = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]





# [Loreto, ..., ...]
botCities = segTail['City']
# [270554, ..., ...]
botPopulations = segTail['Population']
# same old... v
botDeaths = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
botRatio = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]





fig, axs = plt.subplots(2, 2)
fig.autofmt_xdate(rotation=45)

axs[0, 0].set_title('Fatal Encounters With Police in the Ten Most \n Racially Segregated Cities')
axs[0, 0].set_ylim([0, 500])
axs[0, 1].set_title('Fatal Encounters With Police in the Ten Least \n Racially Segregated Cities')
axs[0, 1].set_ylim([0, 500])
axs[1, 0].set_title('Fatal Encounters With Police in the Ten Most \n Racially Segregated Cities per 200k Inhabitants')
axs[1, 0].set_ylim([0, 150])
axs[1, 1].set_title('Fatal Encounters With Police in the Ten Least \n Racially Segregated Cities per 200k Inhabitants')
axs[1, 1].set_ylim([0, 150])
for ax in fig.get_axes():
    ax.label_outer()


def animate(i, topC, topD, topR, botC, botD, botR):

    # Initialize num deaths per city
    for location in locations[:i]:

        # Combines 'New York' and 'New York City' entries
        if location == 'New York City':
            location = 'New York'

        # Increments topDeath index of corresponding topCity
        if location in topC:
            index = topC.get(location)
            topD[index] += 1
            topR[index] += (1/topPopulations[index]) * 200000

        # Increments botDeath index of corresponding botCity
        if location in botC:
            index = botC.get(location)
            botD[index] += 1
            botR[index] += (1/botPopulations[index]) * 200000

    axs[0, 0].bar(topC, topD)
    axs[0, 1].bar(botC, botD)
    axs[1, 0].bar(topC, topR)
    axs[1, 1].bar(botC, botR)
    plt.show()



if __name__ == '__main__':
    ani = animation.FuncAnimation(fig, animate, fargs=(topCities, topDeaths, topRatio, botCities, botDeaths, botRatio), interval=20, frames=1000)



