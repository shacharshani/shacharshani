def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    pair_counter = 0
    i = 1
    while i<len(word):
        if word[i] == word[i-1]:
            pair_counter = pair_counter + 1 # pair_counter += 1
            i += 1
            if pair_counter == 3:
                return True
        else:
            pair_counter = 0
        i+=1
    return False

if __name__ == "__main__":
    my_word = 'abdfddf'
    result = trifeca(my_word)
    print("Result: ", result)