from tkinter import *
import http.client
import json

window = Tk()
window.title("Football Score Query")
window.geometry('550x700')

def matchday_increment():
    int_matchday = int(lbl_matchdaynum.cget('text'))
    if( int_matchday < 38):
        int_matchday += 1
        lbl_matchdaynum.configure(text=str(int_matchday))

def matchday_decrement():
    int_matchday = int(lbl_matchdaynum.cget('text'))
    if(int_matchday > 1):
        int_matchday -= 1
        lbl_matchdaynum.configure(text=str(int_matchday))

def matchday_get():
    return int(lbl_matchdaynum.cget('text'))

def write_match_result(match, outrow):
    lbl_hometeam = Label(window,text=match['homeTeam']['name'])
    lbl_awayteam = Label(window,text=match['awayTeam']['name'])
    lbl_hometeam.grid(column=0,row=outrow)
    lbl_awayteam.grid(column=2,row=outrow)
    lbl_score = Label(window,text=str(match['score']['fullTime']['homeTeam']) + '-' + str(match['score']['fullTime']['awayTeam']))
    if( str(match['score']['fullTime']['homeTeam']) == 'None' ):
        lbl_score = Label(window,text='vs')
    lbl_score.grid(column=1,row=outrow)

def fetch_PL():
    reset_window()
    fetch_scores('PL')

def fetch_LALIGA():
    reset_window()
    fetch_scores('PD')
    
def fetch_BULI():
    reset_window()
    fetch_scores('BL1')

def fetch_SERIEA():
    reset_window()
    fetch_scores('SA')

def fetch_scores(league_code):
    outrow = 2
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': 'b3c9c945282c47e7934f8b4128a3bf2a' }
    reqstring = '/v2/competitions/' + league_code + '/matches?matchday=' + str(matchday_get())
    connection.request('GET', reqstring, None, headers )
    response = json.loads(connection.getresponse().read().decode())
    matches_list = response['matches']
    for match in matches_list:
        write_match_result(match, outrow)
        outrow += 2

def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def reset_window():
    slave_list = window.grid_slaves()
    for slave in slave_list:
        print(str(slave))
        print(right(str(slave),3))
        if (left(str(slave), 7) == '.!label' and right(str(slave),3) != 'el2' and right(str(slave),3) != 'bel'):
            slave.destroy()

lbl_matchdaytitle = Label(window,text='Matchday')
lbl_matchdaytitle.grid(column=0,row=1)
lbl_matchdaynum = Label(window,text='1')
lbl_matchdaynum.grid(column=1,row=1)
btn_decrement = Button(window, text="<",bg='red',command=matchday_decrement )
btn_decrement.grid(column=4, row=0)
btn_increment = Button(window, text=">",bg='red',command=matchday_increment )
btn_increment.grid(column=5, row=0)
btn_reset = Button( window, text="Reset", bg='blue', command=reset_window )
btn_reset.grid(column=0, row=0)
btn_EPL = Button( window, text="PL", bg='green', command=fetch_PL )
btn_EPL.grid(column=7, row=0)
btn_LALIGA = Button( window, text="LLA", bg='green', command=fetch_LALIGA )
btn_LALIGA.grid(column=8, row=0)
btn_BULI = Button( window, text="BULI", bg='green', command=fetch_BULI )
btn_BULI.grid(column=9, row=0)
btn_SERIEA = Button( window, text="SA", bg='green', command=fetch_SERIEA )
btn_SERIEA.grid(column=10, row=0)

window.mainloop()