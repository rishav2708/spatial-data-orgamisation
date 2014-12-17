import json
from geopy import Nominatim
geocoder=Nominatim()
l=["NEW DELHI","KOLKATA","BANGLORE","CHENNAI","HYDERABAD","AHMEDABAD","PUNE"]
records=[]
d={}
for i in l:
	location=geocoder.geocode(i)
	t=tuple([location.latitude,location.longitude])
	d[i]=t
	
fp=open("loction.json","w")
json.dump(d,fp);



"""I have many ideas need to be implemented in the field of data mining. The idea is simply to build intelligent systems based on natural language processing. I hope in your able guidance and platform I would be able to explore and unleash my hidden potential.

I am a young,dynamic and a confident individual who wishes to acquire knowledge from your prestigious firm and contribute my knowledge in the best possible way."""
