import random

class player:
    def __init__(self, name: str, life=5):
        self.name = name
        self.life = life
        self.bullet = 5
    
    def is_shot(self):
        choice = random.randint(1,2)
        if choice == 1:
            return True
        else:
            return False

    def life_remaining(self):
        return f'{self.name} life remains {self.life}'

    def bullet_remaining(self):
        self.bullet -= 1
        return f'{self.name} bullet remains {self.bullet}'

    def take_cover(self, other):
        covers = ['behind a log','behind a tree','behind a stump','in a ravine','in the hollow','in the trenches','behind a wall','in a rubble','in a crater']
        choices = random.choice(covers)
        return f'{other.name} took cover {choices}'

    def shoot(self, other):
        print(self.name, 'takes a shot')
        if self.is_shot is True:
            other.life -= 1
            if other.life > 0:
                return (other.life_remaining())
            else:
                return f'{other.life_remaining()} \n{self.bullet_remaining()} \n{other.name} is dead.'
        else:
            return f'{other.life_remaining()} \n{self.bullet_remaining()} \n{self.take_cover(other)}'
            

def main():
    First_player = input('First player name: ')
    Second_player = input('Second player name: ')
    round = 0
    while True:
        round += 1
        print ("round",round)
        player1 = player(First_player)
        player2 = player(Second_player)
        print('player1:',player1.__dict__)
        print('player2:',player2.__dict__)
        print(player1.shoot(player2))
        print(player2.shoot(player1))
        input('go to the next round\n\n')

if __name__ =='__main__':
    main()