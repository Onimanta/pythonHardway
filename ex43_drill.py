# Problems in this program:
# - when participants are put into the Fight class they are in a list and their name are not clear ('a_player' become 'self.fighters[0]')
# - The speed is not really taken into account turn-wise


class Fight(object):

    def __init__(self, fighters):
        self.fighters = fighters

    def fight(self):
        print "A fight start between %s and %s" % (self.fighters[0].name, self.fighters[1].name)

        while self.fighters[0].life_point > 0 and self.fighters[1].life_point > 0:
            print self.get_fight_state()
            print "What do you do?"
            print "1. attack"

            player_action = raw_input("> ")

            if self.fighters[0].speed >= self.fighters[1].speed:

                if player_action == "1":
                    self.fighters[0].attack(self.fighters[1]) # attack of the player (in first)
                    self.fighters[1].attack(self.fighters[0]) # attack of the opponent
                else:
                    print "Action not recognized"

            elif self.fighters[0].speed < self.fighters[1].speed:

                if player_action == "1":
                    self.fighters[1].attack(self.fighters[0]) # attack of the opponent (in first)
                    self.fighters[0].attack(self.fighters[1]) # attack of the player
                else:
                    print "Action not recognized"

        if self.fighters[0].life_point <= 0:
            print "You loose"
        elif self.fighters[1].life_point <= 0:
            print "You win"
        else:
            print "Draw"

    def get_fight_state(self):
        state = ""
        for participant in self.fighters:
            state += "%s : %d\n" % (participant.name, participant.life_point)
        return state + "\n"


class Participant(object):

    def attack(self, participant):
        print "%s attack" % self.name
        damage = self.atk * 2 - participant.defense
        participant.life_point -= damage
        print "%s takes %d damage" % (participant.name, damage)

class Player(Participant):

    def __init__(self):
        self.name = "You"
        self.life_point = 10
        self.atk = 3
        self.defense = 3
        self.speed = 4

    def attack(self, participant):
        print "%s attack" % self.name
        damage = self.atk * 3 - participant.defense
        participant.life_point -= damage
        print "%s takes %d damage" % (participant.name, damage)


class Opponent(Participant):

    def __init__(self, name, life_point, attack, defense, speed):
        self.name = name
        self.life_point = life_point
        self.atk = attack
        self.defense = defense
        self.speed = speed

    def attack(self, participant):
        super(Opponent, self).attack(participant)

a_player = Player()
an_opponent = Opponent('a bad guy', 5, 3, 2, 3)

sparring = Fight([a_player, an_opponent])
sparring.fight()