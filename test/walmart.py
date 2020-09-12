from bs4 import BeautifulSoup
import requests,lxml
import json
import csv


''' this function to get dataset from walart website'''

def walmart(product):
    url = f'https://www.walmart.com/search/?query={product}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    resultsss = soup.find_all('div' , role="presentation")
    all_data=[['title','price','links']]


    for i in resultsss:
        try:
            each_product = []

            ### to get the name of the product
            title = i.find('a',class_ = 'product-title-link line-clamp line-clamp-2 truncate-title').text
            each_product.append(title)

            ### to get the price of the product
            price = i.find('span',class_ = 'price-group').text
            each_product.append(price)

            #### to  get the url link for each product
            links = i.find('a',class_ = 'product-title-link line-clamp line-clamp-2 truncate-title').get('href')
            each_product.append(f"https://www.walmart.com{links}")

            all_data.append(each_product)
           
            """ to get reviews for each product"""
            # reviews = i.find('span',class_ = 'seo-review-count visuallyhidden').text
            # each_product.append(reviews)
            
            """to get rating for each product """
            # rating = i.find('span',class_ = 'visuallyhidden seo-avg-rating').text
            # each_product.append(rating)

            
                        
        except :
            continue

    
    
       
    ### to send the data sets into .csv file
    with open('walmart_data.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(all_data)  


if __name__ == "__main__":
    walmart('tv')