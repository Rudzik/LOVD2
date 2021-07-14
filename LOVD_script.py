import pandas as pd
import re
import io


pd.options.display.float_format = '{:.0f}'.format
df = pd.read_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/Tracewska_2019.txt", sep='\t', skiprows=0, header=1, low_memory=False)
with open("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/FFBupload_empty.txt") as fh:
    txt = fh.read()
# this piece of code is to avoid closing the file manually! Normally it would look like this:
# fh = open("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/FFBupload_empty.txt")
# txt = fh.read()
# fh.close()
txt1 = '''### LOVD-version 3000-060 ### Full data download ### To import, do not remove or alter this header ### \r\n 
## Genes ## Do not remove or alter this header ## \r\n 
## Transcripts ## Do not remove or alter this header ## \r\n
## Diseases ## Do not remove or alter this header ##\r\n 
## Genes_To_Diseases ## Do not remove or alter this header ##\r\n
## Individuals ## Do not remove or alter this header ##'''

data = io.StringIO(txt1)
txt2 = pd.read_csv(data, sep="\t", header=0)
txt2.to_csv('output.txt', index=False, sep='\t', float_format='%d', header=None, mode='a')

print(txt2)
# txt2 = df1.to_csv(txt2, index=False, sep='\t', float_format='%d', header=None, mode='a')
# print(txt2)

df1 = df.iloc[:, 0:19]
df1 = df1.dropna(subset=['{{panel_size}}'])
df1.drop_duplicates(subset=['{{id}}'])
df1 = df1.to_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt", index=False, sep='\t', float_format='%d', header=None, mode='a')
print(df1)

df2 = df.iloc[:, 19:21]
df2 = df2.dropna()
df2 = df2.drop_duplicates(subset=['{{individualid}}'])


df2.to_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt", sep='\t', float_format='%d', index=False, mode='a')

# df1 = re.sub('  +', '\t', df1)

# df2 = df.iloc[:, 19:21]
# df2 = df2.dropna()
# df2 = df2.drop_duplicates(subset=['{{individualid}}'])
# df2 = df2.to_string(float_format=None, index=False)
# df2 = df2.replace('NaN','')
# df2 = re.sub('  +', '\t', df1)
#
# df3 = df.iloc[:, 19:34]
# df3 = df3.dropna(subset=['{{individualid}}'])
# df3.columns = df3.columns.str.replace(r"(\.)(\d)", '', regex=True)
# df3 = df3.to_string(float_format=None, index=False)
# df3 = df1.replace('NaN','')
# df3 = re.sub('  +', '\t', df1)
# df4 = df.iloc[:, 34:43]
# df4.columns = df4.columns.str.replace(r"(\.)(\d)", '', regex=True)
# df4 = df4.dropna(subset=['{{id}}'])
# df4 = df4.to_string(float_format=None, index=False)
# df4 = df4.replace('NaN','')
# df4 = re.sub('  +', '\t', df1)
# df5 = df.iloc[:, 43:45]
# df5 = df5.dropna(subset=['{{screeningid}}'])
# df5 = df5.to_string(float_format=None, index=False)
# df5 = df5.replace('NaN','')
# df5 = re.sub('  +', '\t', df1)
# df6 = df.iloc[:, 53:76]
# df6.columns = df6.columns.str.replace(r"(\.)(\d)", '', regex=True)
# df6 = df6.to_string(float_format=None, index=False)
# df6 = df6.replace('NaN','')
# df6 = re.sub('  +', '\t', df1)
# df7 = df.iloc[:, 46:53]
# df7.columns = df7.columns.str.replace(r"(\.)(\d)", '', regex=True)
# df7 = df7.to_string(float_format=None, index=False)
# df7 = df7.replace('NaN','')
# df7 = re.sub('  +', '\t', df1)
# df8 = df.iloc[:, 45:47]
# df8.rename(columns={'{{id}}.3': '{{variantid}}'}, inplace=True)
# df8 = df8.to_string(float_format=None, index=False)
# df8 = df8.replace('NaN','')
# # df8 = re.sub('  +', '\t', df1)
# txt = txt.replace('!!! Replace by Copy/Paste columns A to S go under (starting row 2)!!!', df1)
# # txt = txt.replace('{{individualid}}	{{diseaseid}}', '')
# # txt = txt.replace('!!! Replace by Copy/Paste columns T to U go under (starting row 3, so excl. headers)!!!', df2)
# # txt = txt.replace('!!! Replace by Copy/Paste columns T to AH go under (starting row 2)!!!', df3)
# # txt = txt.replace('!!! Replace by Copy/Paste columns AI to AQ go under (starting row 2)!!!', df4)
# # txt = txt.replace('!!! Replace by Copy/Paste columns AR to AS go under (starting row 2)!!!', df5)
# # txt = txt.replace('!!! Replace by Copy/Paste columns BB to BX go under (starting row 2)!!!', df6)
# # txt = txt.replace('!!! Replace by Copy/Paste columns AU to BA go under (starting row 2)!!!', df7)
# # txt = txt.replace('{{screeningid}}	{{variantid}}', '')
# # txt = txt.replace('!!! Replace by Copy/Paste columns AT to AU go under (starting row 3, so excl. headers)!!!', df8)
# f = open('C:/Users/atrac/Documents/work/LOVD/Tracewska 2019/result.txt', 'w')
# f.write(txt)
# f.close()