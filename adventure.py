from adventurelib import *
from datetime import datetime
import adventurelib
import random

have_key = False
have_potion = False
have_effigy = False
found_book = False
found_hatch = False
opened_book = False
opened_door = False
opened_hatch = False
opened_cabinet = False
saved_person = False
hidden_items = [ "book", "key", "potion", "hatch", "effigy" ]

def reset():
	global have_key, have_potion, have_effigy, found_book, found_hatch, opened_book, opened_door, opened_hatch, opened_cabinet, saved_person
	have_key = False
	have_potion = False
	have_effigy = False
	found_book = False
	found_hatch = False
	opened_book = False
	opened_door = False
	opened_hatch = False
	opened_cabinet = False
	saved_person = False

def no_command_matches(command):
	print(random.choice([
		f"It's not possible to '{command}'.",
		"Hmmm, that didn't work.",
		"Perhaps you could try another word or action.",
		"Nothing happens..."
	]))

adventurelib.no_command_matches = no_command_matches

def get_part_of_day(h):
	return (
		"morning"
		if 5 <= h <= 11
		else "afternoon"
		if 12 <= h <= 17
		else "evening"
		if 18 <= h <= 22
		else "night"
	)

class Object:
	global hidden_items
  
	def __init__(self, name, look_at, use = None, take = None, open = None, pull = None):
		self._name = name
		self._look_at = look_at
		self._use = use
		self._take = take
		self._open = open
		self._pull = pull

	def look_at(self):
		if type(self._look_at) == str: 
			print(self._look_at)
		elif callable(self._look_at): 
			self._look_at()
			
	def take(self):
		if self._take is None: 
			print("It's too big to take with you!")
		elif type(self._take) == str: 
			print(self._take)
		elif callable(self._take): 
			self._take()
			
	def use(self):
		if self._use is None: 
			print(f"The {self._name} cannot be used.")
		elif type(self._use) == str: 
			print(self._use)
		elif callable(self._use): 
			self._use()
			
	def open(self):
		if self._open is None: 
			print(f"But.. how to open a {self._name}?")
		elif type(self._open) == str: 
			print(self._open)
		elif callable(self._open): 
			self._open()
					
	def pull(self):
		if self._pull is None:
			if self._name in hidden_items:
				print("Hmmm, that didn't do anything.")
			else:
				print(f"You pull on the {self._name} and it is now in different a position than it was before! :p")
		elif type(self._pull) == str: 
			print(self._pull)
		elif callable(self._pull):
			self._pull()

def look_at_desk():
	global found_book
	print("The desk is simple but made from beautiful wood. It looks a bit old. There are a few books laying on the table. One *book* in particular grabs your attention.")
	found_book = True

def look_at_book():
	global found_book
	if found_book: 
		print("It's actually a spellbook! It looks like there is something inside of it (aside from paper). Would you like to 'open' the book?")
	else: 
		print("I don't know of any book...")
  
def look_at_key():
  global opened_book
  if opened_book: 
    print("It is an old-fashioned iron key. There's a label on it that says *cabinet*.")
  else: 
    print("I don't know of any key...")
  
def look_at_potion():
	global opened_cabinet
	if opened_cabinet: 
		print("On the inside of the small potion flask is a green glowing fluid. On the side of the potion is a label that says \"Antidote. Pour over effigy. Not for drinking!\"")
	else: 
		print("I don't know of any potion...")
  
def look_at_hatch():
	global found_hatch
	if found_hatch: 
		print("There is a small hatch under the carpet! Just like the rest of the floor it is made from wood. It looks like it can be pulled open.")
	else:
		print("Hmmm I don't see any hatch.")
  
def look_at_effigy():
	if opened_hatch:
		print("It looks like a miniature version of a kitty made from straw! The kitty looks very cute but is not able to do anything.")
	else:
		print("An effigy? What's that?")
	
def use_key():
	global have_key, opened_book, opened_cabinet
	if have_key:
		if not opened_cabinet:
			print("You opened the door of the cabinet with the key! Hmmmm.. there is actually nothing inside the cabinet except for a small green 'potion'.")
			opened_cabinet = True
	elif opened_book:
		print("The key cannot be used right now, but you can 'take' it.")
	else:
		print("You don't have any key. :o")

def take_book():
	global found_book
	if found_book:
		print("There's no need to take the book with you. :)")
	else:
		print("Hmmm there might be some books on the *desk*, but you'll have to take a closer 'look at' it first.")

def take_key():
	global have_key, opened_book
	if have_key:
		print("You already have the key!")
	elif opened_book: 
		print("As you take the key you can read the text on the page a little bit better. The book describes a mysterious spell used by ancient shamans to turn a living creature into a straw doll!")
		have_key = True
	else: 
		print("There's no key in sight.")

def take_potion():
	global have_potion, opened_cabinet
	if have_potion: 
		print("You already have the potion!")
	elif opened_cabinet: 
		print("You are now carrying the potion with you.")
		have_potion = True
	else:
		print("There's no potion in sight.")
 
def take_effigy():
	global have_effigy, opened_hatch
	if have_effigy: 
		print("You already have the effigy!")
	elif opened_hatch: 
		print("You gently pick it up and are now carrying a straw effigy of a kitty with you!")
		have_effigy = True
	else:
		print("What's that?")

def open_book():
	global opened_book, found_book, have_key
	if opened_book:
		if have_key:
			print("The book is already laying open on the desk.")
		else:
			print("The book is already laying open on the desk. There is a *key* on top of the open page.")
	elif found_book:
		print("You open the book on a random page. It is a chapter about shamanic rituals, and there is a *key* stuck to the page! You could try to 'take' it.")
		opened_book = True
	else:
		print("You'll have to get a closer 'look at' the desk first.")
 
def open_door():
	global saved_person
	if saved_person:
		print("You open the door and step outside with your new friend next to you. She meows and you suddenly realize that you are high up in green mountains. The kitty runs ahead and looks back for you to follow. Together you walk towards the horizon...\n")
		exit()
	else: 
		print("You open the door and step outside. Suddenly you realize that you are sitting on your computer and playing a text adventure game...")
		exit()
 
def open_cabinet():
	global have_key, opened_cabinet
	if have_key: 
		print("You opened the door of the cabinet with the key! Hmmmm.. there is actually nothing inside the cabinet except for a small green 'potion'.")
		opened_cabinet = True
	else:
		print("You try to open the cabinet but it's locked. You can see a keyhole in the cabinet door.")

def open_hatch():
	global opened_hatch, found_hatch
	if opened_hatch: 
		print("The hatch is already open!")
	elif found_hatch: 
		print("You open the hatch and look inside.. there is a small object here that looks like an *effigy*, but because it is dark you can't really see any details. You can 'take' and 'look at' it to get a better view.",)
		opened_hatch = True
	else:
		print("A hatch? Hmmm haven't seen one around here.")
 
def use_potion():
	global have_potion, have_effigy, saved_person
	if saved_person:
		print("The potion has already been used!")
	elif have_potion and have_effigy:
		print("You pour the contents of the potion on the straw effigy and... There's a flash of smoke that slowly disappears. You can slowly see a shape appearing... there's a cute furry little kitty playing on the floor before you!")
		print("You found the kitty! Time to leave this place. :)")
		saved_person = True
	elif have_potion:
		print("There's nothing in your inventory to use the potion on! Unless you want to drink it..?!")
	else:
		print("You don't have any potion.")

def pull_carpet():
	global found_hatch
	if found_hatch:
		print("The carpet is already pulled back.")
	else:
		print("You pull away the carpet and... it reveals a small *hatch* underneath!")
		found_hatch = True

objects = {
	"chair" : Object(
	 	"chair",
		"The chair is in front of the desk and it looks quite comfortable to sit on.",
		"You try sitting on the chair. It really is as comfortable as it looked! But nothing else happens."
	),
	"desk" : Object(
	 	"desk",
		look_at_desk
	),
	"cabinet" : Object(
	 	"cabinet",
		"There's a large and sturdy cabinet in one corner of the room. You can see a keyhole in the cabinet door.",
		None,
		"The cabinet is wayyyy too big and heavy to pick up!",
		open_cabinet
	),
	"carpet" : Object(
	 	"carpet",
		"It is big and round and heavy, and has a dizzying pattern on it. When you look closer it you can see a slight bulge in the center of it. Perhaps it has been hastily moved recently?",
		"Hmmm.. you could try to 'pull' on the carpet.",
		"It's a little bit too big to put in your pockets, but you could try to 'pull' it instead!",
		None,
		pull_carpet
	),
	"door" : Object(
	 	"door",
		"There's a handle on the door that leads outside, but you cannot see what is on the other side of the door.",
		None,
		None,
		open_door,
		"Ahh that doesn't work because the door opens outwards."
	),
	"book" : Object(
	 	"book",
		look_at_book,
		open_book,
		take_book,
		open_book
	),
	"key" : Object(
	 	"key",
		look_at_key,
		use_key,
		take_key
	),
	"hatch" : Object(
	 	"hatch",
		look_at_hatch,
		None,
		None,
		open_hatch,
  	open_hatch
	),
	"potion" : Object(
	 	"potion",
		look_at_potion,
		use_potion,
		take_potion
	),
	"effigy" : Object(
		"effigy",
		look_at_effigy,
		None,
		take_effigy
	)
}

@when("help")
def help():
	print("--------------------------------------------------------------------------------")
	print("I need your help! There is a kitty trapped in this room! Please help find it by typing commands such as 'look', 'look at', 'use', 'take', and 'open'!")
	print("But let's start by saying 'hi'!\n")
	start(help=False)

@when("hi")
def greeting():
	print(f"Hiya, I hope you are having a good {get_part_of_day(datetime.now().hour)}! First of all, let's have a 'look' around the room.")

@when("look")
def look():
	print("You are standing in a small and brightly lit room. You can see a *chair*, a *desk* and a *cabinet*. There is a big *carpet* on the floor of the room, and there is a *door* to the outside.")
	print("What would you want to 'look at' in more detail?")
		
@when("look at OBJECT")
def look_at(object):
	if object not in objects:
		print("No such object to look at.")
	else:
		try: objects[object].look_at()
		except: pass
 
@when("use OBJECT")
def use(object):
	if object not in objects:
		print("No such object to use.")
	else:
		try: objects[object].use()
		except: pass
				
@when("take OBJECT")
def take(object):
	if object not in objects:
		print("No such object to take.")
	else:
		try: objects[object].take()
		except: pass
 
@when("open OBJECT")
def open(object):
	if object not in objects:
		print("No such object to open.")
	else:
		try: objects[object].open()
		except: pass

@when("pull OBJECT")
def pull(object):
	if object not in objects: 
		print("No such object to pull.")
	else:
		try: objects[object].pull()
		except: pass

@when("drink potion")
def drink_potion():
	if have_potion:
		print("You drink the potion and.. hmm nothing happens. A few moments pass and you start feel a strange sensation in your body.")
		print("You feel like you are shrinking! When you look down at your hands they are now made from straw! Oh nooooooo!")
		exit()
	else:
		print("You dont have any potion with you.")

def exit():
	global saved_person
	if saved_person:
		print("\nYayyyy you did it! You finished the game and got out of the room with your new friend! You can type 'quit' to exit the game or continue to play again.")
		reset()
	else:
		print("\nOopsie, something went wrong! Please try again. :D\n")
		reset()

reset()
help()
