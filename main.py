from dataclasses import dataclass
from bakery import assert_equal
from drafter import *
import random


set_website_title("Pokemon Fight")

add_website_css("body","font-size: 12px;")

#set_site_information




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
    if pokemon == 0:
        return Pokemon("Pikachu",test_attacks,"electric",100,100,0.5,give_sprite(0))
    if pokemon == 1:
        return Pokemon("Electrode",test_attacks,"electric",200,200,0.5,give_sprite(1))
    if pokemon == 2:
        return Pokemon("Oddish",test_attacks,"grass",50,50,0.5,give_sprite(2))
    if pokemon == 3:
        return Pokemon("Seedot",test_attacks,"grass",75,75,0.5,give_sprite(3))
    return Pokemon("Pikachu",test_attacks,"electric",100,100,0.5,give_sprite(0))


pikachu = Pokemon("Pikachu",test_attacks,"electric",100,100,0.5,give_sprite(0))
electrode = Pokemon("Electrode",test_attacks,"electric",200,200,0.5,give_sprite(1))
oddish = Pokemon("Oddish",test_attacks,"grass",50,50,0.5,give_sprite(2))
seedot = Pokemon("Seedot",test_attacks,"grass",75,75,0.5,give_sprite(3))

pokemon_list = [pikachu,electrode,oddish,seedot]



def switch_pokemon(state: State, pokemon: int,change: int) -> Pokemon:
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
    
def calc_attack(state: State, attack_num: int) -> bool:
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
        Button("Some other fourth thing", "pick_pokemon"),
    ])

@route
def pick_pokemon(state: State) -> Page:
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
def opponent_update(state: State, their_name: str, you_name: str) -> Page:
        state.you = you_name
        state.enemy = their_name
        return pick_opponent(state)
        
        
        
        
        
        
    
    

@route
def first_next_pokemon(state: State)-> Page:
    state.you_pokemon[0] = switch_pokemon(state,1,1)
    return pick_pokemon(state)

@route
def first_last_pokemon(state: State)-> Page:
    state.you_pokemon[0] = switch_pokemon(state,1,-1)
    return pick_pokemon(state)

@route
def second_next_pokemon(state: State)-> Page:
    state.you_pokemon[1] = switch_pokemon(state,2,1)
    return pick_pokemon(state)

@route
def second_last_pokemon(state: State)-> Page:
    state.you_pokemon[1] = switch_pokemon(state,2,-1)
    return pick_pokemon(state)

@route
def third_next_pokemon(state: State)-> Page:
    state.you_pokemon[2] = switch_pokemon(state,3,1)
    return pick_pokemon(state)

@route
def third_last_pokemon(state: State)-> Page:
    state.you_pokemon[2] = switch_pokemon(state,3,-1)
    return pick_pokemon(state)



@route
def enter_fight(state: State) -> Page:
    return Page(state, [
        "You are " + str(state.you) + ".\n",
        "Your evil villian is " + str(state.enemy) + "---------------------------------------------------------------------------------------------------------| "+ state.enemy_pokemon[0].name + "    HP: (" + str(state.enemy_pokemon[0].max_health) + " / " + str(state.enemy_pokemon[0].health) + ")     |---------",
        "\n",
        str(state.you_pokemon[0].image.line1) + "-----------------------------------------------------------------------------------------------------------------------" + str(state.enemy_pokemon[0].image.line1) + "\n",
        str(state.you_pokemon[0].image.line2) + "-----------------------------------------------------------------------------------------------------------------------" + str(state.enemy_pokemon[0].image.line2) + "\n",
        str(state.you_pokemon[0].image.line3) + "-----------------------------------------------------------------------------------------------------------------------" + str(state.enemy_pokemon[0].image.line3) + "\n",
        str(state.you_pokemon[0].image.line4) + "-----------------------------------------------------------------------------------------------------------------------" + str(state.enemy_pokemon[0].image.line4) + "\n",
        str(state.you_pokemon[0].image.line5) + "-----------------------------------------------------------------------------------------------------------------------" + str(state.enemy_pokemon[0].image.line5) + "\n",
        str(state.you_pokemon[0].image.line6) + "-----------------------------------------------------------------------------------------------------------------------" + str(state.enemy_pokemon[0].image.line6) + "\n",
        str(state.you_pokemon[0].image.line7) + "-----------------------------------------------------------------------------------------------------------------------" + str(state.enemy_pokemon[0].image.line7) + "\n",
        str(state.you_pokemon[0].image.line8) + "-----------------------------------------------------------------------------------------------------------------------" + str(state.enemy_pokemon[0].image.line8) + "\n",
        Button(str(state.you_pokemon[0].attacks[0].name), "attack_one"),
        Button(str(state.you_pokemon[0].attacks[1].name), "attack_two"),        
        "-|OOO|--| "+ state.you_pokemon[0].name + "    HP: (" + str(state.you_pokemon[0].max_health) + " / " + str(state.you_pokemon[0].health) + ")     |---------",
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
    state.enemy_pokemon = [make_pokemon(0),make_pokemon(0),make_pokemon(0)]
    state.you_pokemon = [make_pokemon(0),make_pokemon(0),make_pokemon(0)]
    return index(state)

@route
def end_game(state: State) -> Page:
    
    return Page(state, [
        "whoa ho ho! You Won/Lost! \n", 
        Button("Start again", "restart"),
    ])

@route
def attack_one(state: State) -> Page:
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
    if len(state.you_pokemon) == 3:
        state.you_pokemon = [state.you_pokemon[1],state.you_pokemon[2],state.you_pokemon[0]]
    elif len(state.you_pokemon) == 2:
        state.you_pokemon = [state.you_pokemon[1],state.you_pokemon[0]]
    state.action = "You have switched to " + state.you_pokemon[0].name
    
    return enter_fight(state)











start_server(State("Blue",[make_pokemon(0),make_pokemon(0),make_pokemon(0)],"Red",[make_pokemon(0),make_pokemon(0),make_pokemon(0)],"The fight has started!",0,0,0), initial_route = "index") 
