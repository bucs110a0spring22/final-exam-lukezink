import requests

class PokeAPI:

  def __init__(self, numbid=1):
    self.api_url = 'https://pokeapi.co/api/v2/pokemon/'+str(numbid)

  def getName(self):
    info = requests.get(self.api_url).json()
    return info['name']

  def getWeight(self):
    info = requests.get(self.api_url).json()
    pounds = info['weight']*0.220462
    return pounds