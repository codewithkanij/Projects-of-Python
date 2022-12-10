#   using a library called 'matplotlib' to draw  chart or graph

"""
# --------------------------------------- for one straightline----------------------------------------------------


import matplotlib.pyplot as plt

x = [2, 8, 16]
y = [2, 3, 6]

plt.plot(x, y)              # plotted this line


plt.xlabel('X Axis')        # to show that in the direction of the x-axis

plt.ylabel('Y Axis')        # # to show that in the direction of the y-axis

plt.title('Demo Graph')     # to show this title top of the graph


plt.show()                  # this graph will be shown by a pop-up

print("Run successfully. ")  # when we closed that pop-up, this line will be printed on console


"""

"""


#  ------------------------------for two different lines on one graph---------------------------------------------------


import matplotlib.pyplot as plt

x1 = [2, 4, 5, 6]
y1 = [2, 3, 6, 7]

plt.plot(x1, y1, label = 'Line 1')   # plotted 1st line

x2 = [2, 8, 16]
y2 = [2, 3, 6]

plt.plot(x2, y2, label = 'Line 2')  # plotted 2nd line


plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Two Lines ')

plt.legend()             # it will be show/indicate what color of each of the line


plt.show()

print("Run successfully. ")

"""

"""

#  ---------------------------------------customized graph-------------------------------------------------------


import matplotlib.pyplot as plt

x = [2, 4, 5, 6]
y = [2, 3, 6, 7]

plt.plot(x, y, color = 'green', linestyle = 'dashed', linewidth = 3, marker = 'o', markerfacecolor = 'blue', markersize = 12)

plt.xlim(1,8)
plt.ylim(1,8)


plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Customization ')


plt.show()

print("Run successfully. ")


"""


# -------------------------------create a bar chart in python-------------------------------------------------------


import matplotlib.pyplot as plt

left = [1, 2, 3, 4, 5, 7]
height = [10, 11, 23, 36, 4, 5]                                 # height of each bar

tick_label = ['one', 'two', 'three','four','five', 'six']       # name to each bar

plt.bar(left, height, tick_label=tick_label, width=0.8, color=['blue', 'orange'])    # plotting the bar


plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Bar Chart ')


plt.show()

print("Run successfully. ")

