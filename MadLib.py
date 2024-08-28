#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a noun: ")
  verb1 = input("Enter a verb: ")
  adjective1 = input("Enter an adjective: ")
  noun2 = input("Enter a noun: ")
  verb2 = input("Enter a verb: ")
  adjective2 = input("Enter an adjective: ")
  #Print the story with the user supplied words.
  print("I like to walk my " + noun1 + " and " + noun2 + " during the " + adjective1 + " night. " )


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
