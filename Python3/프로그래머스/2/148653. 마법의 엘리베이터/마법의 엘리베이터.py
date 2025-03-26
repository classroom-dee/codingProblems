# # not-storey-it's-called-floor-problem
# def solution(floor):
#     div = 10
#     pushed = 0
#     prev = 0
#     while floor >= div or div == 10:
#         rem = (floor % div) - prev
#         if rem > 5 * (div // 10):
#             pushed = pushed + (div - rem) // (div // 10) if div > 10 else pushed + (div - rem)
            
#             floor += div
#         else:
#             pushed += rem // (div // 10)
#         prev += rem
#         div *= 10
#     # account for the first digit
#     last = floor // (div // 10)
#     return pushed + last

def solution(floor):
    pushed = 0 
    carry = 0 # rem tracker
    place = 1 # multiples

    while floor > 0 or carry > 0:  
        digit = (floor % 10) + carry 
        
        if digit > 5:  
            pushed += (10 - digit)  
            carry = 1  
        elif digit < 5: 
            pushed += digit  
            carry = 0 
        else:  
            if (floor // 10) % 10 >= 5: 
                pushed += (10 - digit) 
                carry = 1
            else:
                pushed += digit 
                carry = 0

        floor //= 10  
        place *= 10 

    return pushed