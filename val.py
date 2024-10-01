n = int(input())
data_dict = {}

for i in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a = query[1]
        b = query[2]
        
        add_element = True
        keys_to_delete = []
        for key in data_dict:
            if key[0] <= a and key[1] <= b:
                keys_to_delete.append(key)
            elif key[0] >= a and key[1] >= b:
                add_element = False

        for key in keys_to_delete:
            del data_dict[key]
        
        if add_element:
            data_dict[(a, b)] = None

    elif query[0] == 2:
        print(len(data_dict))
