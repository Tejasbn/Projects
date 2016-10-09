import json
import requests, datetime, time
from datetime import timedelta
geocode = "https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJY9xPAvEWrjsRzNwYYdPoVWU&key=AIzaSyDzIBQRTNa2TcLK6kqPUkfrTs94wQCTkSc" #fetches contents from api
gresp = requests.get(geocode)
gresp = json.loads(gresp.content)

#initialisations
j=0;
start = []
end = []
start_t = [0]*7
start_hours = [0]*7
end_hours = [0]*7
start_mins = [0]*7
end_mins = [0]*7
next_hours= [0]*7
available_time_hr=[0]*7
rem = [0]*7
slots = [0]*7


for i in range(0,6):
    
    
    start = gresp["result"]["opening_hours"]["periods"][i]["open"]["time"] #fetches start time
    end = gresp["result"]["opening_hours"]["periods"][i]["close"]["time"] #fetches end time
    day = gresp["result"]["opening_hours"]["periods"][i]["close"]["day"]  #fetches day 
    #print day
    #print start
    #print end
    
    start_hours[i] = int(start[0:2])
    start_mins[i] = int(start[2:4])
    end_hours[i] = int(end[0:2])
    end_mins[i] = int(end[2:4])
    #print start_hours
    available_time_hr[i] = end_hours[i] - start_hours[i]
    
    #print available_time_hr
    
    slots[i] = (available_time_hr[i] / 3) + (available_time_hr[i] % 3); #calculatng number of slots ( if slots are not divisible by 3 then remainder time is made into another slot)
    #print slots
    next_hours[i] = start_hours[i]

    print "day = " + str(i+1)
    for j in range(1,slots[i]+1):
        
        next_hours[j] = next_hours[i] +   3
        i=j

        data = {
            
            'slot '+str(j) : str(datetime.time(hour=next_hours[j-1],minute=int(start_mins[i])))+" to " +str(datetime.time(hour=next_hours[j],minute=int(start_mins[i]))) 
                            }
        

        json_str = json.dumps(data)
        print json_str
    


    

    
  

    

    




    






    
