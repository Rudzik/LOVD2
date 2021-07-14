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
data = io.StringIO(txt1) #this tells me it is an IO object
txt2 = pd.read_csv(data, sep="\t", header=0) #this reads the data into CSV
txt2.to_csv('C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt', index=False, sep='\t', float_format='%d', mode='a') #this outputs the data into tab delimited text
df1 = df.iloc[:, 0:19]
df1 = df1.dropna(subset=['{{panel_size}}'])
df1.drop_duplicates(subset=['{{id}}'])
df1 = df1.to_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt", index=False, sep='\t', float_format='%d', mode='a')
txt3 = '''## Individuals_To_Diseases ## Do not remove or alter this header ##'''
df2_header = io.StringIO(txt3)
txt3 = pd.read_csv(df2_header, sep="\t")
txt3 = txt3.to_csv('C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt', index=False, sep='\t', float_format='%d', mode='a')
txt31 = '''{{individualid}}\t{{diseaseid}}'''
df2_header2 = io.StringIO(txt31)
txt31 = pd.read_csv(df2_header2, sep="\t")
txt31 = txt31.to_csv('C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt', index=False, sep='\t', float_format='%d', mode='a')
df2 = df.iloc[:, 19:21] ## Individuals_To_Diseases ##
df2 = df2.dropna()
df2 = df2.drop_duplicates(subset=['{{individualid}}'])
df2.to_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt", header=0, index=False, sep='\t', float_format='%d', mode='a')
txt4 = '''## Phenotypes ## Do not remove or alter this header ##'''
df3_header = io.StringIO(txt4)
txt4 = pd.read_csv(df3_header, sep="\t")
txt4 = txt4.to_csv('C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt', index=False, sep='\t', float_format='%d', mode='a')
df3 = df.iloc[:, 19:34] ## Phenotypes ## Do not remove or alter this header ##
df3 = df3.dropna(subset=['{{individualid}}'])
df3.columns = df3.columns.str.replace(r"(\.)(\d)", '', regex=True)
df3.to_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt", index=False, sep='\t', float_format='%d', mode='a')
txt5 = '''## Screenings ## Do not remove or alter this header ##'''
df4_header = io.StringIO(txt5)
txt5 = pd.read_csv(df4_header, sep="\t")
txt5 = txt5.to_csv('C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt', index=False, sep='\t', float_format='%d', mode='a')
df4 = df.iloc[:, 34:43] ## Screenings ## Do not remove or alter this header ##
df4.columns = df4.columns.str.replace(r"(\.)(\d)", '', regex=True)
df4 = df4.dropna(subset=['{{individualid}}'])
df4.to_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt", index=False, sep='\t', float_format='%d', mode='a')
txt6 = '''## Screenings_To_Genes ## Do not remove or alter this header ##'''
df5_header = io.StringIO(txt6)
txt6 = pd.read_csv(df5_header, sep="\t")
txt6 = txt6.to_csv('C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt', index=False, sep='\t', float_format='%d', mode='a')
df5 = df.iloc[:, 43:45] ## Screenings_To_Genes ## Do not remove or alter this header ##
df5 = df5.dropna(subset=['{{screeningid}}'])
df5.to_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt", index=False, sep='\t', float_format='%d', mode='a')
txt7 = '''## Variants_On_Genome ## Do not remove or alter this header ##'''
df6_header = io.StringIO(txt7)
txt7 = pd.read_csv(df6_header, sep="\t")
txt7 = txt7.to_csv('C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt', index=False, sep='\t', float_format='%d', mode='a')

df6 = df.iloc[:, 53:76]## Variants_On_Genome ## Do not remove or alter this header ##
df6.columns = df6.columns.str.replace(r"(\.)(\d)", '', regex=True)
df6 = df6.dropna(subset=['{{id}}'])
df6.to_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt", index=False, sep='\t', float_format='%d', mode='a')

txt8 = '''## Variants_On_Transcripts ## Do not remove or alter this header ##'''
df7_header = io.StringIO(txt8)
txt8 = pd.read_csv(df7_header, sep="\t")
txt8 = txt8.to_csv('C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt', index=False, sep='\t', float_format='%d', mode='a')

df7 = df.iloc[:, 46:53] ## Variants_On_Transcripts ## Do not remove or alter this header ##
df7.columns = df7.columns.str.replace(r"(\.)(\d)", '', regex=True)
df7.to_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt", index=False, sep='\t', float_format='%d', mode='a')
txt9 = '''## Screenings_To_Variants ## Do not remove or alter this header ##\r\n'''
df8_header = io.StringIO(txt9)
txt9 = pd.read_csv(df8_header, sep="\t")
txt9 = txt9.to_csv('C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt', index=False, sep='\t', float_format='%d', mode='a')
txt10 = '''{{screeningid}}\t{{variantid}}'''
df8_header2 = io.StringIO(txt10)
txt10 = pd.read_csv(df8_header2, sep="\t")
txt10 = txt10.to_csv('C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt', index=False, sep='\t', float_format='%d', mode='a')
df8 = df.iloc[:, 45:47] ## Screenings_To_Variants ## Do not remove or alter this header ##
df8.columns = df8.columns.str.replace(r"(\.)(\d)", '', regex=True)
df8.to_csv("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Tracewska 2019/output.txt", header=0, index=False, sep='\t', float_format='%d', mode='a')