from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    res_dict = {}
    for char in word:
        if char in res_dict:
            res_dict[char] = res_dict[char] + 1
        else:
            res_dict[char] = 1
    return res_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
