import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

url ='https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
request = requests.get(url)


'''

Running the preceding commands establishes a connection with the given website and
reads the HTML code of the page. Everything we see on a website (text, images, layouts,
links to other web pages, and so on) can be found in the HTML code of the page. Using the
.text function of request, we can output the entire HTML script of the web page, as
shown here:

'''

print(request.text)

'''

Another detailed webscarping type


'''
titles = []
prices = []
ratings = []
url ='https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
for product in soup.find_all('div', {'class': 'col-sm-4 col-lg-4 colmd-4'}):

   for pr in product.find_all('div', {'class': 'caption'}):
       titles.append(pr)

       for p in pr.find_all('h4', {'class': 'pull-right price'}):

           prices.append(p.text)

       for title in pr.find_all('a', {'title'}):

           titles.append(title.get('title'))

       for rt in product.find_all('div', {'class': 'ratings'}):
           ratings.append(len(rt.find_all('span',
                                          {'class': 'glyphicon glyphicon-star'})))

product_df = pd.DataFrame(zip(titles,prices,ratings), columns = \
['Titles','Prices', 'Ratings'])
product_df.to_csv("ecommerce.csv",index=False)


