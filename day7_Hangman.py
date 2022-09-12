#!/usr/bin/python
# -*- coding: utf-8 -*-
HANGMAN = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
]

words = 'Alligator Ant Arctic wolf Badger Bald eagle Bat Bear Bee Beetle Black Blue whale Butterfly Camel Centipede Chicken Chimpanzee Clams Cockroach Coral Cormorant Cow Coyote Crab Crocodile Crow Deer Dog Dolphin Dove Dragonfly Ducks Elephant Elk Flamingo Fly Fox Frog Giraffe Goat Goose Gorilla Grasshopper Hare Hawk Hedgehog Hippopotamus Horse Jellyfish Kangaroo Koala Leopard Lion Lizard Lobster Louse Mole Monkey Mosquito Moth Mouse Octopus Ostrich Otter Owl Ox Panda Parrot Peacock Pelican Penguin Pig Pigeon Rabbit Raccoon Rat Raven Reindeer Robin Sea anemone Sea lion Sea turtle Sea urchin Seagull Seahorse Seal Shark Sheep Shells Shrimp Snake Sparrow Spider Squid Squirrel Starfish Stork Swallow Swan Tiger Toad Turkey Walrus Whale Woodpecker Worm'.split(
)
import random

# choose random word

word = random.choice(words).lower()
show = []
for letter in word:
    show += '_'

final = ''.join(show)
print("""
_ _ _ ____ _    ____ ____ _  _ ____    ___ ____    
| | | |___ |    |    |  | |\/| |___     |  |  |    
|_|_| |___ |___ |___ |__| |  | |___     |  |__|    
                                                   
      _  _ ____ _  _ ____ _  _ ____ _  _                 
      |__| |__| |\ | | __ |\/| |__| |\ |                 
      |  | |  | | \| |__] |  | |  | | \|  
            
                          by- Prajjwal Subedi
""")
print(f"""
Guess the Animal: {final}
Number of letters: {len(word)}
""")
word_len = len(word)

lives = 0
letters_changed = 0
while lives < 7:
    if letters_changed < word_len:
        choice = input('Please choose the letter:   ').lower()
        t = 0
        if choice in word:
            if choice in show:
                print(f'You already choosed {choice} before.!!!')
            else:
                for x in word:
                    if x == choice:
                        y = word.index(choice, t)
                        show[y] = choice
                        letters_changed += 1
                    t += 1
                    final = ''.join(show)
                print(final)
        else:
            print(HANGMAN[lives])
            lives += 1
            print(final)
    else:
        print(f"""
.   ,.__..  .    .  ..__..  .
 \./ |  ||  |    |  ||  ||\ |
  |  |__||__|    |/\||__|| \|

  The Correct answer is {word}
    """)
        break

if lives > 5:
    print(f"""
    _   _ ____ _  _    _    ____ ____ ____ ____ 
     \_/  |  | |  |    |    |  | |  | [__  |___ 
      |   |__| |__|    |___ |__| |__| ___] |___ 

    The Correct answer was {word}
   """)
