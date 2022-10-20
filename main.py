import requests
from bs4 import BeautifulSoup
import pycron
import time
from functions import urls, checkingName, sendMessage
import logging



logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s :- %(message)s', datefmt='%m-%d-%Y %I:%M:%S')

file_handel = logging.FileHandler("error.log", mode='w')
file_handel.setFormatter(formatter)

stream_handle = logging.StreamHandler()
stream_handle.setFormatter(formatter)

logger.addHandler(file_handel)
logger.addHandler(stream_handle)



def main():

    try:
        url = urls
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        comics_name = soup.find_all("h3", class_="entry-title")
        with open('names.txt', 'w') as f:
            for x in comics_name:
                f.write(x.text + "\n")


        if checkingName("Gohan"):
            sendMessage("Gohan")
        else:
            logger.exception("not present")
    except Exception as e:
      logger.exception(e)
    


if __name__ == "__main__":
    if pycron.is_now('13 13 * * *'):   # True every day at 13:13
        main()
   