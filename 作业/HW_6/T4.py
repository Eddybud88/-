from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# 页面的确没有出版社
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://search.jd.com/Search?keyword=python%20%E4%B9%A6%E7%B1%8D&enc=utf-8')

time.sleep(5)

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

books = []
for item in soup.select('.gl-item'):
    book_name = item.select_one('.p-name em').text.strip()
    price = item.select_one('.p-price i').text.strip()
    publisher = item.select_one('.p-shopnum').text.strip() if item.select_one('.p-shopnum') else 'N/A'
    books.append({
        'book_name': book_name,
        'price': price,
        'publisher': publisher
    })

for book in books[:5]:
    print(f"书名: {book['book_name']}\n价格: {book['price']}\n出版社: {book['publisher']}\n")

driver.quit()

