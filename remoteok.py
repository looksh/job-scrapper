import requests
from bs4 import BeautifulSoup


# TODO keywords들을 가지고 url 요청하도록 만들기


class Scraper:
    # 웹사이트를 스크랩하는 객체가 가져야하는 상태.
    # url
    # skill
    # 스크랩한 배열
    # 메서드
    # 상태를 기반으로 스크랩하는 행동
    def __init__(self, url, skill):
        self.url = url
        self.skill = skill
        self.all_jobs = []

    def scrape_page(self):
        print(f"Scraping {self.url}")
        response = requests.get(
            url=self.url,
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ('
                                   'KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'},
        )
        soup = BeautifulSoup(response.content, "html.parser", )

        jobs = soup.find("table", id="jobsboard").find_all("td", class_="company")[1:]
        print(f"Found {self.skill} {len(jobs)}")
        for job in jobs:
            title = job.find("h2", itemprop="title").text.strip()
            company = job.find("h3", itemprop="name").text.strip()
            location = job.find("div", class_="location").text
            job_data = {
                "skill": self.skill,
                "title": title,
                "company": company,
                "location": location,
            }
            self.all_jobs.append(job_data)

    # 현재 코드에서는 스크랩된 작업 데이터를 all_jobs 리스트에 저장하지만, 이 리스트는 객체 내부에만 저장되기 때문에 외부에서 접근할 수 없음.
    # 스크랩된 작업 데이터를 활용하려면 클래스 외부에서 접근할 수 있도록 메서드를 통해 제공
    def get_jobs(self):
        return self.all_jobs


keywords = ['javascript', 'python', 'flutter']

for keyword in keywords:
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    keyword = Scraper(
        url=url,
        skill=keyword,
    )
    keyword.scrape_page()
    print(keyword.get_jobs())


