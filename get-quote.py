import random
def Primary():
 #  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, last)
  print(quotes [0])

if __name__== "__Primary__":
  Primary()
