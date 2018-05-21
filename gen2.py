
# coding: utf-8

# In[7]:


import urllib.request
import json
import urllib.parse
import random

tenant = "***"
user = "admin@" + tenant
password = '***'


group_template = 'fibgroup_a'


import ssl
import aiohttp

def get_session():
    context = ssl.create_default_context()
    # use only TLSv1_2 and higher
    context.options |= ssl.OP_NO_TLSv1
    context.options |= ssl.OP_NO_TLSv1_1

    session = aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl_context=context, force_close=True, enable_cleanup_closed=True),
        cookie_jar=aiohttp.DummyCookieJar()
    )
    return session

def token():
    
    url = 'https://login.windows.net/' + tenant + '/oauth2/token?api-version=1.0'

    data = urllib.parse.urlencode(
      {
            'username': user,
            'password': password,
            'grant_type': 'password' ,
            'client_id':'04b07795-8ddb-461a-bbee-02f9e1bf7b46',
            'resource': 'https://graph.microsoft.com/'        
        }
    ).encode('utf-8')

    req = urllib.request.Request(url, data = data)

    res = urllib.request.urlopen(req)

    return json.loads( res.read().decode() )['access_token'] 



def post(entity, token, body):
    
    print('_', end=' ')
    #print(body)
    
    api = 'https://graph.microsoft.com/beta/' + entity
    
    headers = { 
        'Authorization' : 'Bearer ' + token,
        'Content-Type' : 'application/json'
        }

    req = urllib.request.Request(api, data = json.dumps(body).encode('utf8'), headers = headers)
    res = urllib.request.urlopen(req)
    
    print('.', end=' ')
        
    id = ''
    
    try:
    
        id = json.loads(res.read())['id']
    
    except Exception as e:
        pass
    
    
    res.close()
    return id

iso = {"BD": "AS", "BE": "EU", "BF": "AF", "BG": "EU", "BA": "EU", "BB": "NA", "WF": "OC", "BL": "NA", "BM": "NA", "BN": "AS",
       "BO": "SA", "BH": "AS", "BI": "AF", "BJ": "AF", "BT": "AS", "JM": "NA", "BV": "AN", "BW": "AF", "WS": "OC", "BQ": "NA",
       "BR": "SA", "BS": "NA", "JE": "EU", "BY": "EU", "BZ": "NA", "RU": "EU", "RW": "AF", "RS": "EU", "TL": "OC", "RE": "AF",
       "TM": "AS", "TJ": "AS", "RO": "EU", "TK": "OC", "GW": "AF", "GU": "OC", "GT": "NA", "GS": "AN", "GR": "EU", "GQ": "AF",
       "GP": "NA", "JP": "AS", "GY": "SA", "GG": "EU", "GF": "SA", "GE": "AS", "GD": "NA", "GB": "EU", "GA": "AF", "SV": "NA",
       "GN": "AF", "GM": "AF", "GL": "NA", "GI": "EU", "GH": "AF", "OM": "AS", "TN": "AF", "JO": "AS", "HR": "EU", "HT": "NA",
       "HU": "EU", "HK": "AS", "HN": "NA", "HM": "AN", "VE": "SA", "PR": "NA", "PS": "AS", "PW": "OC", "PT": "EU", "SJ": "EU",
       "PY": "SA", "IQ": "AS", "PA": "NA", "PF": "OC", "PG": "OC", "PE": "SA", "PK": "AS", "PH": "AS", "PN": "OC", "PL": "EU",
       "PM": "NA", "ZM": "AF", "EH": "AF", "EE": "EU", "EG": "AF", "ZA": "AF", "EC": "SA", "IT": "EU", "VN": "AS", "SB": "OC",
       "ET": "AF", "SO": "AF", "ZW": "AF", "SA": "AS", "ES": "EU", "ER": "AF", "ME": "EU", "MD": "EU", "MG": "AF", "MF": "NA",
       "MA": "AF", "MC": "EU", "UZ": "AS", "MM": "AS", "ML": "AF", "MO": "AS", "MN": "AS", "MH": "OC", "MK": "EU", "MU": "AF",
       "MT": "EU", "MW": "AF", "MV": "AS", "MQ": "NA", "MP": "OC", "MS": "NA", "MR": "AF", "IM": "EU", "UG": "AF", "TZ": "AF",
       "MY": "AS", "MX": "NA", "IL": "AS", "FR": "EU", "IO": "AS", "SH": "AF", "FI": "EU", "FJ": "OC", "FK": "SA", "FM": "OC",
       "FO": "EU", "NI": "NA", "NL": "EU", "NO": "EU", "NA": "AF", "VU": "OC", "NC": "OC", "NE": "AF", "NF": "OC", "NG": "AF",
       "NZ": "OC", "NP": "AS", "NR": "OC", "NU": "OC", "CK": "OC", "XK": "EU", "CI": "AF", "CH": "EU", "CO": "SA", "CN": "AS",
       "CM": "AF", "CL": "SA", "CC": "AS", "CA": "NA", "CG": "AF", "CF": "AF", "CD": "AF", "CZ": "EU", "CY": "EU", "CX": "AS",
       "CR": "NA", "CW": "NA", "CV": "AF", "CU": "NA", "SZ": "AF", "SY": "AS", "SX": "NA", "KG": "AS", "KE": "AF", "SS": "AF",
       "SR": "SA", "KI": "OC", "KH": "AS", "KN": "NA", "KM": "AF", "ST": "AF", "SK": "EU", "KR": "AS", "SI": "EU", "KP": "AS",
       "KW": "AS", "SN": "AF", "SM": "EU", "SL": "AF", "SC": "AF", "KZ": "AS", "KY": "NA", "SG": "AS", "SE": "EU", "SD": "AF",
       "DO": "NA", "DM": "NA", "DJ": "AF", "DK": "EU", "VG": "NA", "DE": "EU", "YE": "AS", "DZ": "AF", "US": "NA", "UY": "SA",
       "YT": "AF", "UM": "OC", "LB": "AS", "LC": "NA", "LA": "AS", "TV": "OC", "TW": "AS", "TT": "NA", "TR": "AS", "LK": "AS",
       "LI": "EU", "LV": "EU", "TO": "OC", "LT": "EU", "LU": "EU", "LR": "AF", "LS": "AF", "TH": "AS", "TF": "AN", "TG": "AF",
       "TD": "AF", "TC": "NA", "LY": "AF", "VA": "EU", "VC": "NA", "AE": "AS", "AD": "EU", "AG": "NA", "AF": "AS", "AI": "NA",
       "VI": "NA", "IS": "EU", "IR": "AS", "AM": "AS", "AL": "EU", "AO": "AF", "AQ": "AN", "AS": "OC", "AR": "SA", "AU": "OC",
       "AT": "EU", "AW": "NA", "IN": "AS", "AX": "EU", "AZ": "AS", "IE": "EU", "ID": "AS", "UA": "EU", "QA": "AS", "MZ": "AF"}

jtitles = ['Software Engineer',
    'Numerical Control Programmer',
    'Consulting Director, Quant Developer',
    'Software Engineer Intern',
    'Software Engineer (Full Stack), Web',
    'Software Engineer, WhatsApp Intern/Co-op',
    'Entry-Level Software Engineer',
    'Data Engineer',
    'Research Assistant',
    'Social Science/Humanities Research',
    'Research Analyst (Data Science)',
    'Clinical Research Assistant',
    'Research and Evaluation Assistant',
    'Associate Professor',
    'Behavioral Research Fellow']

country = [key for key in iso]

def gen(o):
    name = o['login']['username']
    c = random.choice(country)

    return {
        "accountEnabled": True,
        "displayName": o['name']['first'] + ' ' + o['name']['last'],
        "mailNickname": name,
        "userPrincipalName": name + '@' + tenant,
        "passwordProfile" : {
            "forceChangePasswordNextSignIn": True,
            "password": "Unique10"
            } ,
        "city": o['location']['city'],    
        "department": "IT",     
        "jobTitle": random.choice(jtitles),
        "employeeId": o['id']['value'],
        "givenName": o['name']['first'],
        "mobilePhone": o['cell'],
        "officeLocation": o['location']['city'],
        "postalCode": str(o['location']['postcode']),
##           "preferredDataLocation": c,
##           "preferredLanguage": c,
##           "usageLocation": c,
        "country": c,
        "state": o['location']['state'],
        "streetAddress": o['location']['street'],
        "surname": o['name']['last'],
        "businessPhones": [o['phone']]    
    }

def gen1(name):
    return {
      "description": "performance test Fibonacci sized groups",
      "displayName": name,  
      "mailEnabled": True,
      "mailNickname": name,
      "securityEnabled": False,
      "groupTypes": [
          "Unified"
          ]    
    }

def process(results, token, i):
    
    a = 1
    b = 1

    ids = []
    
    for o in results:
#        try:        
            body = gen(o)

            #print('.')

            id = post('users', token, body)        

            ids.append(id)

            if(len(ids) == a + b):            
                a = b
                b = len(ids)
                print(b,end=' ')
                body = gen1('%s%i_%i' % (group_template, i,len(ids)))
                
                group_id = post('groups', token, body)

                for id in ids:
                    body = {
                      '@odata.id': 'https://graph.microsoft.com/beta/directoryObjects/' + id
                    }

                    post('groups/' + group_id + '/members/$ref', token, body)
                print('+', end=' ')

#        except Exception as e:
#            print(e)


page = 1000

for i in range(3):

    res1 = urllib.request.urlopen('https://randomuser.me/api/?results=%i' % page)

    results = json.loads(res1.read())['results']

    process(results, token(), i)
    
    print('.', end=' ')


