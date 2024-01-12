from playwright.sync_api import sync_playwright

pw = sync_playwright().start()

# headless=True -> 브라우저를 띄우지않음
browser = pw.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://example.com/")

page.screenshot(path="screenshot.png")