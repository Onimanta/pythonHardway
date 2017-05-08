from random import sample # used to choose the 3 working escape pods

class Engine(object):

    def __init__(self, scene_map):
        """init the engine with a map containing many scenes"""
        self.scene_map = scene_map

    def play(self):
        """run the game with the opening scene"""
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('escape_pod')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # print the last scene
        current_scene.enter()


class Scene(object):

    def enter(self):
        pass

class Death(Scene):

    def __init__(self, why):
        self.reason = why

    def enter(self):
        print self.reason + " Good job!"
        exit()

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons have invaded our spaceship."
        print "Your comrades and you have been made prisoner but you succeed to escape."
        print "You have to go the planet below to seek for help!"
        print "You are now in the central corridor."

        print "You believed that you were alone but a Gothon show up in front of you!"
        print "You choose to use the last weapon you have left: your sense of humor."
        print "Tell a joke to the Gothon."
        print "1. What is better than one Gothon?.. Two Gothon!"
        print "2. There 3 Gothons on a space boat. One of them jump in the water..hum..the space.. ..and.."

        joke = raw_input("> ")

        if joke == "1":
            print "The Gothon liked your joke and he now think that you are a cool dude."
            print "He lets you continue your way."
            return 'weapon_armory'
        elif joke == "2":
            print "Your joke didn't make the Gothon laugh so he put you in an hyper securised cell."
            death = Death("You'll spend the rest of your life prisoner from the Gothons, peeling space potatoes.")
            death.enter()
        elif joke == "tp": # cheat code to go directly to the escape pod
            return 'escape_pod'
        else:
            print "You don't know what to do so you just go back to your cell."
            death = Death("You'll spend the rest of your life prisoner from the Gothons, peeling space potatoes.")
            death.enter()

class LaserWeaponArmory(Scene):

    def enter(self):
        print "After walking through some corridors you arrive in a laser weapon armory"

        print "On a shelf there's some balls with \"Neutron bomb\" writed on it."
        print "You take one of these but you notice that a code is needed to activate it."
        print "On the wall there is a big sign on which is writted : "
        print "To activate a neutron bomb type \"the code\" on his keyboard."

        nb_of_try = 0

        while nb_of_try < 3:
            print "What do you do?"
            print "1. Try to type a code on the bomb's keyboard"
            print "2. Search for more information in the room"

            code = raw_input("> ")

            if code == "1":
                print "An annoying noise coming from the bomb tells you that you have typed the wrond code."
                nb_of_try += 1
            elif code == "2":
                print "You search on others shelves, between laser guns, beam sabers and space bazookas but you found nothing."
                nb_of_try += 1
            elif code == "the code":
                print "You hear a sound coming from the bomb and it now emit a green light. It seems like it is activated."
                print "You continue your way through the maze of rooms and corridors."
                return 'the_bridge'
            else:
                print "You're trying to shake the bomb. It don't seem to work."

        print "A Gothon show up in the room. He captures you and puts you in an hyper securised cell."
        death = Death("You'll spend the rest of your life prisoner from the Gothons, peeling space potatoes.")
        death.enter()

class TheBridge(Scene):

    def enter(self):
        print "You arrive in a big room full of command panels, it's the bridge. A Gothon is waiting for you."
        print "It seems that he don't want to let you place the bomb."

        distracted = False

        while True:
            print "What do you do?"
            print "1. Place the bomb"
            print "2. Fight with the Gothon"
            print "3. Tell the Gothon that there is a Lamborghini spaceship that pass in front of the window"

            gothon = raw_input("> ")

            if gothon == "1" and distracted:
                print "You place the bomb under a control panel and you run out of here."
                return 'escape_pod'
            elif gothon == "1" and not distracted:
                print "The Gothon sees you placing the bomb. He zap you with is gun and that transforms you into a space frog."
                death = Death("You'll spend the rest of your life swiming in space and eating space bugs.")
                death.enter()
            elif gothon == "2":
                print "You try to run on the Gothon to fight him but he zap you with is gun and that transforms you into a space frog."
                death = Death("You'll spend the rest of your life swiming in space and eating space bugs.")
                death.enter()
            elif gothon == "3" and distracted:
                print "He sees that there are no space Lamborghini and that you're making fun of him."
                print "He zap you with is gun and that transforms you into a space frog."
                death = Death("You'll spend the rest of your life swiming in space and eating space bugs.")
                death.enter()
            elif gothon == "3" and not distracted:
                print "The Gothon runs at the window and looks where the space car is."
                distracted = True
            else:
                print "You try to run back to the laser weapon armory but you fall off the ground"
                print "The Gothon catches you up and put you in an hyper securised cell."
                death = Death("You'll spend the rest of your life prisoner from the Gothons, peeling space potatoes.")
                death.enter()

class EscapePod(Scene):

    def enter(self):
        print "You finally arrive in the room where the escape pods are."

        print "There are five escape pods numbered from 1 to 5."
        print "You have the hurry, the bomb is gonna explode really soon!"
        print "Which one do you take ?"

        working_pods = sample(["1", "2", "3", "4", "5"], 3)

        selected_pod = raw_input("> ")

        print "You enter in the pod and you're popped out of the ship."

        if selected_pod in working_pods:
            print "Your pod is heading right in the direction of the planet."
            print "You take a look above and you see the spaceship exploding."
            print "Yeaaah! You made it."
            print "You have the feeling that you have forgotten something but you can't remember it."
            print "Nevermind.. Now let's have some fun on this planet!"
        elif selected_pod not in working_pods:
            print "Your thrusters don't seem work correctly. After a few seconds of hesitation they stop."
            print "The space ship explode and you're propulsed into the space. You decide to activate the hyper sleep module."
            print "After dozens of years something is finally waking you up."
            print "You get up and you notice that you're surrounded by armed men."
            print "You're being arrested because you let your comrades die in the explosion of the ship back in the days."
            death = Death("You'll spend the rest of your life in a special jail dedicated to Gothons imprisonment.")
            death.enter()
        else:
            print "The thrusters of your pod are mounted upside down so you come back to the ship."
            death = Death("The ship explode and you, the Gothons AND your comrads dies in the explosion.")
            death.enter()

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
    }

    def __init__(self, start):
        self.scene = start

    def next_scene(self, scene_name):
        scene = self.scenes.get(scene_name)
        return scene

    def opening_scene(self):
        """Return the first scene"""
        a_corridor = CentralCorridor()
        return a_corridor

print """
******************************
Gothons from Planet Percal #25
******************************
"""

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

print """
  ***
THE END
  ***
"""