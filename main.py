# Webscraping project copied from Imdad Codes YouTube 
# https://www.google.com/search?q=webscraping+for+beginners&oq=webscraping+for+beginners&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDU5NjJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:44db937e,vid:M37koTo8NjA,st:0
import webbrowser
import httpx
from bs4 import BeautifulSoup

url = 'https://www.houseoffraser.co.uk/men/hoodies-and-sweatshirts'
headers = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

def extract_product_data(product):
  try:
    name = product.find('span', class_='productdescriptionname').text
    brand = product.find('span', class_='productdescriptionbrand').text
    price = product.find('span', class_='CurrencySizeLarge curprice').text.strip()
    print(f'Brand: {brand} Name: {name} Price: {price}')
  except Exception as e:
    print(e)

def main():
  response = httpx.get(url, headers=headers)
  response_html = response.text
  soup = BeautifulSoup(response_html, 'html.parser')

  products = soup.find_all('div', class_='s-productthumbbox')
  for product in products:
    extract_product_data(product)

if __name__ == '__main__':
  main()