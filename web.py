import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import json
def xml_parse():
    data = '''<person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''

    tree = ET.fromstring(data)
    print('Name:', tree.find('name').text)
    print('Attr:', tree.find('email').get('hide'))

xml_parse()

def xml_parse2():
    input = '''<stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>'''
    stuff = ET.fromstring(input)
    lst = stuff.findall('users/user')
    print('User count:', len(lst))
    for item in lst:
        print('Name', item.find('name').text)
        print('Id', item.find('id').text)
        print('Attribute', item.get("x"))

xml_parse2()

def json_parse():
    data = '''
        [
            { "id" : "001",
                "x" : "2",
                "name" : "Quincy"
            } ,
            { "id" : "009",
                "x" : "7",
                "name" : "Mrugesh"
            }
        ]
    '''
    info = json.loads(data)
    print(info[1]['name'])

json_parse()

def google_maps():
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
    while True:
        address = input('Enter location:')
        if len(address) < 1: break
        url = serviceurl + urllib.parse.urlencode({'address': address})
        print('Retrieving', url)
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')
        try:
            js = json.loads(data)
        except:
            js = None
        if not js or 'status' not in js or js['status'] !='OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        print('lat', lat, 'lng', lng)
        location = js['results'][0]['formatted_address']
        print(location)

google_maps()