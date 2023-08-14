import math
import csv

team_location = dict()
time_taken_dict = dict()
def get_team_dict():
    team_location["arsenal"] = "London"
    team_location["aston villa"] = "Birmingham"
    team_location["bournemouth afc"] = "Bournemouth"
    team_location["brentford"] = "London"
    team_location["brighton & hove albion"] = "Brighton"
    team_location["burnley"] = "Burnley"
    team_location["chelsea"] = "London"
    team_location["crystal palace"] = "London"
    team_location["everton"] = "Liverpool"
    team_location["fulham"] = "London"
    team_location["liverpool"] = "Liverpool"
    team_location["luton town"] = "Luton"
    team_location["manchester city"] = "Manchester"
    team_location["manchester united"] = "Manchester"
    team_location["newcastle united"] = "Newcastle"
    team_location["nottingham forest"] = "Nottingham"
    team_location["southampton"] = "Southampton"
    team_location["tottenham hotspur"] = "London"
    team_location["west ham united"] = "London"
    team_location["wolverhampton wanderers"] = "Wolverhampton"

def create_time_travelled_dict():
    file = open("Resources/traveltimes.txt","r")
    time_taken_array = file.read().split("\n")
    for timepair in time_taken_array:
        locA,locB,time = timepair.split(",")
        time_taken_dict[frozenset((locA,locB))] = time


def get_distance_between_two_teams(A, B):
    team_a = A.lower()
    team_b = B.lower()
    if team_location[team_a] == team_location[team_b]:
        return 0
    else:
        return time_taken_dict[frozenset((team_location[team_a].lower(),team_location[team_b].lower()))]


def init_distance_info():
     get_team_dict()
     create_time_travelled_dict()








