def solution(routes):
    # sort by exit points
    routes.sort(key=lambda x: x[1])
    
    count = 0
    camera = -float('inf')
    
    for entry, exit in routes:
        # if this cam can't cover this car
        if camera < entry:
            count += 1
            camera = exit # place a new cam at the end of the curr route
    
    return count