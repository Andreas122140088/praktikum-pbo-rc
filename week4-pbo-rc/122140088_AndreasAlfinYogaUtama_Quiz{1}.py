import random

def hangman_game():
  words = [
      'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler',
      'debugger', 'encryption', 'framework', 'function', 'garbage', 'hash',
      'index', 'iterator', 'javascript', 'json', 'library', 'loop',
      'namespace', 'object', 'operator', 'overload', 'polymorphism', 'queue',
      'recursion', 'serialization', 'stack', 'template', 'variable', 'virtual',
      'web', 'xml', 'yaml', 'zip'
  ]
  stages = ["""
      ------
      |    |
      |
      |
      |
      |
      |
  ------------
  """, """
      ------
      |    |
      |    O
      |
      |
      |
      |
  ------------
  """, """
      ------
      |    |
      |    O
      |    |
      |    |
      |
      |
  ------------
  """, """
      ------
      |    |
      |    O
      |    |
      |    |
      |   /
      |
  ------------
  """, """
      ------
      |    |
      |    O
      |    |
      |    |
      |   / \\
      |
  ------------
  """, """
      ------
      |    |
      |    O
      |  --|
      |    |
      |   / \\
      |
  ------------
  """, """
      ------
      |    |
      |    O
      |  --|--
      |    |
      |   / \\
      |
  ------------
  """]

  chosen_word = random.choice(words)
  word_length = len(chosen_word)
  guessed_word = ["_" for _ in range(word_length)]
  attempts = 6

  while attempts > 0 and "_" in guessed_word:
    for x in range(word_length):
      print(guessed_word[x], end=" ")
    print("\n")

    letter = input("Guess a letter: ")
    letter = letter.lower()
    if letter in chosen_word:
      for index, char in enumerate(chosen_word):
        if char == letter:
          guessed_word[index] = letter
      print("Correct! Keep going!")
      print(stages[6 - attempts])
    else:
      attempts -= 1
      print(f"Incorrect! Attempts left: {attempts}")
      print(stages[6 - attempts])

  if "_" not in guessed_word:
    for x in range(word_length):
      print(guessed_word[x], end=" ")
    print("\n")
    print("Congratulations! You guessed the word.")
  else:
    print("Sorry, you've run out of attempts. The word was:", chosen_word)


hangman_game()
