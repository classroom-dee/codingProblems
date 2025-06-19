def solution(mats, park):
    mats.sort(reverse=True)
    width = len(park[0])
    height = len(park)
    
    def isAvail(start_x, start_y, mat_size) -> bool:
        candid_xlim, candid_ylim = start_x + mat_size, start_y + mat_size
        for y in range(start_y, candid_ylim):
            for x in range(start_x, candid_xlim):
                if x >= width or y >= height:
                    return False
                if park[y][x] != "-1":
                    return False
        return True

    for mat in mats:
        # get the x, y limit for the mat
        xlim = (width // mat) * mat # x lim, 1 based
        ylim = (height // mat) * mat # y lim, 1 based
        for y in range(ylim):
            for x in range(xlim):
                if isAvail(x, y, mat):
                    return mat
    return -1