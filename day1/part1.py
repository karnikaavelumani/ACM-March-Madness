with open('test.txt') as text:
    in_room = 0
    max_value = 0
    for line in text:
        if 'entered' in line:
            in_room += 1
        if 'left' in line:
            in_room -= 1
        if in_room > max_value:
            max_value = in_room
    
    print(max_value)