import requests

print("SOLICITANDO INFORMACION DE INTERNET")
print("espere....") 
url= 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
data=requests.get(url)

if data.status_code==200:
    data = data.json()
    for e in data:
        print(e['id'])
        print(e['fec_alta'])
        print(e['user_name'])
        print(e['codigo_zip'])
        print(e['cantidad_compras_realizadas'])
        
