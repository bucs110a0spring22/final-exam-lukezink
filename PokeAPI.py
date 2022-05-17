import requests

class PokeAPI:

  def __init__(self, numbid=1):
    self.api_url = 'https://pokeapi.co/api/v2/pokemon/'+str(numbid)

  def __str__(self):
    print ("This is PokeAPI with URL: https://pokeapi.co/api/v2/pokemon/")
    

  def getName(self):
    """
    Returns the name of the pokemon
    Takes self
    Returns name as string
    """
    info = requests.get(self.api_url).json()
    return info['name']

  def getWeight(self):
    """
    Gets the weight of pokemon in pounds.
    Takes self
    Returns weight as float
    """
    info = requests.get(self.api_url).json()
    pounds = info['weight']*0.220462
    return pounds