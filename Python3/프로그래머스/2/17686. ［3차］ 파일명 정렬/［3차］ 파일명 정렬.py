import re
def solution(files):
    return sorted(files, key=lambda x: sorter(x))

def sorter(file_name):
    pattern = r'^([^0-9]+)(\d+)(.*)$'
    match = re.match(pattern, file_name)
    # match cannot be None
    head = match.group(1).lower()
    number = match.group(2)
    tail = match.group(3)
    return (head, int(number))