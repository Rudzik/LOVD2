import sys


def replace(text, replacement):
    new = ''

    for c in text:
        try:
            new += replacement[c]
        except KeyError:
            new += c

    return new


aa_code = {
    "A": "Ala", "C": "Cys", "D": "Asp", "E": "Glu", "F": "Phe",
    "G": "Gly", "H": "His", "I": "Ile", "K": "Lys", "L": "Leu",
    "M": "Met", "N": "Asn", "P": "Pro", "Q": "Gln", "R": "Arg",
    "S": "Ser", "T": "Thr", "V": "Val", "W": "Trp", "Y": "Tyr",
    "*": "Ter"
}

hgvs_p = -1

with open("C:/Users/Engineering/Documents/Rudzik/work/LOVD/Hosono_2018/annovar.csv") as csv:
    for line in csv:
        data = line.strip().split("\t")

        if hgvs_p == -1:
            hgvs_p = data.index("HGVS_P")
        else:
            aa = data[hgvs_p]
            data[hgvs_p] = replace(aa, aa_code)

        print("\t".join(data))