import csv
def readCsv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = []
        header = next(reader)
        for row in reader:
            iterable = zip(header, row)
            countryDict = {key: value for key, value in iterable}
            data.append(countryDict)
        return data

if __name__ == '__main__':
    data = readCsv('./world_population.csv')
    print(data[0])