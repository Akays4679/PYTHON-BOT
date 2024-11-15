from requests import*


news_api_key="34e11813918e40a49b8cb0c2c26e86d7"
base_url="https://newsapi.org/v2/top-headlines"
class_news={
  'sources':'cnbc',
  'apiKey':news_api_key 
}
#fetching the news articles also i just wanted to take the headline and wanted to post the link of the news outlet regarding the tech and finances and some economic affairs
response=get(base_url)
articles=response.json()['articles']
for article in articles:
    print(article['title'])
