unsorted_list = [664, 225, 23, 222, 123]

def bubblesorrt(the_list):
    high_idx = len(the_list) -1

    for i in range(high_idx):
        list_changed = False
        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                list_changed = True

            print(the_list, i, j)
        print(list_changed)
        if list_changed == False:
            break
        

bubblesorrt(unsorted_list)