S = input()
zero_cnt = 0
one_cnt = 0

if S[0] == '0' :
    zero_cnt += 1
else :
    one_cnt += 1

for i in range(len(S)-1) :
    if S[i] != S[i+1] :
        if S[i+1] == '0' :
            zero_cnt += 1
        elif S[i+1] == '1' :
            one_cnt += 1

print(min(zero_cnt, one_cnt))
