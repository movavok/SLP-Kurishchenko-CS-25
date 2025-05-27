from classDataParser import DataParser
from interface import draw_social_graph
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    token = os.getenv("GITHUB_TOKEN")

    parser = DataParser(token)
    network = parser.fetch_user_and_friends("movavok")

    draw_social_graph(network)

if __name__ == "__main__":
    main()