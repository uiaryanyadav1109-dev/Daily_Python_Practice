# Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
def merge_list(list1, list2): 
    result_list=[]
    #odd numbers from the first list
    for num in list1:
        if num%2 != 0:
            result_list.append(num)

    #even numbers from the second list
    for num in list2:
        if num%2 == 0:
             result_list.append(num)
    return result_list
print("result list:", merge_list(list1, list2))    