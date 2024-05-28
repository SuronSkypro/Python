def bank(sum_vk, srok_vk, percent):

    i=1
    


    while i <= int(srok_vk):
        sum_vk = sum_vk + (sum_vk / 100 * percent)
        i=i+1

    return sum_vk


print(bank(100,5,10))


