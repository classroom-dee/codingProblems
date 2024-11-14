from collections import deque
fatigue = {
    'diamond': {'diamond': 1, 'iron': 1, 'stone': 1},
    'iron': {'diamond': 5, 'iron': 1, 'stone': 1},
    'stone': {'diamond':25, 'iron':5, 'stone':1}
    }
def solution(picks, minerals):
    results = []
    picks_dict = {'diamond': picks[0], 'iron': picks[1], 'stone': picks[2]}
    for pick in picks_dict:
        if picks_dict[pick] > 0:
            results.append(search(pick, picks_dict.copy(), minerals))
    return min(results)

def search(starter, picks, minerals):
    n_rocks = len(minerals)
    min_fatigue = float('inf')
    
    # pick type, target mineral, current fatigue
    q = deque([(starter, 0, 0, picks.copy())])

    # while there's job: if only...lol
    while q:
        pick, rock_idx, curr_fat, avail_picks = q.popleft()
        # print(pick, rock_idx, curr_fat, avail_picks)
        local_fat = curr_fat

        # use it to exhaustion: 5 times, or until no mineral left
        times_mined = 0

        while rock_idx < n_rocks and times_mined < 5:
            mineral = minerals[rock_idx]
            local_fat += fatigue[pick][mineral]
            # curr_fat += fatigue[pick][mineral]
            times_mined += 1
            rock_idx += 1

        # used up subtraction
        avail_picks[pick] -= 1

        # print(rock_idx, n_rocks, local_fat)
        if rock_idx >= n_rocks or avail_picks['diamond'] + avail_picks['iron'] + avail_picks['stone'] == 0:
            # conclude with min fatigue
            min_fatigue = min(min_fatigue, local_fat)
        else:
            # add next potential picks
            for candidate in avail_picks:
                if avail_picks[candidate] > 0:
                    q.append((candidate, rock_idx, local_fat, avail_picks.copy()))
    return min_fatigue