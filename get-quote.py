def load_all():
 #print("Keep it logically awesome.")

  quotes_file = open("quotes.txt")
  all_quotes = quotes_file.readlines()
  quotes_file.close()

  #print(all_quotes)
  print(all_quotes[-1])

if __name__== "__main__":
  load_all()