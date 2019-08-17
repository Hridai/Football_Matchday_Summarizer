# Football_Matchday_Summarizer
Pulls scores, scorers and tables (live and past results) via an API. GUI built using TKINTER

# Why
To get familiar with basic UI programming in Python and resolving JSON outputs and outputting it in a useful way
Also because I want to check football scores, results, tables by just clicking buttons and not dong numerous google searches. If I want to check the big 4 league results/scorers/standings, I would have to do at least 4 google searches and click into every game to see the scorers individually. Then click again to see the standings.
This displays all the pertinent information from the matchday for the league in question in one easy click.

# NOTE
The free license to this API only allows 10 calls a minute. Each of the below, per league count as one call:
-	Standings
-	Matches
-	Goalscorers in each game

So clicking on "PL" costs 2 calls as it loads the matches and then the scorers underneath it. If standings are ticked, it will cost 3 calls.

# ToDo
- Add Standings when pressing a league button (Possibly with a checkbox? So as not to blast through the free limit of calls to API)
- Add more leagues (Ligue 1? Trivial addition)
- Add scorers by default
- Add times for games in matchweek not yet played
- Add a screenshot of the GUI in this readme
- Format the Matchweek. Add a heading
- Put all of the results in a scrollable list, as it will easily exceed the height of the screen if many scorers, standings incl
