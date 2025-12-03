class LongestConsecutive:
    '''first find smallest number in the sequence,
    then check for consecutive numbers
    no sort as it would be O(n log n) time complexity
    using set for O(1) lookups
    '''

    @staticmethod
    def LongestConsecutive(nums):
        
        if not nums:
            return 0
        longestchain=0
        nums_set= set(nums)
        for num in nums:
            if num-1 not in nums_set:
                current_num = num
                longest =1
                while current_num +1 in nums_set:
                    current_num +=1
                    longest +=1
                max_len = max(longestchain, longest)
        return max_len
    
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    result = LongestConsecutive.LongestConsecutive(nums)
    print(result)
