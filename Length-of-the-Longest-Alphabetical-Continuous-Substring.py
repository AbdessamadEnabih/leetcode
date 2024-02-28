#Length of the Longest Alphabetical Continuous Substring
count = 1
res = 1
for a,b in zip(s, s[1:]):
    if ord(a)+1 == ord(b):
        count += 1
        res = max(res, count)
    else:
        count = 1
return res
