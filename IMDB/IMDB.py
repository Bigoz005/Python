import csv
#pliki wypakowaz 7zip do tego samego folderu co skrypt
with open("dataname.tsv", encoding="utf8") as fd1:
    rd1 = csv.reader(fd1, delimiter="\t", quotechar='"')
    for row1 in rd1:
        print(row1)

with open("datatitle.tsv", encoding="utf8") as fd2:
    rd2 = csv.reader(fd2, delimiter="\t", quotechar='"')
    for row2 in rd2:
        print(row2)
