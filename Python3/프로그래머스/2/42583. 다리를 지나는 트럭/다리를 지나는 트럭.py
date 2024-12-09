from collections import deque
def solution(b_len, w_lim, trucks):
    trucks, bridge = deque(trucks), deque([0]*b_len)
    time, w_sum, arrv, l = 0, 0, 0, len(trucks)
    while arrv != l:
        if trucks and trucks[0] + w_sum <= w_lim:
            front = bridge.popleft()
            if front != 0: 
                arrv += 1
                w_sum -= front
            targ = trucks.popleft()
            bridge.append(targ)
            w_sum += targ
        else:
            front = bridge.popleft()
            if front != 0: 
                arrv += 1
                w_sum -= front
            if trucks and trucks[0] + w_sum <= w_lim:
                targ = trucks.popleft()
                bridge.append(targ)
                w_sum += targ
            else:
                bridge.append(0)
        # print(f'timeframe:{time}, arrived:{arrv}, onthebridge:{bridge}')
        time += 1
    return time