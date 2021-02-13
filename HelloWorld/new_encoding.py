def assign_values(x,l1,list1,list2):
    my_dict = {}
    for i in range(l1):
           my_dict[list1[i]] = list2[i]
    return my_dict[x]

if __name__ == '__main__':
    word1 = input()
    word2 = input()
    new_word1 = input()

    list1 = []
    list2 = []
    for w in word1:
     list1.append(w)
    for v in word2:
     list2.append(v)
    l1 = len(list1)
    for x in new_word1:
        print(assign_values(x,l1,list1,list2),end='')
