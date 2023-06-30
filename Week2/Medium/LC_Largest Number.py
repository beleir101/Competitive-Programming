"""
This is not even my code its a guy form leeetcode @marlen09
checked the solutons after one hour of pure struggle
I'm disgusted for not knowing magic functions and in generally with the way my brain works
"""
class LargerNumKey(str):
    def __lt__(x, y):
        # Compare x+y with y+x in reverse order to get descending order
        #print(x + y,y + x)
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        # Convert the list of numbers to list of strings
        nums = [str(num) for num in nums]
        #print(nums)
        # Sort the list of strings using our custom sorting function
        nums.sort(key=LargerNumKey)
        #print(nums)
        # Join the sorted list of strings to form the final result
        largest_num = ''.join(nums)

        # If the largest number is 0, return "0"
        # Otherwise, return the largest number
        return "0" if largest_num[0] == "0" else largest_num

trial =Solution()
print(trial.largestNumber([96,9,33,92]))