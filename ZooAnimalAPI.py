import requests

class ZooAnimalAPI:

  def __init__(self):
    self.api_url = 'https://zoo-animal-api.herokuapp.com/animals/rand'
    
  def getInfo(self):
    rawdata = requests.get(self.api_url).json()
    minweight = rawdata['weight_min']
    maxweight = rawdata['weight_max']
    avgweight = (float(minweight)+float(maxweight))/2.0
    info = [rawdata['name'],avgweight,rawdata['image_link']]
    return info