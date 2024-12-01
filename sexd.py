#!/usr/bin/env python3
#let ChatGPT write a Sex Dice for me 
#things went on 

import random 
import os
from time import sleep

actions = ["Nudeln", "Kartoffeln", "Reis", "Polenta", "Kartoffelbrei", "Hirsetaler", "Pommes"]
body_parts = ["Gemüse", "Gemüse und Tofu", "Pilzen und Gemüse", "Soß", "Pilzen und Tofu", "Salat", "Schweinehälften"] 

input("Was wollen Sie essen? ENTER Drücken, um es herauszufinden!")

def roll_sex_dice(): 
	action = random.choice(actions) 
	body_part = random.choice(body_parts) 
	return f"{action} mit {body_part}" 

# sleep for 2 seconds after having asked then clean screen
sleep(2)
os.system('clear')

print("Sie wollen", roll_sex_dice(), "essen.")

#clean at end for next use
sleep(5)
os.system('clear')