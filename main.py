import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser",)

# class_를 사용하는 이유는 python에서 class는 예약어이므로
jobs = soup.find("section", class_="jobs").find_all("li")[1: -1]

for job in jobs:
    title = job.find("span", class_="title")
    print(title)