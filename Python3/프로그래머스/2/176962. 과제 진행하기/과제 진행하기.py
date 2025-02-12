# from datetime import datetime, timedelta
# from collections import deque
# def str_to_time(tstr):
#     return datetime.strptime(tstr, "%H:%M")

# def solution(планы):
#     # sort by start asc
#     планы.sort(key=lambda x: str_to_time(x[1]))

#     complete = []
#     putoff = deque()

#     curr_task = None
#     curr_end_time = None

#     i = 0

#     while i < len(планы) or putoff or curr_task:
#         next_task = планы[i] if i < len(планы) else None
#         print(next_task)

#         if curr_task:
#             # new task starts before curr task ends?
#             if next_task and str_to_time(next_task[1]) < curr_end_time:
#                 # put off
#                 rem_time = int((curr_end_time - str_to_time(next_task[1])).total_seconds() / 60)
#                 putoff.append((curr_task[0], rem_time))
#                 curr_task = next_task
#                 curr_end_time = str_to_time(next_task[1]) + timedelta(minutes=int(next_task[2]))
#                 i += 1 # next task
#             elif next_task and str_to_time(next_task[1]) == curr_end_time: # exactly the same time
#                 complete.append(curr_task[0])
#                 curr_task = next_task
#                 curr_end_time = str_to_time(next_task[1]) + timedelta(minutes=int(next_task[2]))
#                 i += 1
#             else: # complete curr task if it ends before nxt
#                 complete.append(curr_task[0])
#                 curr_task = None
#         elif next_task: # available task
#             curr_task = next_task
#             curr_end_time = str_to_time(next_task[1]) + timedelta(minutes=int(next_task[2]))
#             i += 1 # next!
#         elif putoff: # if there's putoff task left
#             task_name, rem_time = putoff.pop()
#             curr_task = (task_name, "dummy", rem_time) # pseudo task
#             curr_end_time = datetime.now() + timedelta(minutes=rem_time)
#         else: # every task is done
#             break
#     if curr_task: # leftover check?
#         complete.append(curr_task[0])
#     return complete
from typing import List

def solution(tasks: List[List[str]]) -> List[str]:
    # Helper function to convert time in "HH:MM" format to minutes since midnight
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes
    
    # Sort tasks by start time
    tasks = sorted(tasks, key=lambda x: time_to_minutes(x[1]))
    
    # Initialize variables
    result = []  # to store the names of finished tasks in order
    stack = []  # LIFO stack to hold put-off tasks
    current_time = 0  # keeps track of the current time in minutes since midnight
    i = 0  # index for iterating over sorted tasks

    while i < len(tasks) or stack:
        # Load the next task or pop from the stack if all scheduled tasks are done
        if stack and (i >= len(tasks) or current_time < time_to_minutes(tasks[i][1])):
            task_name, start_time, duration = stack.pop()
        else:
            task_name, start_time, duration = tasks[i]
            i += 1
            current_time = max(current_time, time_to_minutes(start_time))
        
        duration = int(duration)
        
        # Calculate the end time of the current task
        end_time = current_time + duration
        
        # Check if another task starts during the current task
        while i < len(tasks) and time_to_minutes(tasks[i][1]) < end_time:
            # If a new task starts, put off the current task
            stack.append((task_name, start_time, end_time - time_to_minutes(tasks[i][1])))
            task_name, start_time, duration = tasks[i]
            current_time = time_to_minutes(start_time)
            end_time = current_time + int(duration)
            i += 1

        # If no more interruptions, finish the current task
        result.append(task_name)
        current_time = end_time

    return result