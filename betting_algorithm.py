import distanceinfo as di
import matchdata as md


class BettingAlgorithm:
    def __init__(self):
        self.write_file = False
        self.match_week = 0
        self.file = 0

    def distancetimemodel(self, match_data_list):

        file_user_input = input("Do you want to write to file (y/n)")
        if file_user_input == "y":
            self.write_file = True
            self.match_week = input("Which match week is it? ")
            self.file = open("Resources/week" + self.match_week + "data.txt","w")

        for matchdata in match_data_list:
            distanceinfo = di.DistanceInfo()

            time_array = matchdata.get_data(md.MatchDataFields.TIME).split(" ")

            display_time, time_in_minutes = self._get_display_time(time_array)

            home_team = matchdata.get_data(md.MatchDataFields.HOMETEAM)
            away_team = matchdata.get_data(md.MatchDataFields.AWAYTEAM)

            distance_between_teams = int(distanceinfo.get_distance_between_two_teams(home_team, away_team))

            print(home_team + " vs " + away_team + " at " + display_time + " :")

            against_away_to_win_odd = matchdata.get_data(md.MatchDataFields.AWAYODDS)[1]

            is_bet = True
            liability = 0
            stake = 0
            if time_in_minutes < 780:  #
                if distance_between_teams > 210:
                    stake = self._get_laybet_stake(against_away_to_win_odd, 10)
                    liability = 10
                elif distance_between_teams > 120:
                    stake = self._get_laybet_stake(against_away_to_win_odd, 6)
                    liability = 6
                else:
                    stake = self._get_laybet_stake(against_away_to_win_odd, 3)
                    liability = 3
            elif time_in_minutes < 850:
                if distance_between_teams > 210:
                    stake = self._get_laybet_stake(against_away_to_win_odd, 6)
                    liability = 6
                elif distance_between_teams > 120:
                    stake = self._get_laybet_stake(against_away_to_win_odd, 3)
                    liability = 3
                else:
                    is_bet = False
                    print("No bet.")
            else:
                if distance_between_teams > 210:
                    stake = self._get_laybet_stake(against_away_to_win_odd, 3)
                    liability = 3
                else:
                    is_bet = False
                    print("No bet.")

            if is_bet:
                self._print_laybet(stake, liability, away_team)

    def _get_laybet_stake(self, odds: str, bet_amount):
        odds = float(odds)
        return str(bet_amount / (odds - 1))

    def _get_display_time(self, time_array):
        if time_array[0].split(":")[0].isnumeric():
            display_time = time_array[0]
            time_in_minutes = (int(time_array[0].split(":")[0]) * 60) + int(time_array[0].split(":")[1])

        else:
            display_time = time_array[1]
            time_in_minutes = (int(time_array[1].split(":")[0]) * 60) + int(time_array[1].split(":")[1])
        return display_time, time_in_minutes

    def _print_laybet(self, stake, liability, team):
        print("£" + stake + " (£" + str(liability) + " liability) on " + team + " to not win.")
        if self.write_file:
            self.file.write("£" + stake + " (£" + str(liability) + " liability) on " + team + " to not win.\n")

