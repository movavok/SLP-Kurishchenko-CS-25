from classDataParser import DataParser
from interface import loop
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    token = os.getenv("GITHUB_TOKEN")
    parser = DataParser(token)
    loop(parser)

if __name__ == "__main__":
    main()