from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/search?sid=b5g&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DHP&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.brand%255B%255D%3DLenovo")

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('div', attrs={'class':'_75nlfW'}):
    name = a.find('a', attrs={'class':'wjcEIp'})
    price = a.find('div', attrs={'class':'Nx9bqj'})
    rating = a.find('div', attrs={'class':'XQDdHH'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name':products, 'Price':prices, 'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')

driver.close()
