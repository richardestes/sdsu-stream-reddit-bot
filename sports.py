from sportsreference.ncaab.schedule import Schedule
from sportsreference.ncaab.teams import Teams
import datetime

# teams = Teams()
# for team in teams:
#     print(team.name, team.abbreviation)

def check_if_game_today():
    game_today_bool = False
    now = datetime.datetime.now()
    # date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    now_date_time = now.strftime("%Y-%m-%d")

    print("Current date:")
    print(now_date_time)
    print()

    sdsu_schedule = Schedule('san-diego-state')
    for game in sdsu_schedule:
        game_date = game.datetime.strftime("%Y-%m-%d")
        game_hour = game.datetime.strftime("%H")
        game_hour_int = int(game_hour)
        game_hour_pst = game_hour_int - 3
        if (now_date_time == game_date):
            print("Hey there's a game today!")
            print(game.datetime)
            print(game_date)
            print(game_hour_pst)
            print(game.opponent_name)
            game_today_bool = True
            break
    return game_today_bool




    