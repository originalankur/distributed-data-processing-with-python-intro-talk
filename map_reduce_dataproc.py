import json

from mrjob.job import MRJob
from mrjob.step import MRStep


class MRYelpTopCity(MRJob):
    """
    Find city with most no of restaurants in Yelp dataset.
    https://www.yelp.com/dataset 
    business.json stores the data of all restaurants in Yelp dataset.
    In each individual business.json file, there is a field called "city"
    we want to find out the city with most number of restaurants.
    """

    def mapper_get_city(self, key, line):
        try:
            single_business = json.loads(line)
            if single_business.get('city'):
                # "San Francisco", 1
                # "Los Angeles", 1
                yield single_business['city'], 1
            else:
                yield 'missing_city', 1
        except:
            pass

    def combiner_count_cities(self, city, occurance):
        # "San Francisco", (1,1,1,1,1,1,1,1,1) # per worker node
        yield (city, sum(occurance))

    def reducer_count_cities(self, city, counts):
        # "San Francisco", [9,3,7,2]
        # 21, "San Francisco"
        yield None, (sum(counts), city)

    def reducer_find_max_city(self, _, city_count_pairs):
        # [(21, "San Francisco"), (30, "Los Angeles"), (79, "San Diego"), (21, "San Jose")]
        # (79, "San Diego")
        yield max(city_count_pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_city,
                   combiner=self.combiner_count_cities,
                   reducer=self.reducer_count_cities),
            MRStep(reducer=self.reducer_find_max_city)
        ]


if __name__ == '__main__':
    MRYelpTopCity.run()
