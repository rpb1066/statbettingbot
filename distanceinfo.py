import math
import csv
class DistanceInfo:
    def __init__(self):
        self.team_location = dict()
        self.time_taken_dict = dict()

        self.create_team_dict()
        self.create_time_travelled_dict()

    def create_team_dict(self):
        self.team_location["arsenal"] = "London"
        self.team_location["aston villa"] = "Birmingham"
        self.team_location["bournemouth afc"] = "Bournemouth"
        self.team_location["brentford"] = "London"
        self.team_location["brighton & hove albion"] = "Brighton"
        self.team_location["burnley"] = "Burnley"
        self.team_location["chelsea"] = "London"
        self.team_location["crystal palace"] = "London"
        self.team_location["everton"] = "Liverpool"
        self.team_location["fulham"] = "London"
        self.team_location["liverpool"] = "Liverpool"
        self.team_location["luton town"] = "Luton"
        self.team_location["manchester city"] = "Manchester"
        self.team_location["manchester united"] = "Manchester"
        self.team_location["newcastle"] = "Newcastle"
        self.team_location["nottingham forest"] = "Nottingham"
        self.team_location["southampton"] = "Southampton"
        self.team_location["tottenham hotspur"] = "London"
        self.team_location["west ham united"] = "London"
        self.team_location["wolverhampton wanderers"] = "Wolverhampton"

    def create_time_travelled_dict(self):
        file = open("Resources/traveltimes.txt", "r")
        time_taken_array = file.read().split("\n")
        for timepair in time_taken_array:
            locA, locB, time = timepair.split(",")
            self.time_taken_dict[frozenset((locA, locB))] = time

    def get_distance_between_two_teams(self, A, B):
        team_a = A.lower()
        team_b = B.lower()

        for team in self.team_location.keys():
            if team_a in team:
                team_a = team
            if team_b in team:
                team_b = team

        if self.team_location[team_a] == self.team_location[team_b]:
            return 0
        else:
            return self.time_taken_dict[
                frozenset((self.team_location[team_a].lower(), self.team_location[team_b].lower()))]
