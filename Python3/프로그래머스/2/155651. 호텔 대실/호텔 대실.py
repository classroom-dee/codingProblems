def solution(book_time):
    book_time = sorted(map(to_time, book_time), key=lambda x: x[0])
    # print(f'init: {book_time}')
    roomz = []
    for b in book_time:
        # print(f'booking {b}')
        occupied = False
        for i in range(len(roomz)):
            if roomz[i] <= b[0]:
                # print(f'room {i} available. assigning {b} to this')
                roomz[i] = b[1]
                occupied = True
                break
        if not occupied:
            # print(f'Cant allocate. need new room')
            roomz.append(b[1])
    return len(roomz)
def to_time(l):
    h1, m1 = l[0].split(":")
    h2, m2 = l[1].split(":")
    return [int(h1) * 60 + int(m1), int(h2) * 60 + int(m2) + 10]