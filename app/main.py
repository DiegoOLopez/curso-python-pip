import utils
import readCSV
import charts

def run():

    data = readCSV.readCsv('world_population.csv')

    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generatePieChart(countries, percentages)
    data = readCSV.readCsv('world_population.csv')
    country = input('Ingresa un pais: ')
    result = utils.pupulationByCountry(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.getPopulation(country)
        charts.generateBarChart(labels, values, country['Country/Territory'])

if __name__ == '__main__':
    run()