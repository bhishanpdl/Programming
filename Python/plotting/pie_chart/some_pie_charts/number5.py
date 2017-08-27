fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

angle = 180 + float(sum(small[::2])) / sum(reordered) * 360

pie_wedge_collection = ax.pie(reordered, colors=colors, labels=labels, labeldistance=1.05, startangle=angle);

for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')

ax.set_title("Figure 5");
