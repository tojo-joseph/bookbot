def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    character_list, dict_list = get_char_count(text)
    dict_list.sort(reverse=True, key=sort_on)
    print_report(dict_list)
    print(f"--- End report ---")
    
    



def get_char_count(text):
    list_of_words = text.split()
    
    character_dict = {}
    new_list = []
    for word in list_of_words:
        for character in word:
            character = character.lower()
            if character.isalpha():
                if character not in character_dict:
                    character_dict[character] = 1
                else:
                    character_dict[character] += 1
    
    for dict_entry in character_dict:
        updated_dict = {}
        updated_dict["name"] = dict_entry
        updated_dict["num"] = character_dict[dict_entry]
        new_list.append(updated_dict)
            
        
    
    return character_dict, new_list




        

def sort_on(dict):
    return dict["num"]

def print_report(latest_dict):
    for element in latest_dict:
        print(f"The '{element['name']}' character was found {element['num']} times")
    
    return latest_dict




def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def get_book_text(path):    
    with open(path) as f:
        return f.read()


main()