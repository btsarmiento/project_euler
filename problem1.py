#defining the multiples of 3 and 5 that is below 100
multiples = [x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]
#getting the sum of these multiples
total = sum(multiples)
print(total)