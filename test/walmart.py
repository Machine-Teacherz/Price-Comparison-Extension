from bs4 import BeautifulSoup
import requests,lxml
import json
import csv



def walmart(product):
    url = f'https://www.walmart.com/search/?query={product}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
     

    # to get the item name
 
    title = soup.find_all('a',class_ = 'product-title-link line-clamp line-clamp-2 truncate-title')
    all_title = [item.text for item in title]
    
    # to get the item price   
    price = soup.find_all('span',class_ = 'price-characteristic')
    all_price = [f'${item.text}' for item in price]
    # print(all_price)  


    # to get the url for each product
    links = soup.find_all('a',class_ = 'product-title-link line-clamp line-clamp-2 truncate-title')
    all_links = [f"https://www.walmart.com/{item.get('href')}" for item in links]
    print(all_links)
        
    # to get the item ratings 

    rating = soup.find_all('span',class_ = 'visuallyhidden seo-avg-rating')
    all_rating = [item.text for item in rating]
    # print(all_rating)

    # to get the item reviews
    reviews = soup.find_all('span',class_ = 'seo-review-count visuallyhidden')
    all_reviews = [item.text for item in reviews]
    # print(all_reviews)
       
    i = 0
    all_data = []
    all_data.append(['title','price','rating','reviews','links'])
    while i < 5:
        all_data.append([all_title[i],all_price[i],all_rating[i],all_reviews[i],all_links[i]])
        i +=1
    with open('walmart_data.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(all_data) 


if __name__ == "__main__":
    walmart('mobile')











