import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
# Create 50 random points in the US
n_points = 50
lat = np.random.uniform(24, 50, n_points)
lon = np.random.uniform(-126, -67, n_points)
values = np.random.uniform(0, 10, n_points)

lat_grid, lon_grid = np.meshgrid(np.linspace(24, 50, 100), np.linspace(-126, -67, 100))


power = 2
distance_cutoff = 1000
distances = cdist(np.c_[lat, lon], np.c_[lat_grid.ravel(), lon_grid.ravel()], 'euclidean')
weights = 1 / (distances + 1e-6) ** power
weights[distances > distance_cutoff] = 0

interpolated_values = np.sum(values * weights, axis=0) / np.sum(weights, axis=0)
interpolated_values = np.reshape(interpolated_values, lat_grid.shape)



fig = plt.figure(figsize=(10, 8))
m = Basemap(llcrnrlon=-126, llcrnrlat=24, urcrnrlon=-67, urcrnrlat=50,
            projection='lcc', lat_1=33, lat_2=45, lon_0=-95

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
