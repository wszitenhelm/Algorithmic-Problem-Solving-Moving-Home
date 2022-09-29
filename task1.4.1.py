import sys
import time 


# This class was created to keep track of box's size and coordinates
# to be able to comprare it with FreeSpace's size.
class Box:
    def __init__(self, box_id, len_x, len_y, len_z, x, y, z):
        self.id = box_id
        self.len_x = len_x
        self.len_y = len_y
        self.len_z = len_z
        self.x = x
        self.y = y
        self.z = z


# This class creates free spaces and assign size and coordinates to them.
class FreeSpace:
    def __init__(self, len_x, len_y, len_z, x, y, z):
        self.len_x = len_x
        self.len_y = len_y
        self.len_z = len_z
        self.x = x
        self.y = y
        self.z = z



        
# Main program of this task that firstly reads the input,
# then create Box objects and adds them to te array.
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

    # Sorting boxes by x what was the main aim in this task.
    boxes.sort(key=lambda x:x.len_x)
    boxes.reverse()

    # Ensuring that order of receiving boxes after sorting is kept.
    values_x = []
    for box in boxes:
        if box.len_x not in values_x:
            values_x.append(box.len_x)

    for val_x in values_x:
        s = 0
        k = 0
        for i in range(len(boxes)-1):
            if boxes[i].len_x == val_x:
                s = i
                break
        for k in range(len(boxes[s:])):
            if boxes[k+s].len_x != val_x:
                boxes[s:k+s] = boxes[s:k+s][::-1]
                break
            elif k+s == len(boxes)-1:
                boxes[s:k+s+1] = boxes[s:k+s+1][::-1]
                break
            
    print("order of placing boxes: ")        
    for box in boxes:
        print(box.id, box.len_x, box.len_y)

    # Here program loops through the all boxes to find space for all of them    
    for box in boxes:
        # Sorting of free spaces to have a proper order of free spaces and be able to select
        # space on the right before space above.  

        free_spaces = sorted(sorted(sorted(free_spaces, key=lambda x:x.x), key=lambda x:x.y), key=lambda x:x.z)
        
        # Here program loops through the all free spaces and checks if space's sizes are big enough to find a space for the box        
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
            
    # Sorting boxes by id and printing output        
##    boxes.sort(key=lambda x:x.id)
##    print("placed boxes: ")
##    for box in boxes:
##        print(box.id, box.x, box.y, box.z)


    free_ = 0
    whole_area = area_x * area_y * area_z
    #print(whole_area)
    for space in free_spaces:
        free_ = free_ + (space.len_x * space.len_y * space.len_z)

    wasted = free_ / whole_area

    boxess = len(boxes)

    fitted = 0
    for box in boxes:
        if box.x != -1:
            fitted += 1

    per = fitted/boxess
    print(f"no of boxes to be fitted: {boxess}")
    print(f"boxes fitted: {fitted}")
    print(f"available volume: {whole_area}")
    print(f"volume left : {free_}")

        


start = time.time()
place_boxes()
end = time.time()
total = end - start
print(f"time: {total}")



    


