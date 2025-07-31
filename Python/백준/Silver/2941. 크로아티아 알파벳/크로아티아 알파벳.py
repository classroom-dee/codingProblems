# init
croat_word = input()
priority = 'dz='
char_set = ('c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=')
croat_letters_cnt = 0
idx = 0

while idx < len(croat_word):
    # skip for the length of the pattern
    if croat_word[idx:idx+3] == priority:
        idx += 3
    elif croat_word[idx:idx+2] in char_set:
        idx += 2
    else:
        idx += 1

    # count as one proper letter
    croat_letters_cnt += 1

print(croat_letters_cnt)