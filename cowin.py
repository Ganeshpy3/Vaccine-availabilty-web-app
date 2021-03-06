from bs4 import BeautifulSoup
import requests

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US'})
URL="https://cdn-api.co-vin.in/api/v2/admin/location/states"
webpage = requests.get(URL,headers=HEADERS)
state_soup = BeautifulSoup(webpage.content, "lxml")
state_values=state_soup.text
state_val=state_values.split("{")

def split_state(val):
    j = 0
    lst = []
    for i in val[2:]:
        if j < len(val[2:]) - 1:
            j = j + 1
            lst.append(eval("{" + i[:-1]))
        else:
            lst.append(eval("{" + i[:-11]))
    return lst

def split_district(states):
    state_dist = {}
    dist_dist = {}
    for i in states:
        inp = states[i]
        url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/" + str(inp)
        webpage1 = requests.get(url, headers=HEADERS)
        soup1 = BeautifulSoup(webpage1.content, "lxml")
        dist_value = soup1.text
        dist_val1 = dist_value.split("{")
        dist_lst = []
        y = 0
        for j in dist_val1[2:]:
            if y < len(dist_val1[2:]) - 1:
                y = y + 1
                val0 = "{" + j
                dist_lst.append(eval(val0[:-1]))
            else:
                val0 = "{" + j
                dist_lst.append(eval(val0[:-11]))
        new_lst = []
        for k in dist_lst:
            dist_dist[k["district_name"]] = k["district_id"]
            new_lst.append(k["district_name"])
        state_dist[i] = new_lst
    return dist_dist

def states_dic():
    states = {}
    lst=split_state(state_val)

    for i in lst:
        states[i["state_name"]] = i["state_id"]
    return split_district(states)
dist_dic=states_dic()



district=input("Enter district")
districtval=str(dist_dic[district])
date=input("Enter date")
URL="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+districtval+"&date="+date
HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US'})
webpage = requests.get(URL,headers=HEADERS)
district_soup = BeautifulSoup(webpage.content, "lxml")
district_value=district_soup.text
val=district_value.split("{")
def append_list(dic_val):
    j = 0
    lst=[]
    for i in dic_val[2:]:
        if j < len(dic_val[2:])-1:
            j = j + 1
            val = "{" + i
            lst.append(eval(val[:-1]))

        else:
            val = "{" + i
            lst.append(eval(val[:-2]))

    return lst

def availability(data):
    lst=append_list(data)
availability(val)
