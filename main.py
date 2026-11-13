from dataclasses import dataclass
from bakery import assert_equal
from drafter import *
import random


set_website_title("Pokemon Fight")

#set_site_information

add_website_css("body","font-size: 8px;")


'''
sprite set up

'''

@dataclass
class Sprite:
    line1: str
    line2: str
    line3: str
    line4: str
    line5: str
    line6: str
    line7: str
    line8: str
    

pikachu_sprite = Sprite( "⬛⬛🟨⬛⬛🟨⬛⬛",
                         "⬛⬛🟨🟨🟨🟨⬛⬛",
                         "⬛🟨🟨🟨🟨🟨🟨⬛",
                         "⬛🟨⬛🟨🟨⬛🟨⬛",
                         "⬛🟨🟨🟨🟨🟨🟨⬛",
                         "⬛⬛🟨⬛⬛🟨⬛⬛",
                         "⬛⬛🟨🟨🟨🟨⬛⬛",
                         "⬛🟨🟨🟨🟨🟨🟨⬛",
                )
voltorb_sprite = Sprite( "⬛⬛⬛⬛⬛⬛⬛⬛",
                         "⬛🟥🟥🟥🟥🟥🟥⬛",
                         "🟥⬜🟥🟥🟥🟥⬜🟥",
                         "🟥⬜⬛🟥🟥⬛⬜🟥",
                         "🟥🟥🟥🟥🟥🟥🟥🟥",                         
                         "⬜⬜⬜⬜⬜⬜⬜⬜",
                         "⬜⬜⬜⬜⬜⬜⬜⬜",
                         "⬛⬜⬜⬜⬜⬜⬜⬛",
                )

oddish_sprite = Sprite(    "⬛⬛⬛⬛⬛🟩🟩⬛",
                           "⬛🟩🟩🟩🟩🟩⬛⬛",
                           "⬛🟩⬛🟩🟩⬛⬛⬛",
                           "⬛⬛🟦🟦🟦🟦⬛⬛",
                           "⬛🟦🟥🟦🟦🟥🟦⬛",                         
                           "⬛🟦🟦🟦🟦🟦🟦⬛",
                           "⬛🟦🟦🟥🟥🟦🟦⬛",
                           "⬛⬛🟦🟦🟦🟦⬛⬛",
                )

seedot_sprite = Sprite(    "⬛⬛⬛⬛⬛⬛⬛⬛",
                           "⬛⬛⬛🟫🟫⬛⬛⬛",
                           "⬛🟫🟫🟫🟫🟫🟫⬛",
                           "⬛⬜⬜⬜⬜⬜⬜⬛",
                           "⬛🟫⬜🟫🟫⬜🟫⬛",                         
                           "⬛🟫🟫🟫🟫🟫🟫⬛",
                           "⬛🟫🟫🟫🟫🟫🟫⬛",
                           "⬛⬛🟫🟫🟫🟫⬛⬛",
                )
sprites = [pikachu_sprite,voltorb_sprite,oddish_sprite,seedot_sprite]

def give_sprite(ind: int)->Sprite:
    return sprites[ind]

'''
end sprite set up
'''



@dataclass
class Attack:
    '''
    
    '''
    name: str
    damage: int
    element: str
    
@dataclass
class Pokemon:
    name: str
    attacks: list[Attack]
    element: str
    max_health: int
    health: int
    defense: float
    image: Sprite
    

@dataclass
class State:
    enemy: str
    enemy_pokemon: list[Pokemon]
    you: str
    you_pokemon: list[Pokemon]
    action: str
    picked1: int
    picked2: int
    picked3: int
    

'''
attacks
'''
electro_fist = Attack("Electro Fist",30,"electric")
zap = Attack("Zap",20,"electric")
slap = Attack("Slap",20,"normal")
normal_fist = Attack("Normal Fist",30,"normal")
harden = Attack("Harden",1,"defense")

test_attacks = [electro_fist,zap,slap,harden]
'''
pokemon
'''
def make_pokemon(pokemon: int)-> Pokemon:
    '''
    This function takes in a number and gives a pokemon to prevent
    mutability
    
    attributes:
    pokemon - the number correlating to the pokemon in the pokemon list
    '''
    
    if pokemon == 0:
        return Pokemon("Pikachu",test_attacks,"electric",100,100,0.5,give_sprite(0))
    if pokemon == 1:
        return Pokemon("Electrode",test_attacks,"electric",200,200,0.5,give_sprite(1))
    if pokemon == 2:
        return Pokemon("Oddish",test_attacks,"grass",50,50,0.5,give_sprite(2))
    if pokemon == 3:
        return Pokemon("Seedot",test_attacks,"grass",75,75,0.5,give_sprite(3))
    return Pokemon("Pikachu",test_attacks,"electric",100,100,0.5,give_sprite(0))

assert_equal(make_pokemon(0),Pokemon("Pikachu",test_attacks,"electric",100,100,0.5,give_sprite(0)))
assert_equal(make_pokemon(1),Pokemon("Electrode",test_attacks,"electric",200,200,0.5,give_sprite(1)))


pikachu = Pokemon("Pikachu",test_attacks,"electric",100,100,0.5,give_sprite(0))
electrode = Pokemon("Electrode",test_attacks,"electric",200,200,0.5,give_sprite(1))
oddish = Pokemon("Oddish",test_attacks,"grass",50,50,0.5,give_sprite(2))
seedot = Pokemon("Seedot",test_attacks,"grass",75,75,0.5,give_sprite(3))

pokemon_list = [pikachu,electrode,oddish,seedot]



def switch_pokemon(state: State, pokemon: int,change: int) -> Pokemon:
    '''
    This function changes a pokemon on the user's team
    
    attributes:
    state - The State class that the pokemon are taken from
    pokemon - number slot which will have the change in pokemon
    change: what the pokemon is changing by on the list of pokemon
    
    '''
    
    if pokemon == 1:
        state.picked1 = state.picked1 + change
        if state.picked1 > len(pokemon_list) - 1:
            state.picked1 = 0
        if state.picked1 < 0:
            state.picked1 = len(pokemon_list) - 1
        return make_pokemon(state.picked1)
    if pokemon == 2:
        state.picked2 = state.picked2 + change
        if state.picked2 > len(pokemon_list) - 1:
            state.picked2 = 0
        if state.picked2 < 0:
            state.picked2 = len(pokemon_list) - 1
        return make_pokemon(state.picked2)
    if pokemon == 3:
        state.picked3 = state.picked3 + change
        if state.picked3 > len(pokemon_list) - 1:
            state.picked3 = 0
        if state.picked3 < 0:
            state.picked3 = len(pokemon_list) - 1
        return make_pokemon(state.picked3)
    return make_pokemon(state.picked1)

assert_equal(switch_pokemon(State("Blue",[make_pokemon(0),make_pokemon(0),make_pokemon(0)],
                   "Red",[make_pokemon(0),make_pokemon(0),make_pokemon(0)],"The fight has started!",0,0,0),
             1, 1),Pokemon("Electrode",test_attacks,"electric",200,200,0.5,give_sprite(1)))
    
def calc_attack(state: State, attack_num: int) -> bool:
    '''
    This function matches your chosen move with
    their opponent's type to calculate damage.
    It also updates the action attribute
    
    attributes:
    attack_num: the number that correlates to the move chosen
    state - the State that has the enemy and your data
    '''    
    state.action = state.you_pokemon[0].name + " has used " + str(state.you_pokemon[0].attacks[attack_num].name) + " " 
    if state.you_pokemon[0].attacks[attack_num].element == "electric":
        if state.enemy_pokemon[0].element == "electric":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (2 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "fire":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (1 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "water":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (0.5 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "grass":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (2 + state.enemy_pokemon[0].defense))
    if state.you_pokemon[0].attacks[attack_num].element == "fire":
        if state.enemy_pokemon[0].element == "electric":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (1 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "fire":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (2 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "water":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (2 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "grass":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (0.5 + state.enemy_pokemon[0].defense))
    if state.you_pokemon[0].attacks[attack_num].element == "water":
        if state.enemy_pokemon[0].element == "electric":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (1 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "fire":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (0.5 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "water":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (2 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "grass":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (2 + state.enemy_pokemon[0].defense))
    if state.you_pokemon[0].attacks[attack_num].element == "grass":
        if state.enemy_pokemon[0].element == "electric":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (1 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "fire":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (2 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "water":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (0.5 + state.enemy_pokemon[0].defense))
        if state.enemy_pokemon[0].element == "grass":
            state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (2 + state.enemy_pokemon[0].defense))  
    if state.you_pokemon[0].attacks[attack_num].element == "normal":
        state.enemy_pokemon[0].health = state.enemy_pokemon[0].health - int(state.you_pokemon[0].attacks[attack_num].damage / (1 + state.enemy_pokemon[0].defense))        
    return True


def calc_enemy_attack(state: State) -> bool:
    '''
    This function determines what attack the enemy will use and then and matches it with
    their opponent's type to calculate damage. It also updates the action attribute
    
    attributes:
    state - the State that has the enemy and your data
    move_select - selects a random number from 0 - 3 to choose a move
    '''
    move_select = random.randint(0,3)
    
    state.action = state.action + "| " + state.enemy_pokemon[0].name + " has used " + str(state.enemy_pokemon[0].attacks[move_select].name)
    if state.enemy_pokemon[0].attacks[move_select].element == "electric":
        if state.you_pokemon[0].element == "electric":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (2 + state.you_pokemon[0].defense))
        if state.you_pokemon[0].element == "fire":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (1 + state.you_pokemon[0].defense))
        if state.you_pokemon[0].element == "water":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (0.5 + state.you_pokemon[0].defense))
        if state.you_pokemon[0].element == "grass":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (2 + state.you_pokemon[0].defense))
    if state.enemy_pokemon[0].attacks[move_select].element == "fire":
        if state.you_pokemon[0].element == "electric":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (1 + state.you_pokemon[0].defense))
        if state.you_pokemon[0].element == "fire":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (2 + state.you_pokemon[0].defense))
        if state.you_pokemon[0].element == "water":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (2 + state.you_pokemon[0].defense))
        if state.you_pokemon[0].element == "grass":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (0.5 + state.you_pokemon[0].defense))    
    if state.enemy_pokemon[0].attacks[move_select].element == "fire":
        if state.you_pokemon[0].element == "electric":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (1 + state.you_pokemon[0].defense))
        if state.you_pokemon[0].element == "fire":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (2 + state.you_pokemon[0].defense))
        if state.you_pokemon[0].element == "water":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (2 + state.you_pokemon[0].defense))
        if state.you_pokemon[0].element == "grass":
            state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (0.5 + state.you_pokemon[0].defense))     
    if state.enemy_pokemon[0].attacks[move_select].element == "normal":
        state.you_pokemon[0].health = state.you_pokemon[0].health - int(state.enemy_pokemon[0].attacks[move_select].damage / (1 + state.you_pokemon[0].defense))    
    
    
    
    
    return True


@route
def index(state: State) -> Page:
    '''
    The index page that allows the user to enter the fight, pick your pokemon,
    and opponent
    
    attributes:
    state - the State that has the info to to be passed onto other pages
    '''
    return Page(state, [
        Button("Start the Fight!", "enter_fight"),
        "----------------------------------------------------------------------------------------",
        Button("Pick your Pokemon", "pick_pokemon"),
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        Button("Pick your Opponent!", "pick_opponent"),
        "----------------------------------------------------------------------------------------",
    ])

@route
def pick_pokemon(state: State) -> Page:
    '''
    The page that allows the user to pick their pokemon
    
    attributes:
    state - the State that has the pokemon images to display
    '''
    return Page(state, [
        "Choose your pokemon" + "---------------------------------------------------------------------------------------------------------|",
        Button("Return", "index"),
        "\n",
        "----" + str(state.you_pokemon[0].name) + "---------------------------" + str(state.you_pokemon[1].name) + "---------------------------" + str(state.you_pokemon[2].name) + "----"
        "\n",
        str(state.you_pokemon[0].image.line1) + "---------------" + str(state.you_pokemon[1].image.line1) + "---------------" + str(state.you_pokemon[2].image.line1) + "\n",
        str(state.you_pokemon[0].image.line2) + "---------------" + str(state.you_pokemon[1].image.line2) + "---------------" + str(state.you_pokemon[2].image.line2) + "\n",
        str(state.you_pokemon[0].image.line3) + "---------------" + str(state.you_pokemon[1].image.line3) + "---------------" + str(state.you_pokemon[2].image.line3) + "\n",
        str(state.you_pokemon[0].image.line4) + "---------------" + str(state.you_pokemon[1].image.line4) + "---------------" + str(state.you_pokemon[2].image.line4) + "\n",
        str(state.you_pokemon[0].image.line5) + "---------------" + str(state.you_pokemon[1].image.line5) + "---------------" + str(state.you_pokemon[2].image.line5) + "\n",
        str(state.you_pokemon[0].image.line6) + "---------------" + str(state.you_pokemon[1].image.line6) + "---------------" + str(state.you_pokemon[2].image.line6) + "\n",
        str(state.you_pokemon[0].image.line7) + "---------------" + str(state.you_pokemon[1].image.line7) + "---------------" + str(state.you_pokemon[2].image.line7) + "\n",
        str(state.you_pokemon[0].image.line8) + "---------------" + str(state.you_pokemon[1].image.line8) + "---------------" + str(state.you_pokemon[2].image.line8) + "\n",
        Button("last", "first_last_pokemon"),
        Button("next", "first_next_pokemon"),
        "---------------",
        Button("last", "second_last_pokemon"),
        Button("next", "second_next_pokemon"),
        "---------------",
        Button("last", "third_last_pokemon"),
        Button("next", "third_next_pokemon"),
        "\n",
    ])
@route
def pick_opponent(state: State) -> Page:
    '''
    The page that allows you to pick your name, your opponent's name, and
    the difficulty
    
    attributes:
    state - the State that has the opponent and user's name to be displayed
    as well as the opponent's pokemon to change
    '''
    return Page(state, [
        "Your current Villian's name is " + state.enemy + " and your name is " + state.you +" --------------------------------------------------------------------------------------",
        Button("Return", "index"),
        "\n",
        "Though, at a moment's notice they could be: ",
        TextBox("their_name",state.enemy),
        "and your name could be: ",
        TextBox("you_name",state.you),
        "\n",
        "\n",
        "\n",
        "select enemy difficulty",
        "\n",
        SelectBox("choice",["easy","medium","hard"],"easy"),
        "\n",
        Button("Confirm Changes","opponent_update"),
        
     ])       
        


@route
def opponent_update(state: State, their_name: str, you_name: str, choice: str) -> Page:
    '''
    updates the opponent and user's names as well as the opponent's pokemon
    
    attributes:
    state - the State that will be changed
    their_name: the new name for the enemy
    you_name: the new name for you
    choice: the difficulty level (this doesnt do anything yet
    but will effect what pokemon they choose eventually)
    '''
    for index, poketype in enumerate(state.you_pokemon):
        if poketype.element == "electric":
                state.enemy_pokemon[index] = make_pokemon(2)
        elif poketype.element == "fire":
                state.enemy_pokemon[index] = make_pokemon(2)
        elif poketype.element == "water":
                state.enemy_pokemon[index] = make_pokemon(1)
        elif poketype.element == "grass":
                state.enemy_pokemon[index] = make_pokemon(1)                
        else:
                state.enemy_pokemon[index] = make_pokemon(1)
        print(state.enemy_pokemon[index])
        
        state.you = you_name
        state.enemy = their_name
        return pick_opponent(state)
        
        


        
        
    
    

@route
def first_next_pokemon(state: State)-> Page:
    '''
    this route switches the first of your pokemon by +1
    on the pokemon list
    
    attributes:    
    state - the State that has the pokemon list
    '''
    state.you_pokemon[0] = switch_pokemon(state,1,1)
    return pick_pokemon(state)

@route
def first_last_pokemon(state: State)-> Page:
    '''
    this route switches the first of your pokemon by -1
    on the pokemon list
    
    attributes:    
    state - the State that has the pokemon list
    '''
    state.you_pokemon[0] = switch_pokemon(state,1,-1)
    return pick_pokemon(state)

@route
def second_next_pokemon(state: State)-> Page:
    '''
    this route switches the second of your pokemon by +1
    on the pokemon list
    
    attributes:    
    state - the State that has the pokemon list
    '''
    state.you_pokemon[1] = switch_pokemon(state,2,1)
    return pick_pokemon(state)

@route
def second_last_pokemon(state: State)-> Page:
    '''
    this route switches the second of your pokemon by -1
    on the pokemon list
    
    attributes:    
    state - the State that has the pokemon list
    '''
    state.you_pokemon[1] = switch_pokemon(state,2,-1)
    return pick_pokemon(state)

@route
def third_next_pokemon(state: State)-> Page:
    '''
    this route switches the third of your pokemon by +1
    on the pokemon list
    
    attributes:    
    state - the State that has the pokemon list
    '''
    state.you_pokemon[2] = switch_pokemon(state,3,1)
    return pick_pokemon(state)

@route
def third_last_pokemon(state: State)-> Page:
    '''
    this route switches the third of your pokemon by -1
    on the pokemon list
    
    attributes:    
    state - the State that has the pokemon list
    '''
    state.you_pokemon[2] = switch_pokemon(state,3,-1)
    return pick_pokemon(state)



@route
def enter_fight(state: State) -> Page:
    '''
    this route returns the main fighting page. It displays the user and the opponent's
    pokemon as well as the user's attacks
    
    attributes:
    state - the State class that has all the pokemon stored to be displayed
    and used in the fight

    '''
    return Page(state, [
        "You are " + str(state.you) + ".\n",
        "Your evil villian is " + str(state.enemy) + "---------------------------------------------------------------------------------------------------------| ",
        state.enemy_pokemon[0].name + "    HP: (" + str(state.enemy_pokemon[0].health) + " / " + str(state.enemy_pokemon[0].max_health) + ")     |---------",
        "\n",
        str(state.you_pokemon[0].image.line1),
        "-----------------------------------------------------------------------------------------------------------------------",
        str(state.enemy_pokemon[0].image.line1) + "\n",
        str(state.you_pokemon[0].image.line2),
        "-----------------------------------------------------------------------------------------------------------------------",
        str(state.enemy_pokemon[0].image.line2) + "\n",
        str(state.you_pokemon[0].image.line3),
        "-----------------------------------------------------------------------------------------------------------------------",
        str(state.enemy_pokemon[0].image.line3) + "\n",
        str(state.you_pokemon[0].image.line4),
        "-----------------------------------------------------------------------------------------------------------------------",
        str(state.enemy_pokemon[0].image.line4) + "\n",
        str(state.you_pokemon[0].image.line5),
        "-----------------------------------------------------------------------------------------------------------------------",
        str(state.enemy_pokemon[0].image.line5) + "\n",
        str(state.you_pokemon[0].image.line6),
        "-----------------------------------------------------------------------------------------------------------------------",
        str(state.enemy_pokemon[0].image.line6) + "\n",
        str(state.you_pokemon[0].image.line7),
        "-----------------------------------------------------------------------------------------------------------------------",
        str(state.enemy_pokemon[0].image.line7) + "\n",
        str(state.you_pokemon[0].image.line8),
        "-----------------------------------------------------------------------------------------------------------------------",
        str(state.enemy_pokemon[0].image.line8) + "\n",
        Button(str(state.you_pokemon[0].attacks[0].name), "attack_one"),
        Button(str(state.you_pokemon[0].attacks[1].name), "attack_two"),        
        "-|OOO|--| "+ state.you_pokemon[0].name + "    HP: (" + str(state.you_pokemon[0].health) + " / " + str(state.you_pokemon[0].max_health) + ")     |---------",
        str(state.action),
        "\n",
        Button(str(state.you_pokemon[0].attacks[2].name), "attack_three"),
        Button(str(state.you_pokemon[0].attacks[3].name), "attack_four"),
        "---------------------------------------------------------------------------------------------------------------------------",
        Button("Switch", "switch"),
        Button("Return", "restart"),
    ])

@route
def restart(state: State) -> Page:
    '''
    this route returns the user to the index,
    but also resets the pokemon
    '''
    state.enemy_pokemon = [make_pokemon(0),make_pokemon(0),make_pokemon(0)]
    state.you_pokemon = [make_pokemon(0),make_pokemon(0),make_pokemon(0)]
    return index(state)

@route
def end_game(state: State) -> Page:
    '''
    The end game page that occurs after the battle
    
    attributes:
    state - the State class to be fed into the index again when the user
    clicks the button
    '''
    return Page(state, [
        "whoa ho ho! You Won/Lost! \n", 
        Button("Start again", "restart"),
    ])

@route
def attack_one(state: State) -> Page:
    '''
    
    The function caled the calc_attack and calc_enemy_attack function and
    checks if the
    pokemon is below 100 hp. it then returns the enter_fight page.
    
    attributes:
    state - The State that gets the pokemon info from.

    '''
    calc_attack(state,0)
    if state.enemy_pokemon[0].health < 1:
        state.enemy_pokemon = state.enemy_pokemon[1:]
    if not state.enemy_pokemon:
        return end_game(state)
    calc_enemy_attack(state)

    if state.you_pokemon[0].health < 1:
        state.you_pokemon = state.you_pokemon[1:]
    if not state.you_pokemon:
        return end_game(state)
    return enter_fight(state)

@route
def attack_two(state: State) -> Page:
    '''
    
    The function caled the calc_attack and calc_enemy_attack function and
    checks if the
    pokemon is below 100 hp. it then returns the enter_fight page.
    
    attributes:
    state - The State that gets the pokemon info from.

    '''
    calc_attack(state,1)
    if state.enemy_pokemon[0].health < 1:
        state.enemy_pokemon = state.enemy_pokemon[1:]
    if not state.enemy_pokemon:
        return end_game(state)
    calc_enemy_attack(state)

    if state.you_pokemon[0].health < 1:
        state.you_pokemon = state.you_pokemon[1:]
    if not state.you_pokemon:
        return end_game(state)
    return enter_fight(state)

@route
def attack_three(state: State) -> Page:
    '''
    
    The function caled the calc_attack and calc_enemy_attack function and
    checks if the
    pokemon is below 100 hp. it then returns the enter_fight page.
    
    attributes:
    state - The State that gets the pokemon info from.

    '''
    calc_attack(state,2)
    if state.enemy_pokemon[0].health < 1:
        state.enemy_pokemon = state.enemy_pokemon[1:]
    if not state.enemy_pokemon:
        return end_game(state)
    calc_enemy_attack(state)

    if state.you_pokemon[0].health < 1:
        state.you_pokemon = state.you_pokemon[1:]
    if not state.you_pokemon:
        return end_game(state)
    return enter_fight(state)

@route
def attack_four(state: State) -> Page:
    '''
    
    The function caled the calc_attack and calc_enemy_attack function and
    checks if the
    pokemon is below 100 hp. it then returns the enter_fight page.
    
    attributes:
    state - The State that gets the pokemon info from.

    '''
    calc_attack(state,3)
    if state.enemy_pokemon[0].health < 1:
        state.enemy_pokemon = state.enemy_pokemon[1:]
    if not state.enemy_pokemon:
        return end_game(state)
    calc_enemy_attack(state)

    if state.you_pokemon[0].health < 1:
        state.you_pokemon = state.you_pokemon[1:]
    if not state.you_pokemon:
        return end_game(state)
    return enter_fight(state)

@route
def switch(state: State) -> Page:
    '''
    switches the pokemon you are actively using
    
    attributes:
    state - the State class that has the pokemon list
    '''
    if len(state.you_pokemon) == 3:
        state.you_pokemon = [state.you_pokemon[1],state.you_pokemon[2],state.you_pokemon[0]]
    elif len(state.you_pokemon) == 2:
        state.you_pokemon = [state.you_pokemon[1],state.you_pokemon[0]]
    state.action = "You have switched to " + state.you_pokemon[0].name
    
    return enter_fight(state)











start_server(State("Blue",[make_pokemon(0),make_pokemon(0),make_pokemon(0)],"Red",[make_pokemon(0),make_pokemon(0),make_pokemon(0)],"The fight has started!",0,0,0), initial_route = "index")
