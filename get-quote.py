def Primary():
   print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)

if __name__== "__Primary__":
  Primary()
