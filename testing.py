import requests

gameId = "0041500233"
API_URL = 'https://stats.nba.com/stats/playbyplayv2?EndPeriod=10&EndRange=55800&GameID=%s&RangeType=2&StartPeriod=1&StartRange=0'

GET_TEAMS_URL = 'https://stats.nba.com/stats/boxscoresummaryv2?gameID=%s'

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

headers = {
    'User-Agent': user_agent,
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Referer': 'http://stats.nba.com/events/',
}
r = requests.get(API_URL % gameId, headers=headers)
with open('sample_data.txt', 'w') as file:
    file.write(r.text)
