def solution(n, w, num):
    quotient = num // w
    remainder = num % w
    tot_quot = n // w
    tot_rem = n % w
    odd_layer = 1 if tot_rem != 0 else 0
    
    target_layer = quotient if remainder != 0 or num < w else quotient - 1 # 0-base
    target_layer_direction = 'left' if target_layer % 2 != 0 else 'right'
    target_pos = remainder if remainder != 0 else w # 1-base
    
    next_targ = num
    next_dir = target_layer_direction
    count = 1
    for l in range(tot_quot + odd_layer - target_layer):
        next_targ += ((w - target_pos) * 2 + 1)
        # print(f"next_target: {next_targ}", end=" ")
        target_pos = w - target_pos + 1
        # print(f"at {target_pos}", end=" ")
        count += int(next_targ <= n)
        # print(f"count: {count}")
        
    #13
    #12 #11 #10
    #7  #8  #9
    #6  #5  #4
    #1  #2  #3
    
    return count