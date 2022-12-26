def getPopulation(countryDict):
    populationDict = {
        '1970': int(countryDict['1970 Population']),
        '1980': int(countryDict['1980 Population']),
        '1990': int(countryDict['1990 Population']),
        '2000': int(countryDict['2000 Population']),
        '2010': int(countryDict['2010 Population']),
        '2015': int(countryDict['2015 Population']),
        '2020': int(countryDict['2020 Population']),
        '2022': int(countryDict['2022 Population'])

    }
    keys = populationDict.keys()
    values = populationDict.values()
    return keys, values

def pupulationByCountry(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

def iterablePopulation(data):
    for i in data:
        country = list(filter(lambda item: item['Country/Territory'], data[i]))
        print(country)