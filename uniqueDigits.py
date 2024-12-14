def hasUniqueDigits(num):
    numStr = str(num)
    seen = set()

    for digit in numStr:
        if digit in seen:
            return False
        seen.add(digit)

    return True

def countUniqueDigits(arr):
    result  = []

    for pair in arr:
        low, high = pair

        count = 0
        for num in range(low, high + 1):
            if hasUniqueDigits(num) == True:
                count += 1
        result.append(count)

    print(result)

arr = [[1, 5], [94, 187], [94742, 1927429]]
countUniqueDigits(arr)