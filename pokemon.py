# -*- coding: utf-8 -*-

import time
import random

class Type :
  def __init__(self, index, nom, faiblesse) :
    self.index = index
    self.nom = nom
    self.faiblesse = faiblesse

  def __repr__(self) :
    return "Index : % s, Nom : % s, Faiblesse : % s" % (self.index, self.nom, self.faiblesse)

Feu = Type(0, "Feu", "Eau")
#Feu.__repr__()

Eau = Type(1, "Eau", "Electrique")
#Eau.__repr__()

Electrique = Type(2, "Electrique", "Feu")
#Electrique.__repr__()

types = [Feu, Eau, Electrique]

class Pokemon :
  def __init__(self, p_type, nom, pdv, attaques) :
    max_type_number = len(types)
    if (p_type < 0 or p_type >= max_type_number) :
      self.p_type = types[0]
    self.p_type = types[p_type]
    self.nom = nom
    self.pdv = pdv
    self.attaques = attaques

  def __repr__(self) :
    return "Type : % s, Nom : % s, Points de vie : % s, Attaques : % s, Faiblesse : % s" % (self.p_type, self.nom, self.pdv, self.attaques, self.faiblesse)

class Attaque :
  def __init__(self, a_type, nom, pdv) :
    max_type_number = len(types)
    if (a_type < 0 or a_type >= max_type_number) :
      self.a_type = types[0]
    self.a_type = types[a_type]
    self.nom = nom
    self.pdv = pdv

  def __repr__(self) :
    return "Type : % s, Nom : % s, Points de vie : % s" % (self.a_type, self.nom, self.pdv)


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

Dracofeu = Pokemon(0, 'Dracofeu', 120, [Lance_Flammes, Dracogriffe])
#Dracofeu.__repr__()

Tortank = Pokemon(1, 'Tortank', 130, [Double_canon, Hydroqueue])
#Tortank.__repr__()

Pikachu = Pokemon(2, 'Pikachu', 100, [Eclair, Tonnerre])
#Pikachu.__repr__()

pokemons_liste = [Dracofeu, Tortank, Pikachu]


#MATCH : définition

class PokemonsDispo :
  def __init__(self, pokemonA=None) :
    print('\nPokémons disponibles :\n')
    i = 0
    while (i < len(pokemons_liste)) :
      if (pokemonA == None or pokemons_liste[i] != pokemonA) :
        print('% s : % s, Points de vie : % s, Type : % s, Faiblesse : % s' % (i, pokemons_liste[i].nom, pokemons_liste[i].pdv, pokemons_liste[i].p_type.nom, pokemons_liste[i].p_type.faiblesse))
      i += 1

class ChoixPokemons :
  def __init__(self) :
    print('\nChoix du premier pokémon :')
    PokemonsDispo()
    pA = int(input('\nNuméro du premier pokemon : '))
    if (pA < 0 or pA >= len(pokemons_liste)) :
      pA = 0
    print('\nVous avez choisi % s !' % (pokemons_liste[pA].nom))
    time.sleep(0.5)
    print('\nChoix du second pokémon :')
    PokemonsDispo(pokemons_liste[pA])
    pB = int(input('\nNuméro du second pokémon : '))
    if (pB < 0 or pB >= len(pokemons_liste)) :
      pB = 0
    print('\nVous avez choisi % s.' % (pokemons_liste[pB].nom))
    time.sleep(0.5)
    self.pokemonA = pokemons_liste[pA]
    self.pokemonB = pokemons_liste[pB]

class Depart :
  def __init__(self, pokemonA, pokemonB) :
    print('\nQue le match entre ' + pokemonA.nom + ' et ' + pokemonB.nom + ' commence !')
    print('\n% s a % s points de vie.' % (pokemonA.nom, pokemonA.pdv))
    print('% s a % s points de vie.' % (pokemonB.nom, pokemonB.pdv))

class P_Attaque :
  def __init__(self, attaque, pokemon) :
    pdvA = attaque.pdv
    if (attaque.a_type.nom == pokemon.p_type.faiblesse) :
      pdvA *= 1.2
      print('\nVous attaquez votre adversaire sur sa faiblesse ! La puissance de votre attaque est augmentée de 20%.')
      time.sleep(0.4)
    pdvA = int(pdvA)
    pokemon.pdv = pokemon.pdv - pdvA
    print('\nPoints de vie de % s : % s' % (pokemon.nom, pokemon.pdv))
    time.sleep(0.5)

class Turn :
  def __init__(self, counter, pokemonA, pokemonB) :
      if (counter % 2 == 1) :
        p_turn = pokemonA
        p_att = pokemonB
      else :
        p_turn = pokemonB
        p_att = pokemonA
      print('\nAu tour de ' + p_turn.nom + ' !')
      time.sleep(0.4)
      print('\nAttaques de ' + p_turn.nom + ' : \n')
      time.sleep(0.4)
      i = 0
      while (i < len(p_turn.attaques)) :
        print('% s : % s, Type : % s, Dégâts : % s' % (i, p_turn.attaques[i].nom, p_turn.attaques[i].a_type.nom, p_turn.attaques[i].pdv))
        #print('% s : % s, Type : % s, Dégâts (en points de vie) : % s' % (i, p_turn.attaques[i].nom, p_turn.attaques[i].a_type.nom, p_turn.attaque[i].pdv))
        i += 1
      nbAttaque = int(input('\nEntrez le nombre associé à l\'attaque choisie : '))
      if (nbAttaque < 0 or nbAttaque >= len(p_turn.attaques)) :
        nbAttaque = 0
      attaqueChoisie = p_turn.attaques[nbAttaque]
      print('\n% s utilise % s !' % (p_turn.nom, attaqueChoisie.nom))
      time.sleep(0.4)
      P_Attaque(attaqueChoisie, p_att)

class TurnOrdi :
  def __init__(self, counter, pokemonA, pokemonB) :
      p_turn = pokemonB
      p_att = pokemonA
      time.sleep(0.4)
      print('\nAu tour de ' + p_turn.nom + ' !')
      time.sleep(1.5)
      attaqueChoisie = p_turn.attaques[random.randint(0, len(p_turn.attaques) - 1)]
      print('\n% s utilise % s !' % (p_turn.nom, attaqueChoisie.nom))
      time.sleep(0.8)
      P_Attaque(attaqueChoisie, p_att)

class Resultat :
  def __init__(self, pokemonA, pokemonB) :
    if (pokemonA.pdv > pokemonB.pdv) :
      vainqueur = pokemonA
      print('\n' + pokemonA.nom + ' gagne !')
    elif (pokemonA.pdv == pokemonB.pdv) :
      vainqueur = 0
      print('\nEuuuh... quelque chose s\'est mal passé.')
    else :
      vainqueur = pokemonB
      print('\n' + pokemonB.nom + ' gagne !')

class NouveauMatch :
  def __init__(self, pokemonA, pokemonB) :
    print('\nVoulez-vous faire un nouveau match ?')
    print('\n0 : Nouveau match - mêmes Pokémons !') 
    print('1 : Nouveau match - Pokémons inversés !')
    print('2 : Nouveau match - nouveaux Pokémons !')
    print('3 : Aller au menu principal')
    print('4 : Quitter le jeu')
    nbQuestion = int(input('\nEntrez la valeur désirée : '))
    if (nbQuestion == 0) :
      Match(pokemonA, pokemonB)
    elif (nbQuestion == 1) :
      Match(pokemonB, pokemonA)
    elif (nbQuestion == 2) :
      Match()
    elif (nbQuestion == 4) :
      print('\nÀ bientôt !\n')
    else :
      Menu()

class Match :
  def __init__(self, pokemonA=None, pokemonB=None, Ordi=None) :
    if (pokemonA == None) :
      pokes = ChoixPokemons()
      pokemonA = pokes.pokemonA
      pokemonB = pokes.pokemonB
    pdvA = pokemonA.pdv
    pdvB = pokemonB.pdv
    Depart(pokemonA, pokemonB)
    counter = 1
    while (pokemonA.pdv > 0 and pokemonB.pdv > 0) :
      if (Ordi == None or Ordi != 1) :
        Turn(counter, pokemonA, pokemonB)
      else :
        if (counter % 2 == 1) :
          Turn(counter, pokemonA, pokemonB)
        else :
          TurnOrdi(counter, pokemonA, pokemonB)
      counter += 1
    Resultat(pokemonA, pokemonB)
    pokemonA.pdv = pdvA
    pokemonB.pdv = pdvB
    NouveauMatch(pokemonA, pokemonB)


#MENU PRINCIPAL

class Menu :
  def __init__(self) :
    print('\n\n\nPOKEMON___SHELL')
    print('\nMenu Principal')
    print('\n0 : Combattre - et contrôler les deux pokemons')
    print('1 : Combattre - et jouer contre l\' ordinateur')
    print('2 : Introduction au jeu')
    print('3 : Quitter le jeu')
    valeur = input('\nEntrez la valeur correspondante à l\'action désirée : ')
    if (valeur == 0) :
      Match()
    elif (valeur == 1) :
      Match(Ordi=1)
    elif (valeur == 2) :
      Introduction()
    elif (valeur == 3) :
      print('\nÀ bientôt !\n')


#INTRODUCTION AU JEU

class Introduction() :
  def __init__(self) :
    print('\n\nIntroduction au jeu :')
    print('\nCe jeu émule un combat Pokémon. Vous pouvez choisir chaque Pokémon après avoir indiqué votre mode de jeu désiré.')
    print('\nAprès chaque combat, vous pourrez rejouer, en gardant les mêmes options de combat ou en les modifiant.')
    x = int(input('\nEntrez 0 pour revenir au menu principal : '))
    Menu()


#JEU :

Menu()
