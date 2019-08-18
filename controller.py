from atom.atom import Atom, observe
from atom.api import Int, Str, List

from model import fetch_scores

class MatchDaySummaryController(Atom):
    match_day = Int()
    league_code = Str()
    home_teams = List()
    away_teams = List()
    scores = List()
    match_list = List()

    def increment_match_day(self):
        self.match_day += 1

    def decrement_match_day(self):
        self.match_day -= 1

    @observe('match_list')
    def write_match_result(self, *args):
        home_teams = []
        away_teams = []
        scores = []
        for match in self.match_list:
            home_teams.append(match['homeTeam']['name'])
            away_teams.append(match['awayTeam']['name'])
            home_score_str = str(match['score']['fullTime']['homeTeam'])
            if home_score_str == 'None':
                score = 'vs'
            else:
                score = str(match['score']['fullTime']['homeTeam']) + '-' + str(match['score']['fullTime']['awayTeam'])
            scores.append(score)
        self.home_teams = home_teams
        self.scores = scores
        self.away_teams = away_teams

    @observe('match_day', 'league_code')
    def refresh_match_list(self, *args):
        self.match_list = fetch_scores(league_code=self.league_code, match_day=self.match_day)
