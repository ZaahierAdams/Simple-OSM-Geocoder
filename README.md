# Simple OSM Geocoder
<img alt="Icon" src="https://i.imgur.com/PUq3bS8.png" width="10%"></img>

## About
This is a Python application for geocoding addresses. 
It converts addresses to geographical coordinates using the open-source API *Nominatim*. 

### This repository includes:
- ``` main.py``` the application’s python code  
- ```input.csv``` test input data for the application 

## How to use 
1. Input data:
	- Should be in the same directory as the application
	- the file should be ```.csv``` format and named ```input.csv```
 	- Within ```input.csv``` list the addresses to be geocoded
  
  
2. To Run the application:
    - Run ``` main.py```. You will need to install [Python]( https://www.python.org/downloads/) and the [Geocoder]( https://pypi.org/project/geocoder/) library.


3. Once completed, the application will produce two .csv files: 
    - ```Geocoded Addresses.csv``` Contains addresses that were geocoded
    - ```Failed.csv``` Contains addresses that **failed** to geocode 

## Acknowledgements 
[Nominatim](https://nominatim.org/)

The icon used was created by [Freepik](https://www.freepik.com/) 



