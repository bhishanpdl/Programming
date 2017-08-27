large = slices[:len(slices) / 2]
small = slices[len(slices) / 2:]

reordered = large[::2] + small[::2] + large[1::2] + small[1::2]

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

pie_wedge_collection = ax.pie(reordered, colors=colors, labels=labels, labeldistance=1.05);

for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')

ax.set_title("Figure 4");
