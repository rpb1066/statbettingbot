import distanceinfo as di
import smarkets_scraper as sms

if __name__ == '__main__':
    distance_info = di.DistanceInfo()
    print(distance_info.get_distance_between_two_teams("west ham", "liverpool"))
    scraper = sms.SmarketsScraper()

    scraper.getMatchData()

