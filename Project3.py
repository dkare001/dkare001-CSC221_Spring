import matplotlib.pyplot as plt
import seaborn as sns

def plot_cubic_numbers_with_colormap():
    x = list(range(1, 5001))
    y = [i**3 for i in x]

    sns.set(style='darkgrid')
    plt.scatter(x, y, c=y, cmap='viridis')
    plt.colorbar(label='Cubic Value')
    plt.title("Cubic Numbers with Colormap")
    plt.xlabel("Number")
    plt.ylabel("Cubic Value")
    plt.show()

plot_cubic_numbers_with_colormap()

def plot_first_five_cubic_numbers():
    x = [1, 2, 3, 4, 5]
    y = [i**3 for i in x]

    sns.set(style='darkgrid')
    plt.plot(x, y, marker='o')
    plt.title("First Five Cubic Numbers")
    plt.xlabel("Number")
    plt.ylabel("Cubic Value")
    plt.show()

def plot_first_five_thousand_cubic_numbers():
    x = list(range(1, 5001))
    y = [i**3 for i in x]

    sns.set(style='darkgrid')
    plt.plot(x, y)
    plt.title("First Five Thousand Cubic Numbers")
    plt.xlabel("Number")
    plt.ylabel("Cubic Value")
    plt.show()

plot_first_five_cubic_numbers()
plot_first_five_thousand_cubic_numbers()
