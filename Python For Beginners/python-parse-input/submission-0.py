from typing import List

def read_integers() -> List[int]:
    user_input = input()
    res = []
    for num_str in user_input.split(","):
        res.append(int(num_str))
    return res

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
