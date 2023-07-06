import requests

URL_COUNTRY = 'http://127.0.0.1:8000/countries'
URL_PROVINCES = 'http://127.0.0.1:8000/provinces'
URL_PROFESIONES = 'http://127.0.0.1:8000/profesiones'

def order(conjunto):
    
    name_country = list(conjunto['NAIX_PAIS'])
    code_country = list(conjunto['CODI_NAIX_PAIS'])
    name_province = list(conjunto['NAIX_PROVINCIA'])
    code_province = list(conjunto['CODI_NAIX_PROVINCIA'])
    code_number = list(conjunto.index)
    prof = list(conjunto['NIVELL_INSTRUCCIO'])
        
    country = [{
        "name": name_country[c],
        "code_country": code_country[c]
    }
        for c in range(len(conjunto))
    ]
    
    province = [{
        "name": name_province[p],
        "code_province": code_province[p],
        "code_country": code_country[p]
    }
        for p in range(len(conjunto))
    ]
    
    profesiones = [{
        "code_number": code_number[p],
        "tipo_profesion": prof[p],
        "code_province": code_province[p]
    }
        for p in range(len(conjunto))
    ]
    
    for c in range(len(country)):
        response1 = requests.post(URL_COUNTRY, json=country[c])
    for p in range(len(province)):
        response2 = requests.post(URL_PROVINCES, json=province[p])
    for p in range(len(profesiones)):
        response3 = requests.post(URL_PROFESIONES, json=profesiones[p])