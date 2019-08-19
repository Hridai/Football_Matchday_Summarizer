import http.client
import json


def fetch_scores(league_code, match_day):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': 'b3c9c945282c47e7934f8b4128a3bf2a'}
    reqstring = '/v2/competitions/' + league_code + '/matches?matchday=' + str(match_day)
    connection.request('GET', reqstring, None, headers)
    response = json.loads(connection.getresponse().read().decode())
    matches_list = response.get('matches', [])
    return matches_list
