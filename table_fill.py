import pandas as pd

pd.options.display.float_format = '{:.0f}'.format



df = pd.read_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Surl 2020/table.txt", sep='\t', header=0, low_memory=False)

df = df.ffill(axis=0)


df.to_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Surl 2020/table_output.txt", header=0, index=False, sep='\t', float_format='%d')