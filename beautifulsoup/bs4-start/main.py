from bs4 import BeautifulSoup
import requests

response=requests.get(url="https://news.ycombinator.com/news")
yc_webpage=response.text


soup=BeautifulSoup(yc_webpage,"html.parser")


'''soup=BeautifulSoup(contents,"html.parser")

anchor_tags=soup.find_all(name="a")
for i in anchor_tags:
    print(i.get("href"))'''
results=[]
rows=soup.find_all(name="tr",class_="athing submission")
#print(rows)
pointers=[]
points=soup.find_all(name="td",class_="subtext")
for point in points:
    po=point.select_one("span.score")
    if po:
        text=po.get_text(strip=True)
        pointers.append(text)

print(pointers)

for row in rows:
    a=row.select_one("span.titleline > a")
    title=a.get_text(strip=True)
    link=a["href"]
    results.append((title,link))

for (title,link),points in zip(results,pointers):
    print(title)
    print(link)
    print(points)
    print()



