import matplotlib.pyplot as plt

from util import sort_by_mean, sort_by_median

# y_limits = (-500, 500)

x_label = "Team Number"
y_label = "Score"

scouting_data = {1458: [12, 34, 13, 123, 432],
                 1234: [123, 32, 12, 54, 32],
                 132: [12, 64, 23, 75, 23],
                 1758: [12, 34, 13, 123, 432]}

sorted_data = sort_by_median(scouting_data, 4, True)  # sort_by_mean() can also be used

data_list = []
x_tick_list = []
x_axis_list = []

for number, label in enumerate(sorted_data):
    data = sorted_data[label]
    x_tick_list.append(str(label))
    x_axis_list.append(number + 1)
    data_list.append(data)

plt.figure()
plt.boxplot(data_list)

# plt.ylim(y_limits)

plt.xticks(x_axis_list, x_tick_list)
plt.ylabel(y_label)
plt.xlabel(x_label)

plt.show()
