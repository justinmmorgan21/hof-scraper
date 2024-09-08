# Webscraping project copied from Imdad Codes YouTube 
# https://www.google.com/search?q=webscraping+for+beginners&oq=webscraping+for+beginners&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDU5NjJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:44db937e,vid:M37koTo8NjA,st:0
import webbrowser
import httpx
from bs4 import BeautifulSoup

url = 'https://www.fantasypros.com/nfl/players/christian-mccaffrey.php'
headers = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

# def extract_product_data(product):
#   try:
#     name = product.find('span', class_='productdescriptionname').text
#     brand = product.find('span', class_='productdescriptionbrand').text
#     price = product.find('span', class_='CurrencySizeLarge curprice').text.strip()
#     print(f'Brand: {brand} Name: {name} Price: {price}')
#   except Exception as e:
#     print(e)

def main():
  response = httpx.get(url, headers=headers)
  response_html = response.text
  soup = BeautifulSoup(response_html, 'html.parser')
  details = soup.find_all('div', class_='clearfix detail')
  print(details[2].find('span', class_='pull-right').text)
  image = soup.find('img', class_='side-nav-player-photo-radius-8')
  print(image.get('src'))

  # URL of the image
  image_url = image.get('src')

  # Open the image in the default web browser
  webbrowser.open(image_url)

  # products = soup.find_all('div', class_='s-productthumbbox')
  # for product in products:
  #   extract_product_data(product)

if __name__ == '__main__':
  main()