# import data_structures_and_algorithms.data_structures.linked_list.linked_list

def zipLists(first_l,sec_l):
    if type(first_l) != list or type(sec_l) != list:
        return "invalid input"
    '''
    this function takes in two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
    '''
    a=len(first_l)+len(sec_l)
    n=0
    count=1
    t=True
    while True:
        if t:
            first_l.insert(count,sec_l[n])
            count+=1
            n+=1
            t=False
        else:
            first_l.insert(count+n,sec_l[n])
            count+=1
            n+=1

        if len(first_l) == a:
            return first_l

if __name__ == "__main__":
    pass
    print(zipLists([1,2,3,4,5,6],[1,2,3,4,5,6,7,8,9]))
