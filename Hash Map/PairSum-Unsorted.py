class PAriSumUnsorted:
    '''x+y = target
    y=target-x
    since they ask to return indexes we cannot sort the array. we can sort a copy of the array 
    and use two pointer approach but that will take extra space.
    we can use hash map to store the elements as we iterate through the array.
    for each element we check if target-element exists in the hash map. 
        if it exists we return the indexes.
    else we add the element to the hash map and continue.'''

    @staticmethod
    def Unsorted(arr, target):
        hash={}
        for i,num in enumerate(arr):
            complement = target - num
            if complement in hash:
                return [hash[complement], i]
            hash[num] = i
        return []
    
if __name__ == "__main__":
    arr = [10, 7, 11, 15]
    target = 22
    result = PAriSumUnsorted.Unsorted(arr, target)
        
    '''
    Time Complexity: O(n) where n is the number of elements in the array.
    Space Complexity: O(n) for the hash map.'''