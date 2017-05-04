class Engine(object):

    def __init__(self, scene_map):
        """init the engine with a map containing many scenes"""
        self.map = scene_map

    def play(self):
        """run the game with the opening scene"""
        self.map.opening_scene()


class Scene(object):

    def enter(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

     def enter(self):
         print "You are in the central corridor"

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapdePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start):
        self.scene = start


    def next_scene(self, scene_name):
        self.scene = scene_name
        self.opening_scene()

    def opening_scene(self):
        if self.scene == 'central_corridor':
            a_corridor = CentralCorridor()
            a_corridor.enter()
        else:
            print "Unknown room"



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()