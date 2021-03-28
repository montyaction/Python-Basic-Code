# dictionary comprehension with if else
# d = {1: 'odd' , 2:'even}

odd_even = {i :('Even'if i%2 ==0 else "Odd")for i in range(1,11)}
# print(odd_even)
for k,v in odd_even.items():
    print(f"{k} : {v}")