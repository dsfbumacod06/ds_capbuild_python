'''
Allocation

Inputs
Number of Test Cases
 - - - - Test Case 1 - - - 
 N, B
 A1 A2 . . . An
 up to Test Case N
'''


def allocation(T):
    case_houses = []
    while T > 0:
        prices,houses = [],0
        N,B = map(int,input().split())
        prices.extend(map(int,input().split()))
        if len(prices) > N:
            raise Exception("Too many prices entered.")
        for price in sorted(prices):
            if B >= price:
                B = B - price
                houses += 1
        case_houses.append(houses)
        T -= 1
    return case_houses



if __name__ == "__main__":
    T = int(input()) # number of test cases.
    print(allocation(T))