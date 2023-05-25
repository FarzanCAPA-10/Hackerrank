def runnerup(nums):
    winner = float('-inf')
    runner = float('-inf')

    for num in nums:
        if num > winner:
            runner = winner
            winner = num

        elif num < winner and num > runner:
            runner = num
    return runner    

score = [2,3,5,4,7]
ans = runnerup(score)
print(ans)