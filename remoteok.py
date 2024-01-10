import requests
from bs4 import BeautifulSoup

# TODO keywords들을 가지고 url 요청하도록 만들기

#
# class Scraper:
#     # 웹사이트를 스크랩하는 객체가 가져야하는 상태.
#     # url
#     # skill
#     # 메서드
#     # 상태를 기반으로 스크랩하는 행동
#     def __init__(self, url, skill):
#         self.url = url
#         self.skill = skill
#
#     def scrape_page(self):


keywords = ['javascript', 'python', 'flutter']
all_jobs = []

def scrape_page(skill, url):
    print(f"Scraping {url}")
    response = requests.get(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ('
                               'KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'},
    )
    soup = BeautifulSoup(response.content, "html.parser", )

    jobs = soup.find("table", id="jobsboard").find_all("td", class_="company")[1:]
    print(f"Found {skill} {len(jobs)}")
    for job in jobs:
        title = job.find("h2", itemprop="title").text.strip()
        company = job.find("h3", itemprop="name").text.strip()
        location = job.find("div", class_="location").text
        job_data = {
            "skill": skill,
            "title": title,
            "company": company,
            "location": location,
        }
        all_jobs.append(job_data)


for keyword in keywords:
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    scrape_page(keyword, url)
