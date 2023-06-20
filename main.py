import random
import hangman_words
import animation
print(animation.logo)

flow = "y"

chosen_word = random.choice(hangman_words.word_list)
guess = ''
lives = 6
predict_word = []
wrong_guess = []
length = len(chosen_word)
for j in chosen_word:
  predict_word.append('_')

while flow == "y":
  while lives > 0:
    guess = input("Guess a letter: ").lower()
    found = False

    for i in range(length):
      if guess == chosen_word[i]:
        predict_word[i] = guess
        found = True

    if not found:
        if guess not in wrong_guess:
          wrong_guess.append(guess)
          lives -= 1
        else:
          print("You alrready guessed that letter!")
          
    print(animation.stages[lives])
  
    print(predict_word)
    
    if "_" not in predict_word:
      print("YOU WIN BRO!")
      flow = input("Do you want to play again? y/n")
      chosen_word = random.choice(hangman_words.word_list)
      guess = ''
      lives = 6
      predict_word = []
      wrong_guess = []
      length = len(chosen_word)
      for j in chosen_word:
        predict_word.append('_')   
      break

  if lives == 0: 
    print("You Lose MF!")
    print("The answer is",chosen_word)
    flow = input("Do you want to play again? y/n \n")
    if flow == "y":
      chosen_word = random.choice(hangman_words.word_list)
      guess = ''
      lives = 6
      predict_word = []
      wrong_guess = []
      length = len(chosen_word)
      for j in chosen_word:
        predict_word.append('_')

