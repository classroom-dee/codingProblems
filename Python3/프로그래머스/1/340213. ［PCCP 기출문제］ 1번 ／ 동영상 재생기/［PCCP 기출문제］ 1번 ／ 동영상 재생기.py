# from datetime import datetime, timedelta
# def solution(video_len, pos, op_start, op_end, commands):
    
#     def convert(time_string):
#         return datetime.strptime(time_string, "%M:%S")
    
#     commands_dic = {
#         'prev': (lambda p: p - timedelta(seconds=10)),
#         'next': (lambda p: p + timedelta(seconds=10))
#     }
    
#     video_len, pos, op_start, op_end = convert(video_len), convert(pos), convert(op_start), convert(op_end)
#     ten, start = convert("00:10"), convert("00:00")
#     curr_pos = pos
#     if op_start <= curr_pos <= op_end:
#         print("start position in opening")
#         curr_pos = op_end
    
#     for command in commands:
#         curr_pos = commands_dic[command](curr_pos)
#         if curr_pos < ten:
#             print("less than 10 from the start")
#             curr_pos = start
#         elif op_start <= curr_pos <= op_end:
#             print("opening")
#             curr_pos = op_end
#         elif video_len - timedelta(seconds=10) < curr_pos:
#             print("less than 10 rem")
#             curr_pos = video_len

#     return curr_pos.strftime('%M:%S')

from datetime import timedelta

def solution(video_len, pos, op_start, op_end, commands):
    
    def to_timedelta(time_str):
        minutes, seconds = map(int, time_str.split(":"))
        return timedelta(minutes=minutes, seconds=seconds)

    def to_mmss(td):
        total_seconds = int(td.total_seconds())
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02}:{seconds:02}"

    # Convert all time strings to timedelta
    video_len = to_timedelta(video_len)
    curr_pos = to_timedelta(pos)
    op_start = to_timedelta(op_start)
    op_end = to_timedelta(op_end)

    # Handle opening skip at the initial position
    if op_start <= curr_pos <= op_end:
        curr_pos = op_end

    for command in commands:
        if command == "prev":
            curr_pos -= timedelta(seconds=10)
            if curr_pos < timedelta(seconds=0):
                curr_pos = timedelta(seconds=0)
        elif command == "next":
            curr_pos += timedelta(seconds=10)
            if curr_pos > video_len:
                curr_pos = video_len

        # Skip opening if landed inside it
        if op_start <= curr_pos <= op_end:
            curr_pos = op_end

    return to_mmss(curr_pos)
