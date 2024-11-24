def main():
    letters_dic = {}
    #count the number of letters
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count = len(file_contents.split())
    print(f"{count} words in the book")
#count the number of times each letter occurs
    
    lowered_string = file_contents.lower()

    # Iterate over each character in the string
    for letter in lowered_string:
    # Check if the character is in the dictionary
        if letter in letters_dic:
        # Increment the count if it exists
            letters_dic[letter] += 1
        else:
        # Initialize the count if it's not in the dictionary
            letters_dic[letter] = 1
    print(letters_dic)    
main()