def Stock_Profit(arr):
    max_profit = 0
    buy_price = arr[0]

    for i in range(1,len(arr)):
        if arr[i] < buy_price:
            buy_price = arr[i]
        else:
            profit = arr[i] - buy_price
            max_profit = max(max_profit,profit)
    return max_profit
arr = list(map(int,input().split()))
print(Stock_Profit(arr))
