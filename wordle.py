import random
from words import words


class wordle:
    def __init__(self):
        self.remaining = [chr(i) for i in range(97, 123)]
        self.letters = [chr(i) for i in range(97, 123)]
        self.word = list(words.word[random.randint(0,199)])
        self.guesses = 0
        self.guess = ''
        self.grid = ['x', 'x', 'x', 'x', 'x']

    def play(self):
        print('Thanks for playing wordle.')
        print('The rules are as follows:')
        print('Guess a word with 5 letters')
        print('You will get the letter in capitals if it is both in the word and in the correct space')
        print('You will get the letter in lower case if it\'s in the word but not in the place you guessed')
        print('You will get x if the letter is not in the word')

        while self.guesses <= 5:
            print('Have a guess!')
            guess = input()
            self.guess = guess
            self.guesses+=1
            self.resolve_guess()

            if 'x' not in self.grid:
                print(f'You win! The word was {self.word}')
                break
            if self.guesses >= 5:
                print('Sorry, you lose!')
                print(f'The word was {str(self.word)}')
                break

    def resolve_guess(self):
        if len(self.guess) != 5:
            print('Please make sure guess is 5 letters!')
        else:
            for i in range(0, 5):
                if self.guess[i] in self.remaining:
                    self.remaining.remove(self.guess[i])
                if self.guess[i] not in self.word:
                    continue
                elif self.guess[i] in self.word and self.guess[i] != self.word[i]:
                    self.grid[i] = self.guess[i]
                else:
                    self.grid[i] = self.guess[i].upper()
            print(f'Guess {self.guesses} out of 5')
            print(str(self.grid))
            print('Letters left:')
            print(str(self.remaining))



if __name__ == '__main__':
    game = wordle()
    game.play()
