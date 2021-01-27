import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/wfootball/record/index.nhn', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

rank_table = soup.select('#wfootballTeamRecordBody > table > tbody> tr:nth-child(1)')

for info in rank_table:
    team_rank = info.select_one('td.num.best > div.inner > strong').text
    team_name = info.select_one('td.align_l> div.inner > span.name').text
    win_point = info.select_one('td.selected> div.inner > span').text
    if float(win_point) > 30:
        print(team_rank, team_name, win_point)

#container

# wfootballTeamRecordBody > table > tbody > tr:nth-child(1) > td.num.best > div > strong

#wfootballTeamRecordBody > table > tbody > tr:nth-child(1) > td.align_l > div > span

# wfootballTeamRecordBody > table > tbody > tr:nth-child(1) > td.selected > div > span
