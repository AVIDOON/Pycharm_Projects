# A = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
def binary_search(low, high, middle):

      if a > A[middle]:
        print(a, "is greater than", A[middle])
        low = middle + 1
        middle = int((high + low)/2)
        return binary_search(low, high, middle)

      if a < A[middle]:
        print(a, "is Less than", A[middle])
        high = middle - 1
        middle = int((high + low)/2)
        return  binary_search(low, high, middle)

      if a == A[middle]:
          print("Finally in the middle")
          return middle


A = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# search for 23
a = int(input("Enter the number you want to search : "))

low = 0
high = len(A) - 1
middle = int((low + high)/2)
index = binary_search(low, high, middle)
print("no is found at " + str(index + 1) + "th positon.")

