import json
data= {
    "Kerala":"Thiruvananthapuram",
    "Karnataka":"Bengaluru",
    "Tamil Nadu": "Chennai",
    "Maharashtra":"Mumbai",
    "Rajasthan" :"Jaipur",
    "Andhra Pradesh" :"Visakhapatanam",
    "Telangana" : "Hyderbad"
}
file=open("C:\\Users\\Amrutha Ajay\\Desktop\\New folder (2)\\assign6\\qstn2.json","w")
json.dump(data,file)