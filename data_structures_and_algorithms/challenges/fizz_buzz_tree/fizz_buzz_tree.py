def FizzBuzzTree(Ktree):
    new_tree=[]
    for i in Ktree:
        new_tree.append(i)
    for index,i in enumerate(new_tree):
        if i%3 == 0 and i%5 == 0:
            new_tree[index] = 'FizzBuzz'
        elif i%3 == 0:
            new_tree[index] = 'Fizz'
        elif i%5 == 0:
            new_tree[index] = 'Buzz'
        else:
            new_tree[index] = f'{i}'
    return new_tree
        


if __name__ == "__main__":
    print(FizzBuzzTree([1,2,4,5,3,4,9,5,2,3,15]))