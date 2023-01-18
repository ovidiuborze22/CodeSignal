# Given the string, check if it is a palindrome.
def solution(inputString):
    return inputString == inputString[::-1]

# Driver code
if __name__=='__main__':

    inputString = 'aabaa'

    print(solution(inputString))

# Palindrome Explanation:
# A string that doesn't changed when reversed (it reads the same backward and forward).