import time
import random
import sys
import gc


def appendAll(className, array):
  for obj in gc.get_objects():
    if (isinstance(obj, className)):
      array.append(obj)


class Type:
  def __init__(self, index, name, weakness):
    self.index = index
    self.name = name
    self.weakness = weakness
    return None

  def __repr__(self):
    return "Index: % s, Name: % s, Weakness: % s" % (self.index, self.name, self.weakness)

Fire = Type(0, "Fire", "Water")
Water = Type(1, "Water", "Electric")
Electric = Type(2, "Electric", "Fire")

types = []
appendAll(Type, types)

class Creature:
  def __init__(self, c_type, name, life_points, attacks):
    max_type_number = len(types)
    if (c_type < 0 or c_type >= max_type_number):
      c_type = 0
    self.c_type = types[c_type]
    self.name = name
    self.life_points = life_points
    self.attacks = attacks
    return None

  def __repr__(self):
    return "Type: % s, Name: % s, Life Points: % s, Attacks: % s" % (self.c_type, self.name, self.life_points, self.attacks)

class Attack:
  def __init__(self, a_type, name, life_points):
    max_type_number = len(types)
    if (a_type < 0 or a_type >= max_type_number):
      a_type = 0
    self.a_type = types[a_type]
    self.name = name
    self.life_points = life_points
    return None

  def __repr__(self) :
    return "Type: % s, Name: % s, Life Points: % s" % (self.a_type, self.name, self.life_points)


#ATTACKS:

Flame_Avalanche = Attack(0, 'Flame Avalanche', 50)
Fire_Hug = Attack(0, 'Fire Hug', 40)
Whale_Headbump = Attack(1, 'Whale Headbump', 45)
Shark_Bite = Attack(1, 'Shark Bite', 45)
IEM_Slap = Attack(2, 'IEM Slap', 33)
Thunderoar = Attack(2, 'Thunderoar', 40)

attacks_list = []
appendAll(Attack, attacks_list)


#CREATURES:

DragonDad = Creature(0, 'DragonDad', 128, [Flame_Avalanche, Fire_Hug])
Poseideamon = Creature(1, 'Poseideamon', 130, [Whale_Headbump, Shark_Bite])
Teslabott = Creature(2, 'Teslabott', 140, [IEM_Slap, Thunderoar])

creatures_list = []
appendAll(Creature, creatures_list)


#MATCH: (definition)

def available_creatures(creatureA=None):
  print('\nAvailable Creatures:\n')
  i = 0
  while (i < len(creatures_list)):
    if (creatureA == None or creatures_list[i] != creatureA) :
      print('% s : % s, Life Points: % s, Type: % s, Weakness: % s' % (i, creatures_list[i].name, creatures_list[i].life_points, creatures_list[i].c_type.name, creatures_list[i].c_type.weakness))
    i += 1
  return None

def get_creature(given_input):
  try:
    creature = raw_input(given_input)
    creature = ord(creature[0]) - 48
  except Exception:
    creature = 0
  if (creature < 0 or creature >= len(creatures_list)) :
    creature = 0
  return creature

class Choice_Creatures:
  def __init__(self):
    print('\nFirst Creature:')
    available_creatures()
    cA = get_creature('\nNumber of the first Creature: ')
    print('\nYou chose % s!' % (creatures_list[cA].name))
    time.sleep(0.7)
    print('\nSecond Creature:')
    available_creatures(creatures_list[cA])
    cB = get_creature('\nNumber of the second creature: ')
    if (cA == cB):
      if (cA > 0):
        cB -= 1
      else:
        cB += 1
    print('\nYou chose % s!' % (creatures_list[cB].name))
    time.sleep(0.7)
    self.creatureA = creatures_list[cA]
    self.creatureB = creatures_list[cB]
    return None

  def __repr__(self):
    return "First Creature: % s, second Creature: % s" % (self.creatureA, self.creatureB)


def start(creatureA, creatureB):
  print('\nLet the match between ' + creatureA.name + ' and ' + creatureB.name + ' begin!').upper()
  time.sleep(1.4)
  print('\n% s has % s Life Points.' % (creatureA.name, creatureA.life_points))
  time.sleep(0.7)
  print('% s has % s Life Points.' % (creatureB.name, creatureB.life_points))
  time.sleep(0.7)
  return None


def creature_attack(attack, creature):
  life_pointsA = attack.life_points
  if (attack.a_type.name == creature.c_type.weakness):
    life_pointsA *= 1.2
    print('\nYou attack your opponent on his weakness! The power of your attack is increased by 20%.')
    time.sleep(0.8)
  life_pointsA = int(life_pointsA)
  creature.life_points = creature.life_points - life_pointsA
  if (creature.life_points < 0):
    creature.life_points = 0
  print('\nLife Points of % s: % s' % (creature.name, creature.life_points))
  time.sleep(0.6)
  return None


def turn_(counter, creatureA, creatureB):
  if (counter % 2 == 1) :
    c_turn = creatureA
    c_att = creatureB
  else:
    c_turn = creatureB
    c_att = creatureA
  turn = c_turn
  att = c_att
  print('\nIT\'S ' + c_turn.name.upper() + '\'S TURN!')
  time.sleep(0.6)
  print('\n' + c_turn.name + '\'s attacks: \n')
  time.sleep(0.6)
  i = 0
  while (i < len(c_turn.attacks)):
    print('% s: % s, Type: % s, Damages: % s' % (i, c_turn.attacks[i].name, c_turn.attacks[i].a_type.name, c_turn.attacks[i].life_points))
    i += 1
  try:
    nbAttack = raw_input('\nEnter the number associated with the chosen attack: ')
    nbAttack = ord(nbAttack[0]) - 48
  except Exception:
    nbAttack = 0
  if (nbAttack < 0 or nbAttack >= len(c_turn.attacks)):
    nbAttack = 0
  chosen_attack = c_turn.attacks[nbAttack]
  print('\n% s uses % s!' % (c_turn.name, chosen_attack.name))
  time.sleep(0.6)
  creature_attack(chosen_attack, c_att)
  return None


def turn_computer(counter, creatureA, creatureB):
  c_turn = creatureB
  c_att = creatureA
  time.sleep(0.2)
  print('\nIT\'S ' + c_turn.name.upper() + '\'S TURN!')
  time.sleep(0.6)
  chosen_attack = c_turn.attacks[random.randint(0, len(c_turn.attacks) - 1)]
  print('\n% s uses % s!' % (c_turn.name, chosen_attack.name))
  time.sleep(0.6)
  creature_attack(chosen_attack, c_att)
  return None


class Result:
  def __init__(self, creatureA, creatureB):
    if (creatureA.life_points > creatureB.life_points):
      self.winner = creatureA
      print('\n' + creatureA.name.upper() + ' WINS!')
    elif (creatureA.life_points == creatureB.life_points):
      self.winner = 0
      print('\nWell... Something went wrong.')
    else:
      self.winner = creatureB
      print('\n' + creatureB.name.upper() + ' WINS!')
    return None

  def __repr__(self):
    return "% s" % (self.winner) if creatureA.life_points > creatureB.life_points or creatureB.life_points > creatureA.life_points else None


def new_match(creatureA, creatureB, Computer=None):
  print('\nWhat do you want to do?')
  print('\n0 : New match - same Creatures!') 
  print('1 : New match - inversed Creatures!')
  print('2 : New match - new Creatures!')
  print('3 : Go to the main menu')
  print('4 : Quit the game')
  try:
    nbQuestion = raw_input('\nEnter the desired value: ')
    nbQuestion = ord(nbQuestion[0]) - 48
  except Exception:
    new_match(creatureA, creatureB, Computer=1) if Computer == 1 else new_match(creatureA, creatureB)
  if (nbQuestion == 0):
    if (Computer == 1):
      Match(creatureA, creatureB, Computer=1)
      return None
    Match(creatureA, creatureB)
  elif (nbQuestion == 1):
    if (Computer == 1):
      Match(creatureB, creatureA, Computer=1)
      return None
    Match(creatureB, creatureA)
  elif (nbQuestion == 2):
    if (Computer == 1):
      Match(Computer=1)
      return None
    Match()
  elif (nbQuestion == 4):
    print('\nSee you soon!\n')
    return None
  else:
    menu()
  return None


class Match:
  def __init__(self, creatureA=None, creatureB=None, Computer=None):
    if (creatureA == None):
      crea = Choice_Creatures()
      creatureA = crea.creatureA
      creatureB = crea.creatureB
    life_pointsA = creatureA.life_points
    life_pointsB = creatureB.life_points
    start(creatureA, creatureB)
    self.counter = 1
    while (creatureA.life_points > 0 and creatureB.life_points > 0):
      if (Computer == None or Computer != 1):
        turn_(self.counter, creatureA, creatureB)
      else:
        if (self.counter % 2 == 1):
          turn_(self.counter, creatureA, creatureB)
        else:
          turn_computer(self.counter, creatureA, creatureB)
      self.counter += 1
    self.result = Result(creatureA, creatureB)
    creatureA.life_points = life_pointsA
    creatureB.life_points = life_pointsB
    if (Computer == None):
      new_match(creatureA, creatureB)
    else:
      new_match(creatureA, creatureB, Computer=1)
    return None

  def __counter(self):
    return self.counter

  def __result(self):
    return self.result.__repr__()



#MAIN MENU:

def menu(value=None):
  if (value == None):
    print('\n\n\nCREATURES\' FIGHT')
    print('\nMain Menu')
    print('\n0 : Fight - and control both Creatures')
    print('1 : Fight - and play against the computer')
    print('2 : Game introduction')
    print('3 : Quit the game')
    try:
      value = raw_input('\nEnter the value assigned to the desired action: ')
      value = ord(value[0]) - 48
    except Exception:
      menu()
  if (value == 0):
    Match()
  elif (value == 1):
    Match(Computer=1)
  elif (value == 2):
    introduction()
  elif (value == 3):
    print('\nSee you soon!\n')
  else: 
    menu()
  return None


#GAME INTRODUCTION:

def introduction():
  print('\n\nGame introduction:')
  print('\nIn this game, you can play a fight between two Creatures. You can choose each Creature after indicating your desired game mode.')
  print('\nAfter each fight, you will be able to replay, keeping the same combat options or changing them.')
  try:
    x = raw_input('\nPress Enter to return to the main menu : ')
  except Exception:
    x = 0
  menu()
  return None


#CHECK_ARGV:

def check_argv():
  if (len(sys.argv) > 1):
    v = ord(sys.argv[1][0]) - 48
    if (v >= 0 and v <= 4):
      menu(v)
      return None
  menu()
  return None


#GAME:

Main = check_argv()
