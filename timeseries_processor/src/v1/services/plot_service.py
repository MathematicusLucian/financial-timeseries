import matplotlib.pyplot as mplt

def create__plot_space(data):
    return data.plot(grid=True)

def create__plot(data):
    plot = create__plot_space(data)
    return plot
