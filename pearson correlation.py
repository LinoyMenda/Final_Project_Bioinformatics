import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats


List = ["Breast.csv", "Colon.csv","Esophagus.csv","Liver.csv","Lung.csv","Ovary.csv","Pancreas.csv","Skin.csv","Stomach.csv","Testis.csv"]
for i in List:
    df = pd.read_csv(i)
    list1 = df["E2F7-h"].dropna().tolist()
    list2 = df["E2F8-h"].dropna().tolist()
    x_simple = np.array(list1)
    y_simple = np.array(list2)
    #calculates pearson correlation
    print(scipy.stats.pearsonr(x_simple, y_simple))
    #creating the plot
    slope, intercept, r, p, stderr = scipy.stats.linregress(x_simple, y_simple)
    line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
    fig, ax = plt.subplots()
    ax.plot(x_simple, y_simple, linewidth=0, marker='s', label='Data points')
    ax.plot(x_simple, intercept + slope * x_simple, label=line)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.title(i)
    ax.legend(facecolor='white')
    plt.show()

