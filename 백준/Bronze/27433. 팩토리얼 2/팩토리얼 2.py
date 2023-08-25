N = int(input())
my_dict = {}
my_dict[0] = 1
my_dict[1] = 1
def fact(n):
    if n == 1 or n == 0:
        return 1
    if n not in my_dict:
        my_dict[n] = n * fact(n-1)
    return my_dict[n]
fact(N)
print(my_dict[N])