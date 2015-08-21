import sys
import os
import csv


def tsvToCsv(inputFile, outputFile):
    csv.field_size_limit(sys.maxsize)
    csvReader = csv.reader(open(inputFile), delimiter="\t")
    csv.writer(file(outputFile, 'w+')).writerows(csvReader)


def main():
    if len(sys.argv) > 2 and os.path.isfile(sys.argv[1]):
        tsvToCsv(sys.argv[1], sys.argv[2])
    else:
        print "Usage: tsvToCsv in.tsv out.csv"

if __name__ == "__main__":
    main()
