import distanceinfo as di
import smarkets_scraper as sms
import matchdata as md

if __name__ == '__main__':
    distance_info = di.DistanceInfo()
    print(distance_info.get_distance_between_two_teams("west ham", "liverpool"))
    scraper = sms.SmarketsScraper()

    match_data_list = scraper.get_match_data()

    for matchdata in match_data_list:
        time = matchdata.get_data(md.MatchDataFields.TIME)


