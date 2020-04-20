import random
def load_all():
 #print("Keep it logically awesome.")

  quotes_file = open("quotes.txt")
  quotes = quotes_file.readlines()
  quotes_file.close()

  number_of_lines = len(quotes)

  #print(number_of_lines -1)

  #last = 13
  rnd = random.randint(0, number_of_lines-1)
  rnd2 = random.randint(0, number_of_lines-1)

  #last = len(quotes_file) -1
  #print(quotes_file[rnd])
  #print(all_quotes)
  #print(quotes[-1])	

  print(quotes[rnd], end = '')
  print(quotes[rnd2], end ='')

if __name__== "__main__":
  load_all()