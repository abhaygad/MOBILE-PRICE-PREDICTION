from bs4 import BeautifulSoup as Soup
import pandas as pd

data = pd.read_csv('DATA/DATA-PHONE.csv')

x=data["NAME"]
for i in x:

    soup = Soup('phone_source/'+str(x)+'.html')

    title = soup.find('meta')
    meta = soup.new_tag('link')
    meta['rel'] = "stylesheet"
    meta['href'] = "DATA/styles_new_add.css"
    title.insert_after(meta)

    print (soup)