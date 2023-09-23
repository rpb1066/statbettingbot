import os
from enum import Enum
from enum import auto


class MatchData:
    def __init__(self, smarkets_match_data, time: str):
        self.match_data_dict = dict()

        self.match_data_dict[MatchDataFields.TIME] = " ".join(time.replace(",", "").split(" "))
        data_list = smarkets_match_data.split("\n")

        self.match_data_dict[MatchDataFields.HOMETEAM] = data_list[0]
        self.match_data_dict[MatchDataFields.AWAYTEAM] = data_list[1]
        self.match_data_dict[MatchDataFields.DAY] = data_list[2]
        self.match_data_dict[MatchDataFields.HOMEODDS] = (data_list[6], data_list[8])
        self.match_data_dict[MatchDataFields.DRAWODDS] = (data_list[11], data_list[13])
        self.match_data_dict[MatchDataFields.AWAYODDS] = (data_list[16], data_list[18])

        print(self.match_data_dict.values())

    def get_data(self, data_field):
        return self.match_data_dict[data_field]


class MatchDataFields(Enum):
    HOMETEAM = auto()
    AWAYTEAM = auto()
    DAY = auto()
    HOMEODDS = auto()
    DRAWODDS = auto()
    AWAYODDS = auto()
    TIME = auto()
