#!/usr/bin/env python3


url = 'https://www.buffalotracedistillery.com/product-availability'

def __list_from_elements(list_of_elements):
  product_list = []
  for element in list_of_elements:
    product_list.append(element.text)
  return product_list

def __list_products(list_of_products):
  for product in list_of_products:
    print(f" - {product}")

from requests_html import HTMLSession

session = HTMLSession()
response = session.get(url)

available_products_selector = '.container--product-availability-available .container--product-availability-available h3'
available_products = __list_from_elements(response.html.find(available_products_selector))

unavailable_products_selector = '.container--product-availability-available .container--product-availability-not-available h3'
unavailable_products = __list_from_elements(response.html.find(unavailable_products_selector))

print('Available Products:')
__list_products(available_products)

print('')

print('Unavailable Products:')
__list_products(unavailable_products)  


