from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedList = sorted(nums)
        leftPointer = 0
        rightPointer = len(sortedList) - 1

        while leftPointer < rightPointer:
            add = sortedList[leftPointer] + sortedList[rightPointer]

            if add < target:
                leftPointer += 1
            elif add > target:
                rightPointer -= 1
            else:
                index1 = nums.index(sortedList[leftPointer])
                index2 = nums.index(sortedList[rightPointer])

                if index1 == index2:
                    index2 = nums.index(sortedList[rightPointer], index1 + 1)
                
                return f'{[index1, index2]} = {target}'

        # If no pair is found
        return []

# Call the method with a sample list and target value
result = Solution().twoSum([2, 3, 4, 5, 6, 7], 12)
print(result)  # Expected output: indices of the numbers summing up to 12, e.g., [4, 5]