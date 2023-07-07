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
    } for p in range(len(conjunto))
    ]
    
    profesiones = [{
        "code_number": code_number[p],
        "tipo_profesion": prof[p],
        "code_province": code_province[p]
    }
        for p in range(len(conjunto))
    ]
    
    lista_country = []
    lista_province = []
    
    for c in range(len(country)):
        if country[c] not in lista_country:
            lista_country.append(country[c])
            requests.post(URL_COUNTRY, json=lista_country[c])
    for p in range(len(province)):
        if province[p] not in lista_province:
            lista_province.append(province[p])
            requests.post(URL_PROVINCES, json=lista_province[p])
    for p in range(len(profesiones)):
        requests.post(URL_PROFESIONES, json=profesiones[p])