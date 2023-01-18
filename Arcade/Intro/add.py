# Write a function that returns the sum of two numbers.

def solution(param1, param2):
   return param1 + param2

# Driver code
if __name__=='__main__':

    param1 = int(input('param1: '))
    param2 = int(input('param2: '))
    
    result = solution(param1,param2)
    print(f'The sum is: {result}')
