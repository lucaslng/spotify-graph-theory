from dotenv import load_dotenv
from scrape_all import scrape_all
from os import getenv

def main():
	load_dotenv()
	token = getenv('TOKEN')
	if token is None:
		print("Please put TOKEN in .env!")
		return
	targetid = getenv('TARGETID')
	if targetid is None:
		print("Please put TARGETID in .env!")
		return
	
	scrape_all(token, targetid, 2)

if __name__ == "__main__":
	main()