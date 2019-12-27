import pandas as pd
import requests


from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XgO5jEczZPY")
soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(id="seven-day-forecast-body")

items= week.find_all(class_="tombstone-container")
print(items[0].find(class_="period-name").get_text())
print(items[0].find(class_="short-desc").get_text())
print(items[0].find(class_="temp").get_text())
periodnames=[item.find(class_="period-name").get_text() for item in items]
print(periodnames)
shortdesc=[item.find(class_="short-desc").get_text() for item in items]
temperature=[item.find(class_="temp").get_text() for item in items]
print(shortdesc)
print(temperature)


weatherstuff= pd.DataFrame(
    {
        "period":periodnames,
        "short description":shortdesc,
        "temperature":temperature
    }


)
print(weatherstuff)
weatherstuff.to_csv("weather.csv")