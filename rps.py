
import random
import sys

class Player:
    pass
    
    
class HumanPlayer(Player):
    #def __init__(self):
        
    def move(self):
        a = str(input('Rock, paper, scissors? [r/p/s] '))
        return a
    
    
class ComputerPlayer(Player):
    def move(self):
        b = random.choice(['r', 'p', 's'])
        return b
        
class Game():
    def play(self):
        print('--- Rock Paper Scissors Game ---')
        rounds = int(input('How many rounds would you like to play? '))
    #    dict = {
     #       ('r', 'r') : 'tie',
      #      ('r', 'p') : 'lose',
       #     ('r', 's') : 'win',
        #    ('p', 'r') : 'win',
         #   ('p', 'p') : 'tie',
          #  ('p', 's') : 'lose',
           # ('s', 'r') : 'lose',
            #('s', 'p') : 'win',
            #('s', 's') : 'tie'
        #}

        if rounds == 0:
            sys.exit()
        else:
            human = HumanPlayer()
            computer = ComputerPlayer()
            count = 0
            tie = 0
            win = 0
            lose = 0
            for i in range(0, rounds):
                move1 = human.move()
                move2 = computer.move()
                #print(move2)
                #print(move1)
                if move1 == 'r' and move2 == 'r':
                    print('You: Rock | Computer: Rock')
                    print('This round is a tie!')
                    print()
                    #tie = 1
                if move1 == 'p' and move2 == 'p':
                    print('You: Paper | Computer: Paper')
                    print('This round is a tie!')
                    print()
                    #tie = 1
                if move1 == 's' and move2 == 's':
                    print('You: Scissors | Computer: Scissors')
                    print('This round is a tie!')
                    print()
                    #tie = 1
                if move1 == 'p' and move2 == 'r':
                    print('You: Paper | Computer: Rock')
                    print('You won this round!')
                    print()
                    win += 1
                if move1 == 'r' and move2 == 's':
                    print('You: Rock | Computer: Scissors')
                    print('You won this round!')
                    print()
                    win += 1
                if move1 == 's' and move2 == 'p':
                    print('You: Scissors | Computer: Paper')
                    print('You won this round!')
                    print()
                    win += 1
                if move1 == 'p' and move2 == 's':
                    print('You: Paper | Computer: Scissors')
                    print('You lost this round!')
                    print()
                    lose += 1
                if move1 == 's' and move2 == 'r':
                    print('You: Scissors | Computer: Rock')
                    print('You lost this round!')
                    print()
                    lose += 1
                if move1 == 'r' and move2 == 'p':
                    print('You: Rock | Computer: Paper')
                    print('You lost this round!')
                    print()
                    lose += 1
            self.score(win, lose)
                #print('as')
                #tuple = (move1, move2)
                #for j, k in dict.items():
                    #if tuple == j:
                        #print(k)
            
    def score(self, win, lose):
        print('Final score: Human ', win, '-', lose, 'Computer')
        self.replay()
        

    def replay(self):
        ard = input('Do you still want to play? y/n ')
        if ard == 'y':
                self.play()
        elif ard == 'n':
                sys.exit()
        else:
            print('Sorry, only y or n')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#        if count == rounds:
 #           return 'Human ', human_score, '-', computer_score, 'Computer'
  #      if tie != 0:
   #         print('Human ', human_score, '-', computer_score, 'Computer')
    #    if win != 0:
     #       if human_score == 0:
      #          human_score = 1
       #     else:
        #        human_score += 1
         #   print('Human ', human_score, '-', computer_score, 'Computer')
   #     if lose != 0:
    #        if computer_score == 0:
     #           computer_score == 1
      #      else:
       #         computer_score += 1
        #    print('Human ', human_score, '-', computer_score, 'Computer')
       # tie1 = tie
        #win1 = win
        #lose1 = lose
        
            
        
        
        
                
                
#game = Game()
#game.play()
