import requests
from bs4 import BeautifulSoup
import os
"""
Welcome! 

This is a scrapper that writes whatever you need into a new .txt file. 
I hope the comments should help you with the process of this automated python file
-Andrew Stevenson
"""

class Scrap():
    def __init__(self, url, file_name, element, h_class):
      
        self.url = url # URL of your chose
        self.file_name = file_name # What the file will be called when you run (make sure you add .txt or what you want)
        self.element = element # What HTML element you are looking for
        self.h_class = h_class # The class of that same html element
        #IMPORTANT: please only change the variables at the bottom of the page, there will be a marker
        pass

    def scrapProcces(self):
        url = self.url
        element = self.element
        h_class = self.h_class
        file_name = self.file_name
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

        try:
            #getting the responce and also setting headers and timeouts (10 seconds)
            response = requests.get(url, headers=headers, timeout=10)
            

            if response.status_code == 200:
                print("All Good, Working the Magic 😃")

                
                information = BeautifulSoup(response.text, "html.parser")

                web_scrapped = information.find_all(element, class_=h_class)
                total_info = len(web_scrapped)
                with open (file_name, 'w') as file:
                    for info in web_scrapped:
                        file.write(info.get_text())
                        # print(info.text.strip())
                        # converted = str(info)
                        # os.write("info.txt", converted)

                print(total_info)

            


        except ValueError as v:
            print(f"Value Error {v}")
        except TimeoutError as t:
            print(f"Time Out Error {t}")

    
        
    


my_url = "https://www.asus.com/us/laptops/for-creators/all-series/"
start = Scrap(url=my_url, element="div", h_class="seriesRightBody LevelTwoSeriesPage__seriesRightBody__2DRzz", file_name="new_data.txt") #THIS IS WHERE YOU CHANGE THE VARS
start.scrapProcces()
