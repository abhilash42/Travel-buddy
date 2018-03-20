import script
import requests
import os
# sending get request and saving the response as response object
#get request


# extracting data in json format


#print(data)
while 1:
    r = requests.get('http://167.99.34.239:8000/table1/')
    data = r.json()
    data1=str(data)
    print(data1)
    if data1 == '[]':
        print("hii")
        continue
    for i in data:
    #print(i)
        ch1=i['choice1']
        ch2=i['choice2']
        name=i['name']
        list1=[ch1,ch2,name]
        print(list1)
        break

# file2 is another python file jisme func is a function which returns a list
    list2=script.fn(list1)
    print("hello")
    print(list2)
    r=requests.delete('http://167.99.34.239:8000/table1/')
    print(r.status_code, r.reason)
    string = ",".join(list2)
    print(string)
    r=requests.post('http://167.99.34.239:8000/table2/', data={'rest_names':string})
    print(r.status_code, r.reason)
