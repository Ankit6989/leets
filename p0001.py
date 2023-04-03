# Basic Approach:(Brute force code using Two Pointers)

class Solution(object):
    def twoSum(self, nums, target):
        # Using Two pointers P1 and P2 to represent every possible pairs of the array.
        for p1 in range(len(nums)):
            for p2 in range(p1 + 1, len(nums)):
                # If one of those pairs add together equal to the target return the answer else return None.
                if nums[p1] + nums[p2] == target:
                    return [p1, p2]
        return 'None'


 # Optimized solution using Hash table

class Solution(object):
    def twoSum(self, nums, target):
        nums_map = {}
        for p in range(len(nums)):
            # Using get method to check Is the current number exist in hashmap
            current_number = nums_map.get(nums[p])
            if current_number >= 0:
                return [current_number, p]
            else:
                matched_number = target - nums[p]
                nums_map[matched_number] = p
