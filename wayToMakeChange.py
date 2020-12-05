def numberOfWaysToMakeChange(n, denoms):

    ways = []
    for i in range(n + 1):
        ways.append(0)

    ways[0] = 1
    for i in range(len(denoms)):
        for amount in range(1, len(ways)):
            if amount >= denoms[i]:
                ways[amount] += ways[amount-denoms[i]]

    return ways[-1]
