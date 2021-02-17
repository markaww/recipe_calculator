import requests
from bs4 import BeautifulSoup
import re
import random

allrecipes_urls = ['https://www.allrecipes.com/recipes/200/meat-and-poultry/beef/',
                   'https://www.allrecipes.com/recipes/201/meat-and-poultry/chicken/',
                   'https://www.allrecipes.com/recipes/205/meat-and-poultry/pork/',
                   'https://www.allrecipes.com/recipes/93/seafood/',
                   'https://www.allrecipes.com/recipes/225/side-dish/vegetables/',
                   'https://www.allrecipes.com/recipes/95/pasta-and-noodles/',
                   'https://www.allrecipes.com/recipes/96/salad/',
                   'https://www.allrecipes.com/recipes/84/healthy-recipes/', ]


allrecipes_categories = [re.sub("\d", "", i[37:-1])[1:] for i in allrecipes_urls]


def get_recipes():
    html_list = [requests.get(url).content for url in allrecipes_urls]
    soup_list = [BeautifulSoup(html, 'html.parser') for html in html_list]

    links_raw = [soup.find_all('a', {'class': 'card__titleLink manual-link-behavior'}) for soup in soup_list]

    pattern = 'href+(.*?)tab'

    links_clean = [re.findall(pattern, str(i)) for i in links_raw]

    links_clean[1]

    dictionary = dict(zip(allrecipes_categories, links_clean))
    list(dictionary.keys())

    recipe_picks = [re.sub('\'="', '', f'{i}: {random.sample(dictionary[i], 3)}') for i in allrecipes_categories]

    return recipe_picks


print(get_recipes())