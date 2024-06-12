"""TWO POINTERS TECHNIQUES """

"""This code involves two pointers one moves from left to right (leftPointer) and the other moves from right to left (rightPointer) moving towards the centre.
    it adds up the value each pointer stores, and checks if the summation is equal to a target value, else it keeps moving till it finds the value"""

def Two_sums(lst, target):
    # array = [2, 3, 4, 5, 6]  # Sample array, not used in the function
    lst.sort()  # Sort the list to use the two-pointer technique
    leftPointer = 0  # Initialize the left pointer to the start of the list
    rightPointer = len(lst) - 1  # Initialize the right pointer to the end of the list
    # running = True  # Unused variable from previous version

    # Loop until the left pointer is less than the right pointer
    while(leftPointer < rightPointer):
        add = lst[leftPointer] + lst[rightPointer]  # Calculate the sum of values at both pointers
        if add < target:  # If the sum is less than the target
            leftPointer += 1  # Move the left pointer to the right
        elif add > target:  # If the sum is greater than the target
            rightPointer -= 1  # Move the right pointer to the left
        else:  # If the sum is equal to the target
            print(f"[{lst[leftPointer]}, {lst[rightPointer]}] = {target}")  # Print the pair
            return  # Exit the function after finding the pair

    # If no pair is found after the loop, print the following message
    print("No pair found that adds up to the target")

# Call the function with a sample list and target value
Two_sums([7, 3, 9, 5, 14], 8)
