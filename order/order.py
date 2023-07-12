import requests

URL = "http://127.0.0.1:8000"
PATH_COUNTRY = "/countries"
PATH_PROVINCES = "/provinces"
PATH_PROFESIONES = "/profesiones"

def order(conjunto):

    countries = [
        {
            "name": name_country, 
            "code_country": code_country
        }
        for name_country, code_country in zip(
            conjunto["NAIX_PAIS"], conjunto["CODI_NAIX_PAIS"]
        )
    ]

    provinces = [
        {
            "name": name_province,
            "code_province": code_province,
            "code_country": code_country
        }
        for name_province, code_province, code_country in zip(
            conjunto["NAIX_PROVINCIA"],
            conjunto["CODI_NAIX_PROVINCIA"],
            conjunto["CODI_NAIX_PAIS"],
        )
    ]

    profesiones = [
        {
            "code_number": code_number,
            "tipo_profesion": prof,
            "code_province": code_province
        }
        for code_number, prof, code_province in zip(conjunto.index, conjunto['NIVELL_INSTRUCCIO'], conjunto['CODI_NAIX_PROVINCIA'])
    ]

    for country in range(len(countries)):
        requests.post(f'{URL}{PATH_COUNTRY}', json=countries[country])
    for province in range(len(provinces)):
        requests.post(f'{URL}{PATH_PROVINCES}', json=provinces[province])
    for profesion in range(len(profesiones)):
        requests.post(f'{URL}{PATH_PROFESIONES}', json=profesiones[profesion])
