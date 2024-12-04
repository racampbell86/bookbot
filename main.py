def main():
    letters_dic = {}
    #count the number of letters
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_count = len(file_contents.split())
    lowered_string = file_contents.lower()
     

    # Iterate over each character in the string
    for letter in lowered_string:
    # Check if the character is in the dictionary
        if letter.isalpha():
            if letter in letters_dic:
        # Increment the count if it exists
                letters_dic[letter] += 1
            else:
        # Initialize the count if it's not in the dictionary
                letters_dic[letter] = 1
        # Convert dictionary to list of dictionaries
    char_list = []
    for letter, count in letters_dic.items():
        char_list.append({"char": letter, "num": count})
    
    # Sort the list by count (num) in descending order
    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)

    # print(f"The {name} character was found {num} times")
    print("--- Begin report of books/frankenstein.txt ---") 
    #count the number of times each letter occurs   
    print(f"{word_count} words found in the document\n")
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End report ---")

main()