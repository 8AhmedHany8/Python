def mutate_string(string, position, character):
    #conert string to list
    llist = list(string)
    #replace character in refered position
    llist[position] = character

    string = ''.join(llist)

    return string

