from playwright.sync_api import sync_playwright
import time

pw = sync_playwright().start()

# headless=True -> 브라우저를 띄우지않음
browser = pw.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/jobsfeed")

time.sleep(1)

page.click("button.Aside_searchButton__Xhqq3")

time.sleep(1)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("python")

time.sleep(1)

page.keyboard.down("Enter")

time.sleep(1)

page.click("a#search_tab_position")

time.sleep(3)

page.keyboard.down("End")

time.sleep(1)

page.keyboard.down("End")

time.sleep(3)

pw.stop()