from Statistics import statistics

class Zscore:

    @staticmethod
    def zscore(data):
        mean = statistics.mean(data)
        stD = statistics.standardDeviation(data)
        for i in data:
            zscore = (i - mean) / stD
            return zscore
