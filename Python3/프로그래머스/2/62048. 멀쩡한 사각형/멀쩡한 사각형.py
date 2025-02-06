import math
def solution(w, h):
    joong_gan = w + h - math.gcd(w, h)
    jeonchae = w * h
    return jeonchae - joong_gan