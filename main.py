def main():
    path_of_book = "books/frankenstein.txt"
    contents = get_contents(path_of_book)

    word_count = get_word_count(contents)
    
    char_count=get_char_count(contents)
    
    char_sorted = char_sorted_list(char_count)

    print(f"---Begin report of {path_of_book}---")
    print(f"{word_count} words found in the document")
    print("\n")
    
    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("---End report---")

def get_contents(path):
    with open(path) as file:
        return file.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text = text.lower()
    chars_count={}
    for char in text:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    return chars_count

def sort_list(d):
    return d["num"]

def char_sorted_list(chars_count_dict):
    sorted_list=[]
    for ch in chars_count_dict:
        sorted_list.append({"char":ch, "num": chars_count_dict[ch]})
    sorted_list.sort(reverse=True , key=sort_list)
    return sorted_list

main()




#another mehtod to write the function
"""def main(): 
    with open(r"books/frankenstein.txt","r") as file:
        file_contents =file.read()
    print(file_contents)

main()
"""
