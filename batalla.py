import random

#Ingresar HPs
psj1 = int(input("HP personaje 1: "))
psj2 = int(input("HP personaje 2: "))

dmg = 10
#Ingresar prob esquivar
dodge1 = float(input("Dodge personaje 1: "))
dodge2 = float(input("Dodge personaje 2: "))

rnd = random.random()

while psj1>0 and psj2>0:

  #Ataca personaje 1
  crit = random.random()
  damage = crit*dmg
  #Esquiva personaje 2
  dodge = random.random()
  if(dodge<0.5):
    psj2-=damage

  #Ataca personaje 2
  crit = random.random()
  damage = crit*dmg
  #Esquiva personaje 1
  dodge = random.random()
  if(dodge<0.5):
    psj1-=damage
  
if psj1 > 0:
  print("Gana personaje 1")
if psj2 > 0:
  print("Gana personaje 2")
