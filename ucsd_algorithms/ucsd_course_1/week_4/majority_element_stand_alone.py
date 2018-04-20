#tHink from top to bottom. When nums have two partitions, and we already know a is the majority element of the first partition (line 11) and b is the majority element of the second partition (line 12). If c is the majority element, then either:
#a == b == c, i.e., c is the majority element in both partitions
#a != b. then c must be equal to either a or b. 
#We can prove 2 by contradiction. If c != a and c != b, then c is not the majority element in either partition. That means, occurrences(c in 1st partition) <= len(1st partition)/2 and occurrences(c in 2nd partition) <= len(2nd partition)/2. Therefore, occurences(c in nums) <= len(nums)/2, which contradicts with the fact that c is the majority element. So we recursively can prove the correctness of every level of divide-and-conquer.

def majorityElement(nums):
    # if 0 or 1 length return the obvious
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    
    # keep breaking it down, first and second halves
    a_array = nums[:len(nums)//2]
    b_array = nums[len(nums)//2:]
    a = majorityElement(a_array)
    b = majorityElement(b_array)
    #print('a {} and b {}'.format(a, b))

    if a == b:
        return a
    else:
        # checks count of a(which is a single digit) if > length//2 return a - why even do the
        # recursion, you can just iterate the list and run the count on the iterated element
        return a if nums.count(a) > len(nums)/2 else b


def majorityElement_2(myList):
    length = len(myList)

    if length == 1:
        return myList[0]
    if length == 0:
        return -1
    
    a_array = myList[:len(myList)//2]
    b_array = myList[len(myList)//2:]

    ML = majorityElement_2(a_array)
    MR = majorityElement_2(b_array)

    if ML == MR:
        return ML
    if ML >= 0 and MR == -1:
        return ML
    elif ML == -1 and MR >= 0:
        return MR
    else:
        return -1

    return ML if myList.count(ML) > len(myList) else MR



A = [3, 3, 1, 3, 1, 1, 3, 1]; #Our array
#A = [1, 1, 2, 2, 3, 3, 4, 4]
print('majorityElement {}'.format(majorityElement(A)))
print('majorityElement_2 {}'.format(majorityElement_2(A)))
