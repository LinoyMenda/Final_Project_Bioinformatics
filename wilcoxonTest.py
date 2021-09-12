from scipy.stats import wilcoxon
import pandas as pd

f = open("wilcoxonResultsE2F1.txt", "w")
List = ["Breast.csv", "Colon.csv","Esophagus.csv","Liver.csv","Lung.csv","Ovary.csv","Pancreas.csv","Skin.csv","Stomach.csv","Testis.csv"]
print("E2F1:")
for i in List:
    df = pd.read_csv(i)
    new_df = df[['E2F1-h', 'E2F1-s']].dropna()
    wilcoxonResult = wilcoxon(new_df['E2F1-h'], new_df['E2F1-s'], correction=False)
    print(i+': '+str(wilcoxonResult))
    f.write(i+" E2F1: " + str(wilcoxonResult)+'\n')
f.close()

f1 = open("wilcoxonResultsE2F7.txt", "w")
List = ["Breast.csv", "Colon.csv","Esophagus.csv","Liver.csv","Lung.csv","Ovary.csv","Pancreas.csv","Skin.csv","Stomach.csv","Testis.csv"]
print("E2F7:")
for j in List:
    df = pd.read_csv(j)
    new_df = df[['E2F7-h', 'E2F7-s']].dropna()
    wilcoxonResult = wilcoxon(new_df['E2F7-h'], new_df['E2F7-s'], correction=False)
    print(j+': '+str(wilcoxonResult))
    f1.write(j+" E2F7: " + str(wilcoxonResult)+'\n')
f1.close()

f2 = open("wilcoxonResultsE2F8.txt", "w")
List = ["Breast.csv", "Colon.csv","Esophagus.csv","Liver.csv","Lung.csv","Ovary.csv","Pancreas.csv","Skin.csv","Stomach.csv","Testis.csv"]
print("E2F8:")
for h in List:
    df = pd.read_csv(h)
    new_df = df[['E2F8-h', 'E2F8-s']].dropna()
    wilcoxonResult = wilcoxon(new_df['E2F8-h'], new_df['E2F8-s'], correction=False)
    print(h+': '+str(wilcoxonResult))
    f2.write(h+" E2F8: " + str(wilcoxonResult)+'\n')
f2.close()