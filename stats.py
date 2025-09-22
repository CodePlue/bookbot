
def word_count(text):
    count =  len(text.split())
    return count

def sort_on(items):
    return items["num"]

def character_count(text):
    lower = text.lower().split()

    dictionary = {}

    for word in lower:
        for letter in word:
            dictionary[letter] = dictionary.get(letter,0) + 1 
   
    # for word in lower:
    #     for letter in word:
    #         dictionary[letter] += 1
    
    
    return dictionary

def dict_to_list(dict):
    for letter in dict:
        return dict[letter]

def dict_format(dict):
    temp = []
    for key, value in dict.items():
        temp.append({"char": key, "num": value})
    return temp 
