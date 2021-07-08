'''
Developed by: Zaahier Adams
https://github.com/ZaahierAdams
'''

from geocoder import osm
from csv import writer as CSVwritter
from csv import reader

def Failed(string, list_error):
    print('_________________________________________')
    print('FAILED:',string)
    return list_error.append(string)
    
def Geocoder():
    f = open('input.csv')
    text = ''
    csv_f = reader(f)
    list_error = []
    
    with open('Geocoded Addresses.csv', mode='w') as output:
        writer = CSVwritter(output, delimiter=',', lineterminator = '\n')
    
        writer.writerow(['Address','Latitude','Longitude'])
        
        for row in csv_f: 
            try:
                string  = row[0]
            except IndexError:
                continue
            try:
                g = osm(string, maxRows=1)
                lat = g.osm['y']
                long = g.osm['x']
                city1 = g.osm['addr:city']
                state1 = g.osm['addr:state']
                country1 = g.osm['addr:country']
                
                print('_________________________________________')
                print(string)
                print(lat,',',long)   
                writer.writerow([string, lat, long])

            except KeyError:
                Failed(string, list_error)
            except TypeError: 
                Failed(string, list_error)
                
    with open('Failed.csv', mode='w') as output:
        writer = CSVwritter(output, delimiter=',', lineterminator = '\n')
        writer.writerow(['Addresses failed to Geocode'])
        print(list_error)
        for fail in list_error:
            writer.writerow([fail])
    f.close()
if __name__ == '__main__':
    Geocoder()
    
                
        
        
        
        
    
