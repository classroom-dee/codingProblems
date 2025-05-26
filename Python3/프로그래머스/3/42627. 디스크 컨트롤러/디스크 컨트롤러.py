import heapq
# request time, time required to fin
def solution(jobs):
    # Sort jobs by request time first
    jobs.sort()
    # print("order of jobs: ", jobs)
    n = len(jobs)
    time = 0  # Current time
    i = 0     # Index for jobs list
    total_turnaround = 0
    heap = []  # Priority queue: (duration, request_time, job_id)

    job_id = 0  # To handle tie-breaking by job order (job_id)

    while i < n or heap:
        # Push all jobs that have arrived by the current time into the heap
        while i < n and jobs[i][0] <= time:
            request_time, duration = jobs[i]
            heapq.heappush(heap, (duration, request_time, job_id))
            job_id += 1
            i += 1

        if heap:
            # Pop the highest-priority job .. 
            duration, request_time, _, = heapq.heappop(heap)
            time += duration  # Advance time by job's duration
            turnaround = time - request_time  # Completion time - arrival time
            total_turnaround += turnaround
        else:
            # If no job is available to process, jump to the next job's request time
            time = jobs[i][0]

    return total_turnaround // n  # Return the integer part of average