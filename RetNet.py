import os
import glob
import pandas as pd

retnet_url = 'https://sph.uth.edu/retnet/disease.htm'
filtered_dir = 'C:/Users/Engineering/Documents/Rudzik/work/LOVD/Turro 2020/32581362_Turro-2020_SupTab2 (2).txt'
output_dir = 'C:/Users/Engineering/Documents/Rudzik/work/LOVD/Turro 2020/retnet_filtered'

retnet_dfs = pd.read_html(retnet_url, header=1)
retnet_df = pd.concat(retnet_dfs, ignore_index=True)

retnet_df['Gene'] = retnet_df['Symbols;OMIM Numbers'].str.extract('(^\w+)')
filtered_path = glob.glob(filtered_dir)

os.makedirs(output_dir, exist_ok=True)

for path in filtered_path:
    filtered_df = pd.read_csv(path, sep='\t')
    filename = os.path.basename(path)
    filename_without_extension = os.path.splitext(filename)[0]
    new_filename = filename_without_extension + '_retnet.csv'
    full_output_path = os.path.join(output_dir, new_filename)
    df = pd.merge(left=filtered_df, right=retnet_df, how='inner', on='Gene')
    df.to_csv(full_output_path)

