from geopy.geocoders import Nominatim 
from geopy import distance

lug_um = input("Lugar um: ")
lug_dois = input("Lugar dois: ")

loc_um = Nominatim(user_agent="GetLoc") 
getLoc_um = loc_um.geocode(lug_um) 

loc_dois = Nominatim(user_agent="GetLoc") 
getLoc_dois = loc_dois.geocode(lug_dois) 

um = (getLoc_um.latitude, getLoc_um.longitude)
dois = (getLoc_dois.latitude, getLoc_dois.longitude)

print(f"Distância entre {lug_um} e {lug_dois}: {round(int(distance.distance(um, dois).kilometers), 2)}km")