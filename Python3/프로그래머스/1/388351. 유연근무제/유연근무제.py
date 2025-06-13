def solution(schedules, timelogs, startday):
    def to_true_target(time):
        hrs = time // 100
        mins = time % 100
        mins += 10
        if mins >= 60:
            mins -= 60
            hrs += 1
        hrs %= 24
        return hrs * 100 + mins
    def emp_reducer(emp_info):
        target_time = emp_info[0]
        true_target = to_true_target(target_time)
        # print(true_target)
        actual_times = emp_info[1]
        days = 1
        current = startday
        isIn = True
        while days < 8:
            if (true_target < actual_times[days-1]) and not (current == 6 or current == 7):
                # print(f"target time: {true_target}, actual time: {actual_times[days-1]} day: {current}")
                isIn = False
                break
            current = (current % 7) + 1
            days += 1
        return isIn
    return sum(map(emp_reducer, zip(schedules, timelogs)))