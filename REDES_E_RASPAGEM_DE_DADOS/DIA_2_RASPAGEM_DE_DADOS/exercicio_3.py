# 🚀 Exercício 4: Baseando-se em uma página contendo detalhes sobre um livro
# (http://books.toscrape.com/catalogue/the-grand-design_405/index.html),
# faça a extração dos campos título, preço,
# descrição e url contendo a imagem de capa do livro.

import requests
from parsel import Selector

response = requests.get(
    "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"
)
selector = Selector(text=response.text)
title = selector.css("h1::text").get()

prices = selector.css(".price_color::text").re(r"£\d+\.\d{2}")
print(prices[0].lstrip('£'))
description = selector.css("#product_description ~ p::text").get()
suffix = '...more'
if description.endswith(suffix):
    description = description[:-len(suffix)]

image = selector.css("img::attr(src)").get()
print(title, prices[0].lstrip('£'), description, image)
