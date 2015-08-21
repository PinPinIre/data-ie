import sys
import os
import csv
import pandas as pd


def loadData(inputFile):
    return pd.read_csv(inputFile, index_col=0)


def main():
    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        loadData(sys.argv[1])
    else:
        print "Usage: scriptName.py in.tsv out.csv"

if __name__ == "__main__":
    main()
