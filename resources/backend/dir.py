import requests
import json
def where_to(li):
    print("Please enter your latitude.")
    iss=0
    while iss==0:
        try:
            lat=float(input())
            iss=1
        except:
            print("Please input a decimal number.")
    print("Please enter your longtitude.")
    iss=0
    while iss==0:
        try:
            lon=float(input())
            iss=1
        except:
            print("Please input a decimal number.")
    url="https://maps.googleapis.com/maps/api/directions/json?origin="+str(lat)+","+str(lon)+"&destination="+str(lat)+","+str(lon)+"&waypoints="
    for i in range(len(li)):
        url+=li[i]
        if i+1<len(li):
            url+="|"
    url+="&key=AIzaSyAZE2aUeyKWQxpYwdTDM1HNmVeeg9d1uDw"
    hi3=requests.get(url)
    hi4=json.loads(hi3.text)
    asdf1=0
    while 1==1:
        try:
            u=hi4['routes'][0]['legs'][asdf1]['steps'][0]['html_instructions']
        except:
            break
        asdf2=0
        while 1==1:
            try:
                print(hi4['routes'][0]['legs'][asdf1]['steps'][asdf2]['html_instructions'])
                print("For another", hi4['routes'][0]['legs'][asdf1]['steps'][asdf2]['distance']['text'])
            except:
                break
            asdf2+=1
        asdf1+=1
