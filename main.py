import random
import sys

class player:
    def __init__(self, name: str, life=5):
        self.name = name
        self.life = life
        self.bullet = 20
    
    def is_shot(self):
        choice = random.randint(1,2)
        if choice == 1:
            return True
        return False

    def hit(self, other):
        self.bullet -= 1
        other_was_hit = random.getrandbits(1)
        if other_was_hit:
            other.life -= 1
            if other.life <= 0:
                print(other.name + ' was killed')
                print('***********')
                print('|game over|*********')
                print('***********')
                print(self.name +' won')
                sys.exit()
            else:
                return f'{other.name} has been shot'
        else:
            covers = ['behind a log','behind a tree','behind a stump','in a ravine','in the hollow','in the trenches','behind a wall','in a rubble','in a crater']
            choices = random.choice(covers)
            return f'{other.name} took cover {choices}'

    def take_cover(self, other):
        covers = ['behind a log','behind a tree','behind a stump','in a ravine','in the hollow','in the trenches','behind a wall','in a rubble','in a crater']
        choices = random.choice(covers)
        return f'{other.name} took cover {choices}'

    def shoot(self, other):
        print(self.name, 'takes a shot')
        print(self.hit(other))
        print(other.name, 'takes a shot')
        print(other.hit(self))
        return

def main():
    First_player = input('First player name: ')
    Second_player = input('Second player name: ')
    player1 = player(First_player)
    player2 = player(Second_player)
    round = 0
    print('****************************************')
    print('\n')
    while True:
        round += 1
        print ('***********')
        print ('| round',round,'|')
        print ('***********')
        print(player1.shoot(player2))
        print('****************************************')
        print(f'LIVES Remaining:[{player1.name}:{player1.life},{player2.name}:{player2.life}]')
        print(f'BULLET Remaining:[{player1.name}:{player1.bullet},{player2.name}:{player2.bullet}]')
        print('****************************************')
        print('\n')
        
if __name__ =='__main__':
    main()