# Count Pairs Whose Sum is Less than Target

# Runtime: 39 ms
# Memory Usage: 16.5 MB

def numberOfEmployeesWhoMetTarget(hours, target: int):
    hours.sort()
    c = 0
    for i in hours:
        if i >= target:
            c+=1
            
    return c 





hours = [5,1,4,2,2]
target = 6

print(numberOfEmployeesWhoMetTarget(hours, target))







