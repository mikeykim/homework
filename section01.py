import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('/Users/user/Downloads/chromedriver', options=options)
driver.implicitly_wait(3)
driver.get('https://sports.news.naver.com/wfootball/record/index.nhn?category=epl&tab=team')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
rank_table = soup.select('#wfootballTeamRecordBody > table > tbody > tr')

for info in rank_table:
    team_rank = info.select_one('td > div.inner > strong').text

    team_name = info.select_one('td.align_l> div.inner > span.name').text
    win_point = info.select_one('td.selected> div.inner > span').text
    if float(win_point) > 30:
        print(team_rank, team_name, win_point)
