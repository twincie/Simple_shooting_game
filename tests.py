import random
import sys

class player:
    def __init__(self, name: str, life=5):
        self.name = name
        self.life = life
        self.bullet = 30
    
    def is_shot(self):
        choice = random.randint(1,2)
        if choice == 1:
            return True
        return False

    def hit(self, other):
        other.life -= 1
        if other.life <= 0:
            print(other.name + ' was killed')
            print('game over ')
            print(self.name +' won')
            sys.exit()
        else:
            return f'{other.name} has been shot'

    def take_cover(self, other):
        covers = ['behind a log','behind a tree','behind a stump','in a ravine','in the hollow','in the trenches','behind a wall','in a rubble','in a crater']
        choices = random.choice(covers)
        return f'{other.name} took cover {choices}'

    def shoot(self, other):
        print(self.name, 'takes a shot')
        self.bullet -= 1
        choice = self.is_shot()
        if choice is True:
            return self.hit(other)
        else:
            covers = ['behind a log','behind a tree','behind a stump','in a ravine','in the hollow','in the trenches','behind a wall','in a rubble','in a crater']
            choices = random.choice(covers)
            return f'{other.name} took cover {choices}'

def main():
    First_player = input('First player name: ')
    Second_player = input('Second player name: ')
    player1 = player(First_player)
    player2 = player(Second_player)
    round = 0
    while True:
        round += 1
        print ('round',round)
        print(player1.shoot(player2))
        print(player2.shoot(player1))
        print(f'LIVES Remaining:[{player1.name}:{player1.life},{player2.name}:{player2.life}]')
        print(f'BULLET Remaining:[{player1.name}:{player1.life},{player2.name}:{player2.life}]')
        print('\n')

if __name__ =='__main__':
    main()