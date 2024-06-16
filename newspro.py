from lxml import html
import requests

url = requests.get("https://www.indiatvnews.com")

res = html.fromstring(url.content)

p= res.xpath("//h3/text()")

for i in p:
    print(i)
