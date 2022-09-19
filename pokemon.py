# -*- coding: utf-8 -*-

import numpy as np

class Type :
  def __init__(self, index, nom, faiblesse) :
    self.index = index
    self.nom = nom
    self.faiblesse = faiblesse

  def __repr__(self) :
    return "Index : % s, Nom : % s, Faiblesse : % s" % (self.index, self.nom, self.faiblesse)

#TYPES

Feu = Type(0, "feu", 1)
#Feu.__repr__()

Eau = Type(1, "eau", 2)
#Eau.__repr__()

Electrique = Type(2, "electrique", 0)
#Electrique.__repr__()

i = Feu.index
j = Eau.index
k = Electrique.index
types = np.array([i, j, k])
#print(types)

class Pokemon :
  def __init__(self, p_type, nom, pdv, attaques, faiblesse) :
    max_type_number = len(types)
    if (p_type < 0 or p_type >= max_type_number) :
      self.p_type = 0
    #print(types[p_type])
    self.p_type = types[p_type]
    self.nom = nom
    self.pdv = pdv
    self.attaques = attaques
    self.faiblesse = faiblesse

  def __repr__(self) :
    return "Type : % s, Nom : % s, Points de vie : % s, Attaques : % s, Faiblesse : % s" % (self.p_type, self.nom, self.pdv, self.attaques, self.faiblesse)

class Attaque :
  def __init__(self, a_type, nom, pdv) :
    self.a_type = a_type
    self.nom = nom
    self.pdv = pdv

  def __repr__(self) :
    return "Type : % s, Nom : % s, Points de vie : %s" % (self.a_type, self.nom, self.pdv)

#ATTAQUES

Lance_Flammes = Attaque(0, 'Lance-Flammes', 50)
#Lance_Flammes.__repr__()

Dracogriffe = Attaque(0, 'Dracogriffe', 40)
#Dracogriffe.__repr__()

Double_canon = Attaque(1, 'Double-Canon', 45)
#Double_canon.__repr__()

Hydroqueue = Attaque(1, 'Hydroqueue', 35)
#Hydroqueue.__repr__()

Eclair = Attaque(2, 'Éclair', 20)
#Eclair.__repr__()

Tonnerre = Attaque(2, 'Tonnerre', 40)
#Tonnerre.__repr__()

#POKEMONS

Dracofeu = Pokemon(0, 'Dracofeu', 120, [Lance_Flammes, Dracogriffe], 1)
#Dracofeu.__repr__()

Tortank = Pokemon(1, 'Tortank', 130, [Double_canon, Hydroqueue], 2)
#Tortank.__repr__()

Pikachu = Pokemon(2, 'Pikachu', 100, [Eclair, Tonnerre], 0)
#Pikachu.__repr__()

class P_Attaque :
  def __init__(self, attaque, pokemon) :
    self.attaque = attaque
    p = pokemon.faiblesse
    pdvA = self.attaque.pdv
    if (self.attaque.a_type == p) :
      pdvA *= 1.2
      print('Vous attaquez votre adversaire sur sa faiblesse ! La puissance de votre attaque est augmentée de 20%.')
    pdvA = int(pdvA)
    pokemon.pdv = pokemon.pdv - pdvA
    print('Points de vie de  % s : %s' % (pokemon.nom, pokemon.pdv))

class Match :
  def __init__(self, pokemonA, pokemonB) :
    pdvA = pokemonA.pdv
    pdvB = pokemonB.pdv
    print('Que le match entre ' + pokemonA.nom + ' et ' + pokemonB.nom + ' commence !')
    print('% s a % s points de vie.' % (pokemonA.nom, pokemonA.pdv))
    print('% s a % s points de vie.' % (pokemonB.nom, pokemonB.pdv))
    counter = 1
    while (pokemonA.pdv > 0 and pokemonB.pdv > 0) :
      if (counter % 2 == 1) :
        p_turn = pokemonA
        p_att = pokemonB
      else :
        p_turn = pokemonB
        p_att = pokemonA
      print('Au tour de ' + p_turn.nom + ' !')
      print('Attaques de ' + p_turn.nom + ' : ')
      i = 0
      while (i < len(p_turn.attaques)) :
        print('% s : %s' % (i, p_turn.attaques[i]))
        i += 1
      nbAttaque = int(input('Entrez le nombre équivalent à l\'attaque choisie : '))
      if (nbAttaque < 0 or nbAttaque >= len(p_turn.attaques)) :
        nbAttaque = 0
      attaqueChoisie = p_turn.attaques[nbAttaque]
      print(attaqueChoisie)
      P_Attaque(attaqueChoisie, p_att)
      counter += 1
    if (pokemonA.pdv > pokemonB.pdv) :
      vainqueur = pokemonA
      print(pokemonA.nom + ' gagne !')
    elif (pokemonA.pdv == pokemonB.pdv) :
      vainqueur = 0
      print('Euuuh... quelque chose s\'est mal passé')
    else :
      vainqueur = pokemonB
      print(pokemonB.nom + ' gagne !')
    pokemonA.pdv = pdvA
    pokemonB.pdv = pdvB

Match(Pikachu, Tortank)