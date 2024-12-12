def count_words(string):
    words = string.split()
    count = 0.
    for word in words:
        count += 1.
    return count
def count_characters(string):
  char_counts = {}
  for char in string.lower():
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1
  return char_counts



def main():
    
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = count_words(file_contents)
    characters = count_characters(file_contents)

    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{num_words} words found in the document")
    for w in sorted(characters, key=characters.get, reverse=True):
        #print(w, characters[w])
        print(f"The '{w}' character appears {characters[w]} times")
if __name__=="__main__":
    main()
