import matplotlib.pyplot as pt
from matplotlib.axes import Axes


def add_graph(x_values, y_values, title, x_label, y_label, axes: Axes):
    pt.figure()
    axes.set_title(title)
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
    axes.plot(x_values, y_values, linewidth=0.7)
    axes.grid()