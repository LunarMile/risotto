import pandas as pd
import matplotlib as plt
import seaborn as sns

if __name__ == '__main__':

    fatal = pd.read_csv('resources/fatal_encounters.csv', delimiter=',')
    segregation = pd.read_csv('resources/seg_per_city.csv', delimiter=',')

    print(fatal.head())
    print(segregation.head())



