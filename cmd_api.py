'''Command line app that consumes public APi'''

import requests

def app():
    '''Reads json data from API, returns a headline,
    author of the article, and a short excerpt from the article'''

    json_data = requests.get(
        "https://newsapi.org/v1/articles?source=techcrunch&apiKey=0240c7583a744026977e20577dae994b")

    as_python_dict = json_data.json()

    articles_in_dict = as_python_dict['articles']

    for article in articles_in_dict:
        print('HEADLINE: ' + article['title'])
        print('Author: ' + article['author'])
        print()
        print(article['description'])
        print()
        print('...' * 60)

app()
