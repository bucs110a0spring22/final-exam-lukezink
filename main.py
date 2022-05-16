import PokeAPI
import ZooAnimalAPI
import random

def fight(aniname,aniweight,pokename,pokeweight):
  if (aniweight > pokeweight):
    statcalc = (aniweight-pokeweight)/aniweight
    if statcalc < 0.5:
      result = (1-statcalc)*100
    else:
      result = statcalc*100
    return (aniname+" has a "+str(result)+"% chance of winning!")
  elif (aniweight < pokeweight):
    statcalc = (pokeweight-aniweight)/pokeweight
    if statcalc < 0.5:
      result = (1-statcalc)*100
    else:
      result = statcalc*100
    return (pokename+" has a "+str(result)+"% chance of winning!")
  

def main(): 
  randid = random.randrange(1,809)
  pokemon = PokeAPI.PokeAPI(randid)
  pokename = pokemon.getName()
  pokeweight = pokemon.getWeight()
  animal = ZooAnimalAPI.ZooAnimalAPI()
  aniinfo = animal.getInfo()
  aniname = aniinfo[0]
  aniweight = aniinfo[1]
  print("The pokemon selected is: "+ pokename)
  print(pokename+" weighs about "+str(round(pokeweight))+" lbs.")
  print("The animal selected is: "+ aniname)
  print(aniname+" weighs about "+str(round(aniweight))+" lbs.")
  result = fight(aniname,aniweight,pokename,pokeweight)
  print(result)
main()