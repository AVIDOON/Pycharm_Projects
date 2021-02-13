# def list_doubler(my_list):
#     doubler = []
#
# my_list = [1,2,3,4,5,6]
# doubled_list = list_doubler(my_list)
# print(doubled_list)


# def list_doubler(my_list):
#      doubled = [num * 2 for num in my_list]
#      return doubled
#
# my_list = [1,2,3,4,5,6]
# doubled_list = list_doubler(my_list)
# print(doubled_list)

#
# def list_doubler(my_list):
#      return [num * 2 for num in my_list]
#
# my_list = [1,2,3,4,5,6]
# doubled_list = list_doubler(my_list)
# print(doubled_list)


#
# def long_words(lst):
#     words = []
#     for word in lst:
#         if len(word) > 5:
#            words.append(word)
#     return words
#
# lst = ['mango', 'orange', 'papaya', 'grapes']
# print(long_words(lst))

#
#
# def long_words(lst):
#     return [word for word in lst if len(word) > 5]
#
# lst = ['mango', 'orange', 'papaya', 'grapes']
# print(long_words(lst))


# def tri_recursion(k):
# 	if(k>0):
# 		result = k + tri_recursion(k-1)
# 		print(result)
# 	else:
# 		result = 0
#        return r


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

tri_recursion(6)