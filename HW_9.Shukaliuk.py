
print("TASK 1_____________________________________________________________________________________\n")

"""Функція жадібного алгоритму find_coins_greedy. 
функція повинна приймати суму, яку потрібно видати покупцеві, 
і повертати словник із кількістю монет кожного номіналу, 
що використовуються для формування цієї суми. """

coins = [50, 25, 10, 5, 2, 1]
final_sum = 113

def find_coins_greedy(user_list, needed_result):
    sorted_list = sorted(user_list, reverse=True)
    needed_result_sum = needed_result
    change_dic = {}
    
    while needed_result_sum > 0:
        for coin in sorted_list:
            if coin <= needed_result_sum:
                needed_result_sum = needed_result_sum - coin
                if coin in change_dic:
                    change_dic[coin]= change_dic[coin]+ 1
                else:
                    change_dic[coin] = 1
                break
    return change_dic, needed_result_sum

print(find_coins_greedy(coins,final_sum))

print("\nTASK 1 recursion __________________________________________________________________________\n")


coins = [50, 25, 10, 5, 2, 1]
final_sum = 114

def find_coins_greedy_rec(user_list, needed_result, change_dic):
    if change_dic is None:
        change_dic = {}
    sorted_list = sorted(user_list, reverse=True)
    
    for coin in sorted_list:
        if needed_result == coin:
            if coin in change_dic:
                change_dic[coin]= change_dic[coin]+ 1
            else:
                change_dic[coin] = 1
            return change_dic
        elif needed_result > coin:
            if coin in change_dic:
                change_dic[coin]= change_dic[coin]+ 1
            else:
                change_dic[coin] = 1
            return(find_coins_greedy_rec(user_list, needed_result-coin, change_dic))
    return change_dic   

print(find_coins_greedy_rec(coins,final_sum, None))         
    
print("\nTASK 2_____________________________________________________________________________________\n")
"""Функція динамічного програмування find_min_coins.
повинна приймати суму для видачі решти, 
використовувати метод динамічного програмування,
знайти мінімальну кількість монет, необхідних для формування цієї суми. 
повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим способом """

def find_min_coins(coins_list, needed_sum):
    min_coins = [float('inf')] * (needed_sum + 1)
    min_coins[0] = 0

    last_used_coin = [None] * (needed_sum + 1)
        
    for current_sum in range(1, needed_sum + 1):
        for coin in coins_list:
            if coin <= current_sum:
                if min_coins[current_sum - coin] + 1 < min_coins[current_sum]:
                    min_coins[current_sum] = min_coins[current_sum - coin] + 1
                    last_used_coin[current_sum] = coin

    result = {}
    current_sum = needed_sum

    while current_sum > 0:
        coin = last_used_coin[current_sum]
        if coin is None:
            return {}

        if coin in result:
            result[coin]= result[coin]+ 1
        else:
            result[coin] = 1

        current_sum =  current_sum - coin
    return result

print(find_min_coins(coins, final_sum))