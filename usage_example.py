

progressive_plot = ProgressivePlot()

# Надо задать функцию и сетку узлов

def f(x):
    return x  # some function


M = EquidistantNodesSet1d(start, end, step)

progressive_plot.start(f, M)