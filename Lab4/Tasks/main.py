from utils import *

def main():
    filePath = "Book/The Metamorphosis.txt"

    genRanSentence(*listOfWords()) # 1
    amountOfSymbols(filePath) # 2.1
    amountOfWords(filePath) # 2.2
    findRepSeq(filePath) # 3

if __name__ == "__main__":
    main()