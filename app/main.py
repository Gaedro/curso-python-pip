import utils
import read_csv
import charts

#print(data[0])

def run():
  data= read_csv.leer_excel('world_population.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  
  pais = input('Type Country => ')
  
  result = utils.population_by_country(data, pais)
  #print(result)
  if len(result) > 0:
    country = result[0]
    #print(country)
    labels, values = utils.get_poblacion(country)
    #print(labels, values)
    charts.generate_bar_chart(pais, labels, values)  

if __name__ == '__main__':
  run()