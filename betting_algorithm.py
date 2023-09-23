import distanceinfo as di
import matchdata as md


class BettingAlgorithm:
    def __init__(self):
        pass

    def distancetimemodel(self, match_data_list):
        for matchdata in match_data_list:
            distanceinfo = di.DistanceInfo()

            time_array = matchdata.get_data(md.MatchDataFields.TIME).split(" ")

            time_in_minutes = 0
            if time_array[0].split(":")[0].isnumeric():
                display_time = time_array[0]
                time_in_minutes = (int(time_array[0].split(":")[0]) * 60) + int(time_array[0].split(":")[1])

            else:
                display_time = time_array[1]
                time_in_minutes = (int(time_array[1].split(":")[0]) * 60) + int(time_array[1].split(":")[1])

            home_team = matchdata.get_data(md.MatchDataFields.HOMETEAM)
            away_team = matchdata.get_data(md.MatchDataFields.AWAYTEAM)

            distance_between_teams = int(distanceinfo.get_distance_between_two_teams(home_team, away_team))

            print(home_team + " vs " + away_team + " at " + display_time + " :")

            if time_in_minutes < 780:#
                if(distance_between_teams>210):
                    print("£10 on " + away_team + " to not win.")
                elif(distance_between_teams > 120):
                    print("£6 on " + away_team + " to not win.")
                else:
                    print("£3 on " + away_team + " to not win.")
            elif time_in_minutes < 850:
                if (distance_between_teams > 210):
                    print("£6 on " + away_team + " to not win.")
                elif (distance_between_teams > 120):
                    print("£3 on " + away_team + " to not win.")
                else:
                    print("No bet.")
            else:
                if (distance_between_teams > 210):
                    print("£3 on " + away_team + " to not win.")
                else:
                    print("No bet.")




