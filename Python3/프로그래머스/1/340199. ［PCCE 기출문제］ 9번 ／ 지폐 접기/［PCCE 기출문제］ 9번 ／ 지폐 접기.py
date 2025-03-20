def solution(wallet, bill):
    answer = 0
    bill_min, bill_max, wallet_min, wallet_max = min(bill), max(bill), min(wallet), max(wallet)
    
    while bill_min > wallet_min or bill_max > wallet_max:
        
        if bill[0] == bill_max:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        
        answer += 1
        bill_min, bill_max = min(bill), max(bill)
            
    return answer
