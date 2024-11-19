# word relay prob with bad konglish 
def solution(n, words):
    i = 0
    j = 0
    turns = [0] * n
    counts = {w:0 for w in set(words)}
    prev = ''
    while True:
        if j == len(words): break
        word = words[j]
        turns[i] += 1 # taken a turn
        # print(f'{i+1}th person has taken his/her {turns[i]}th turn, used word {word}')
        if j != 0:
            if word[0] != prev[-1]:
                return [i+1, turns[i]]
        if counts[word] > 0:
            # print("Which has already been used! YOU ARE THE WEAKEST LINK!")
            return [i+1, turns[i]]
        else:
            counts[word] += 1
        i = (i + 1) % n
        j += 1
        prev = word
    return [0, 0]