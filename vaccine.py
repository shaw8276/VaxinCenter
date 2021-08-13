from typing import Counter
import requests

import time
from datetime import datetime, timedelta

from requests.models import Response

print("Starting search for Covid vaccine slots!")

a=int(input("enter age :"))
p=input("entter your pin code :")
print_f = 'Y'
numdays = 3

actual = datetime.today()

fo_d=[actual + timedelta(days=i) for i in range(numdays)]
#print(fo_d)

actual_date=[i.strftime("%d%m%y") for i in fo_d]
#print(actual_date)

while True:
    counter=0

    for d in actual_date:
        url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(p,d) 
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
            
        result = requests.get(url, headers=header)

        if result.ok:
            Response_json=result.json()
            if Response_json["centers"]:
                if(print_f.lower()=='y'):
                    for center in Response_json["centers"]:
                            for session in center["sessions"]:
                                if (session["min_age_limit"] <= a and session["available_capacity"] > 0 ) :
                                    print('Pincode: ' + p)
                                    print("Available on: {}".format(d))
                                    print("\t", center["name"])
                                    print('\t', center['address'])
                                    print("\t", center["block_name"])
                                    print("\t Price: ", center["fee_type"])
                                    print("\t Availablity : ", session["available_capacity"])

                                    if(session["vaccine"] != ''):
                                        print("\t Vaccine type: ", session["vaccine"])
                                    print("\n")
                                    counter = counter + 1
            else:
                print("No Response!")
                
    if counter==0:
        print("No Vaccination slot available!")
    else:
        print("Search Completed!")

    dt = datetime.now() + timedelta(minutes=2)

    while datetime.now() < dt:
        time.sleep(1)