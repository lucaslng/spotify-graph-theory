from dotenv import load_dotenv
from scraper import scrape
from os import getenv

def main():
	load_dotenv()
	scrape(*map(lambda x: str(getenv(x)), ('USERNAME', 'PWD', 'TARGETID')))

if __name__ == "__main__":
	main()