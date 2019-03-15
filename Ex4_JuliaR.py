#438745-FS2019-0: Geodata analysis and modelling
#Julia Ryser, 12.03.2019

#Exercise 4

#The package numpy needs to be installed (and imported)

import numpy

#function extracts the precipitation data from the file
def read_pre_list(data):
    pre_data_arrow = numpy.loadtxt(data, skiprows=1, usecols=[2])
    return pre_data_arrow

#Main skript calls the function and displays some data
path = r"C:\Users\Julia\PycharmProjects\Exercise3\precip_data.txt"
pre_data = read_pre_list(path)

min_pre = pre_data.min()
max_pre = pre_data.max()
mean_pre = round(pre_data.mean(), 2)

print("minimal precipitation value: {}\nmaximal precipitation value: {}\nmean precipitation value: {}".format(min_pre, max_pre, mean_pre))

#this is a comment to try GitKraken
