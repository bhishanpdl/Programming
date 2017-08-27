from random import shuffle

slices = [1,2,3] * 4 + [20, 25, 30] * 2
shuffle(slices)

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

cmap = plt.cm.prism
colors = cmap(np.linspace(0., 1., len(slices)))

labels = ["Some text"] * len(slices)

ax.pie(slices, colors=colors, labels=labels, labeldistance=1.05)
ax.set_title("Figure 1");
