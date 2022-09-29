import sys
import time


# This class was created to keep track of box's size and coordinates
# to be able to comprare it with FreeSpace's size.
class Box:
    def __init__(self, box_id, len_x, len_y, x, y, z):
        self.id = box_id
        self.len_x = len_x
        self.len_y = len_y
        self.x = x
        self.y = y
        self.z = z


# This class creates free spaces and assign size and coordinates to them.
class FreeSpace:
    def __init__(self, len_x, len_y, x, y):
        self.len_x = len_x
        self.len_y = len_y
        self.x = x
        self.y = y
        
        
# Main program of this task that firstly reads the input,
# then create Box objects and adds them to te array.
def place_boxes():
    lines=sys.stdin.readlines()
    l=lines[0].split()
    area_x=int(l[0])
    area_y=int(l[1])
    no_of_boxes =int(lines[1])
    boxes=[]
    free_spaces = []
    whole_space = FreeSpace(area_x, area_y, 0, 0)
    free_spaces.append(whole_space)
    for i in range(2,no_of_boxes+2):
        values = lines[i].split()
        len_x = int(values[0])
        len_y = int(values[1])
        box = Box(i-2,len_x, len_y, -1, -1, -1)
        boxes.append(box)

    # Sorting boxes by the area what was the main aim in this task.
    boxes.sort(key=lambda x:x.len_x*x.len_y)
    boxes.reverse()

    # Ensuring that order of receiving boxes after sorting is kept.
    values_v = []
    for box in boxes:
        if box.len_x * box.len_y not in values_v:
            values_v.append(box.len_x * box.len_y)
    for val_v in values_v:
        s = 0
        k = 0
        for i in range(len(boxes)-1):
            if boxes[i].len_x*boxes[i].len_y == val_v:
                s = i
                break
        for k in range(len(boxes[s:])):
            if boxes[k+s].len_x * boxes[k+s].len_y != val_v:
                boxes[s:k+s] = boxes[s:k+s][::-1]
                break
            elif k+s == len(boxes)-1:
                boxes[s:k+s+1] = boxes[s:k+s+1][::-1]
                break
            
    # Here program loops through the all boxes to find space for all of them           
    for box in boxes:
        # Sorting of free spaces to have a proper order of free spaces and be able to select
        # space on the right before space above.        
        free_spaces.sort(key=lambda x:x.len_y*x.len_x)
        # Here program loops through the all free spaces and checks if space's sizes are big enough to find a space for the box        
        for space in free_spaces:
            if box.len_y <= space.len_y and box.len_x <= space.len_x:
                box.x = space.x
                box.y = space.y
                box.z = 0
                new_space_x = space.len_x - box.len_x
                new_space_y = space.len_y - box.len_y
                # Program creates new Free Space objects that were creating from putting box into previous free space
                # and adds them to the array of free spaces. 
                space_right = FreeSpace(new_space_x, box.len_y, space.x + box.len_x, space.y)
                space_above = FreeSpace(space.len_x, new_space_y, space.x, space.y + box.len_y)
                free_spaces.append(space_right)
                free_spaces.append(space_above)
                space.len_x = 0
                space.len_y = 0
                break
            # Cheking box and free space once again after rotating box
            elif box.len_x <= space.len_y and box.len_y <= space.len_x:
                box.x = space.x
                box.y = space.y
                box.z = 0
                new_space_x = space.len_x - box.len_y
                new_space_y = space.len_y - box.len_x
                space_right = FreeSpace(new_space_x, box.len_x, space.x, space.y+box.len_x)
                space_above = FreeSpace(space.len_x, new_space_y, space.x, space.y + box.len_y)
                free_spaces.append(space_right)
                free_spaces.append(space_above)
                space.len_x = 0
                space.len_y = 0
                break 

    # Sorting boxes by id and printing output
##    boxes.sort(key=lambda x:x.id)   
##    for box in boxes:
##        print(box.id, box.x, box.y, box.z)

    # Testing methods (time and area that was not used)   
    free_ = 0
    whole_area = area_x * area_y
    #print(whole_area)
    for space in free_spaces:
        free_ = free_ + (space.len_x * space.len_y)

    wasted = free_ / whole_area

    boxess = len(boxes)

    fitted = 0
    for box in boxes:
        if box.x != -1:
            fitted += 1

    per = fitted/boxess
    print(f"no of boxes to be fitted: {boxess}")
    print(f"boxes fitted: {fitted}")
    print(f"boxes fitted %: {per}")
    print(f"available area: {whole_area}")
    print(f"space left : {free_}")
    print(f"space left % : {wasted}")
    
start = time.time()
place_boxes()
end = time.time()
total = end - start
print(f"time: {total}")


    


