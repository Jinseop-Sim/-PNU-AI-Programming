def make_country_list(file):
  infile = open(file, 'r')
  countryList = [line.rstrip() for line in infile]
  for i in range(len(countryList)):
    countryList[i] = countryList[i].split(',')
    countryList[i][2] = eval(countryList[i][2])
    countryList[i][3] = eval(countryList[i][3])
  return countryList

def show_FLC(countries):
  print("{0:20}{1:9}.format("Country", "Area (sq. mi.)"))
  for i in range(5):
        print("{0:20}{1:9,d}.format(countries[i][0], countries[i][3]))
  
def create_new_file(countries):
  outfile = open("UNbyArea.txt")
  for country in countries:
    outfile.write(country[0] + ',' + str(country[3]) + "\n")
  outfile.close()

countries = make_country_list("UN.txt")
countries.sort(key=lambda country: country[3], reverse=True)
show_FLC(countries)
create_new_file(countries)
