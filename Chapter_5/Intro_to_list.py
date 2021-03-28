numbers = [1,2,3,4,5,6,]
print(numbers[1])
print(numbers[0:3])
print(numbers[1:4])
print(numbers[0:-3])
print(numbers[::-1])

words = ["word1","word2","word3","word4"]
print(words[:2])

mixed = [1,2,3,4,"five","six",2.3,None]
print(mixed[-1])

mixed[6:] = ['three','four']
print(mixed)