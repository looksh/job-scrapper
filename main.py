import requests
from bs4 import BeautifulSoup

all_jobs = []


# 페이지의 job 목록을 가져오기
def scrape_page(url):
    print(f"Scraping {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser", )

    # class_를 사용하는 이유는 python에서 class는 예약어이므로
    jobs = soup.find("section", class_="jobs").find_all("li")[1: -1]
    for job in jobs:
        title = job.find("span", class_="title").text
        company, time, region = job.find_all("span", class_="company")
        link = job.find("div", class_="tooltip")
        if link:
            link = link.next_sibling["href"]
        job_data = {
            "title": title,
            "company": company.text,
            "time": time.text,
            "region": region.text,
            "link": f"https://weworkremotely.com{link}",
        }
        all_jobs.append(job_data)


# 페이지의 개수를 알아내는 함수
def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser", )
    return len(soup.find_all("span", class_="page"))


# 페이지의 총 개수가 저장되는 변수
total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

# 페이지 개수에 따른 요청 url 만들기
for number in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={number + 1}"
    scrape_page(url)

# print(len(all_jobs))
