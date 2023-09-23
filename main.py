import distanceinfo as di
import smarkets_scraper as sms
import matchdata as md
import betting_algorithm

if __name__ == '__main__':

    scraper = sms.SmarketsScraper()

    match_data_list = scraper.get_match_data()

    betting_algorithm = betting_algorithm.BettingAlgorithm()
    betting_algorithm.distancetimemodel(match_data_list)


