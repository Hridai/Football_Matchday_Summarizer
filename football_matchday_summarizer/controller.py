from atom.atom import Atom, observe
from atom.api import Int, Str, List

from football_matchday_summarizer.model import *

class MatchDaySummaryController(Atom):
    # lhs screen
    match_day = Int(1)
    match_list = List() # from API call
    league_code = Str(default='PL')
    home_teams = List()
    away_teams = List()
    scores = List()
    
    # rhs screen
    standings_list = List() # from API call
    standings_team = List()
    standings_p = List()
    standings_w = List()
    standings_l = List()
    standings_d = List()
    standings_gf = List()
    standings_ga = List()
    standings_gd = List()
    standings_pts = List()

    def increment_match_day(self):
        self.match_day += 1

    def decrement_match_day(self):
        if self.match_day > 1:
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
    
    @observe('standings_list')
    def write_standings(self, *args):
        temp_teams = []
        temp_p = []
        temp_w = []
        temp_l = []
        temp_d = []
        temp_gf = []
        temp_ga = []
        temp_gd = []
        temp_pts = []
        for entry in self.standings_list:
            temp_teams.append(entry['team']['name'])
            temp_p.append(str(entry['playedGames']))
            temp_w.append(str(entry['won']))
            temp_l.append(str(entry['lost']))
            temp_d.append(str(entry['draw']))
            temp_gf.append(str(entry['goalsFor']))
            temp_ga.append(str(entry['goalsAgainst']))
            temp_gd.append(str(entry['goalDifference']))
            temp_pts.append(str(entry['points']))
        self.standings_team = temp_teams
        self.standings_p = temp_p
        self.standings_w = temp_w
        self.standings_l = temp_l
        self.standings_d = temp_d
        self.standings_gf = temp_gf
        self.standings_ga = temp_ga
        self.standings_gd = temp_gd
        self.standings_pts = temp_pts
            
    
    @observe('match_day', 'league_code')
    def refresh_match_list(self, *args):
        self.match_list = fetch_scores(league_code=self.league_code, match_day=self.match_day)
    
    @observe('league_code')
    def refresh_standings_list(self, *args):
        self.standings_list = fetch_standings(league_code=self.league_code)
