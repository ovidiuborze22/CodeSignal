# Given a year, return the century it is in. 
# The first century spans from the year 1 up to and including the year 100, 
# the second - from the year 101 up to and including the year 200, etc.

def solution(year):
    return (year + 99) // 100

# Driver code
if __name__=='__main__':

    year = 1905

    print(solution(year))