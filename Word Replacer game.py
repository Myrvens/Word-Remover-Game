def replace_word():
    print("Welcome to the Word Replacer Game! ")
    print("Let's have fun playing \n")
    
    # Initial sentence
    sentence = "Hi guys, I am Myrvens, and yes yes yes you are currently playing!"
    print(f"Original Sentence: \"{sentence}\"")
    
    # User input for word replacement
    word_to_replace = input("Enter the word you'd like to replace: ")
    word_replacement = input(" Enter the fun new word to replace it with: ")
    
    # Replacing words and showing the updated sentence
    new_sentence = sentence.replace(word_to_replace, word_replacement)
    print("\n Here’s your updated sentence! ")
    print(f"\"{new_sentence}\"")

    # A playful ending
    print("\nThanks for playing the Word Replacer Game!")

# Call the function
replace_word()
