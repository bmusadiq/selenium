from selenium import webdriver
from pages.quotes_page import QuotePage
chrome=webdriver.Chrome(executable_path="E:\Downloads\chromedriver_win32\chromedriver.exe")
chrome.get('http://quotes.toscrape.com/search.aspx')
pages=QuotePage(chrome)
author=input('Enter the author you likes quote from: ')
pages.select_author(author)
tags=pages.get_available_tags()
print("select on of these tags{[]}".format(" | ".join(tags)))
selected_tag=input("Enter your tag: ")
pages.select_tag(selected_tag)