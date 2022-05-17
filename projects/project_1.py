# Project 1 - text pro

def sentence_phraser(phrase):
  interregatives = ("what", "why", "how", "is", "are", "was", "were")
  capitalized = phrase.capitalize()

  if phrase.startswith(interregatives):
    return "{} ? ".format(capitalized)
  else:
    return "{}.".format(capitalized)



def get_input():
  user_inputs  = []

  while True:
    user_input = input("Say something: ")
    if user_input == "/end":
      break
    else:
      user_inputs.append(sentence_phraser(user_input))
      continue

  return " ".join(user_inputs) 

print(get_input())