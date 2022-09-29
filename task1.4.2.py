import sys 

class Box:
    def __init__(self, box_id, len_x, len_y, len_z, x, y, z):
        self.id = box_id
        self.len_x = len_x
        self.len_y = len_y
        self.len_z = len_z
        self.x = x
        self.y = y
        self.z = z


class FreeSpace:
    def __init__(self, len_x, len_y, len_z, x, y, z):
        self.len_x = len_x
        self.len_y = len_y
        self.len_z = len_z
        self.x = x
        self.y = y
        self.z = z
        

def place_boxes():
    lines=sys.stdin.readlines()
    l=lines[0].split()
    area_x=int(l[0])
    area_y=int(l[1])
    area_z=int(l[2])
    no_of_boxes =int(lines[1])
    boxes=[]
    free_spaces = []
    whole_space = FreeSpace(area_x, area_y, area_z, 0, 0, 0)
    free_spaces.append(whole_space)
    for i in range(2,no_of_boxes+2):
        values = lines[i].split()
        len_x = int(values[0])
        len_y = int(values[1])
        len_z = int(values[2])
        box = Box(i-2,len_x, len_y, len_z, -1, -1, -1)
        boxes.append(box)

    boxes.sort(key=lambda x:x.len_y)
    boxes.reverse()

    values_y = []
    for box in boxes:
        if box.len_y not in values_y:
            values_y.append(box.len_y)

    for val_y in values_y:
        s = 0
        k = 0
        for i in range(len(boxes)-1):
            if boxes[i].len_y == val_y:
                s = i
                break
        for k in range(len(boxes[s:])):
            if boxes[k+s].len_y != val_y:
                boxes[s:k+s] = boxes[s:k+s][::-1]
                break
            elif k+s == len(boxes)-1:
                boxes[s:k+s+1] = boxes[s:k+s+1][::-1]
                break

    for box in boxes:
        print(box.id, box.len_x, box.len_y, box.len_z)
        
    for box in boxes:
        free_spaces = sorted(sorted(sorted(free_spaces, key=lambda x:x.x), key=lambda x:x.y), key=lambda x:x.z)
        for space in free_spaces:
            if box.len_y <= space.len_y and box.len_x <= space.len_x and box.len_z <= space.len_z:
                box.x = space.x
                box.y = space.y
                box.z = space.z
                new_space_x = space.len_x - box.len_x
                new_space_y = space.len_y - box.len_y
                new_space_z = space.len_z - box.len_z
                # Program creates new Free Space objects that were creating from putting box into previous free space
                # and adds them to the array of free spaces. 
                space_right = FreeSpace(new_space_x, box.len_y, box.len_z, space.x + box.len_x, space.y, space.z)
                space_above = FreeSpace(space.len_x, new_space_y, box.len_z, space.x, space.y + box.len_y, space.z)
                space_up = FreeSpace(space.len_x, space.len_y, new_space_z, space.x, space.y, space.z + box.len_z)
                free_spaces.append(space_up)
                free_spaces.append(space_right)
                free_spaces.append(space_above)
                free_spaces.pop(free_spaces.index(space))
                break
