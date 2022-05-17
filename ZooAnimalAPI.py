import requests

class ZooAnimalAPI:

  def __init__(self):
    self.api_url = 'https://zoo-animal-api.herokuapp.com/animals/rand'

  def __str__(self):
    print ("This is ZooAnimalAPI with URL: https://zoo-animal-api.herokuapp.com/animals/rand/")
    
  def getInfo(self):
    '''
    Gets the name and weight of a random animal
    Takes self
    Returns name and weight as string and float respectively
    '''
    rawdata = requests.get(self.api_url).json()
    minweight = rawdata['weight_min']
    maxweight = rawdata['weight_max']
    avgweight = (float(minweight)+float(maxweight))/2.0
    info = [rawdata['name'],avgweight]
    return info