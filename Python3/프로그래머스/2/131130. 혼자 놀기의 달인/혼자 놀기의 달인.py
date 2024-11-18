# master single player problem
def solution(cards):
    # init
    records = set() # index tracking
    groups = [] # group tracking

    # helper for grouping with starting point
    def form_group(start_idx):
        group = []
        curr_idx = start_idx

        while curr_idx not in records:
            records.add(curr_idx)
            group.append(curr_idx)
            curr_idx = cards[curr_idx - 1]
        return group
    
    # form groups by visiting nodes
    for i in range(1, len(cards) + 1):
        if i not in records:
            group = form_group(i)
            groups.append(len(group))
    
    # two largest groups?
    groups.sort(reverse=True)

    # score based decision
    if len(groups) < 2:
        return 0
    else:
        return groups[0] * groups[1]