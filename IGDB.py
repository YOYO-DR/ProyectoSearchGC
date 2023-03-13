import requests
from googletrans import Translator

url = 'https://id.twitch.tv/oauth2/token'
data = {'client_id': 'drp1kpogy07hyf63pczg0rrwssytyh', 'client_secret': 'gej0e3fzqrs1kzkj5zf89gfiu2pgcr','grant_type':'client_credentials'}

response = requests.post(url, data=data)

print(response.json()['access_token'])

#

api_key = response.json()['access_token']

url = 'https://api.igdb.com/v4/games'

headers = {
    'Client-ID': 'drp1kpogy07hyf63pczg0rrwssytyh',
    'Authorization': f'Bearer {api_key}'
}
#id, nombre y descripcion
while True:
  print('------------------------')
  juegoBusqueda=input('\nIngresa el nombre del juego a buscar: ')
  data = f'fields name, summary, total_rating_count, total_rating; limit 10; search "{juegoBusqueda}";'
  response = requests.post(url, headers=headers, data=data)

  traductor=Translator()
  if len(response.json())!=0:
    for i in response.json():
      print('------------------------')
      for clave,valor in i.items():
        if clave=='summary':
          descri=traductor.translate(str(valor),dest='es').text
          print('descripcion:',descri)
          continue
        print(f'{clave}: {valor}')

  else:
    print(f'El juego {juegoBusqueda} no se pudo encontrar')
