# q1.1

# i=0
# for i in range(3):
#     print("vishesh kumar bansal")




# q2.1
# a=int(input("first no"))
# b=int(input("second no"))
# c=int(input("third no"))
# print("sum of no ",a+b+c)





# q2.2
# a=input("first st")
# b=input("second st")
# c=input("third st")
# print("concatination  ",a+b+c ,end=" ")



# q3.1
# for i in range(1,11):
#     print("7 X ",i, " = ",7*i )

# for i in range(1,11):
#     print("9 X ",i, " = ",9*i )





# q3.2
# n=int(input("enter the no to get table"))
# for i in range(1,11):
#     print(n," X ",i, " = ",n*i )


# q3.3
# n=int(input("enter the no to get sum"))
# sum=0
# for i in range(1,n+1):

#     sum=sum+i
# print(sum)






# q4.1
# a=int(input("first no"))
# b=int(input("second no"))
# c=int(input("third no"))
# print(f"max of {a},{b},{c} is",max(a,b,c))





# q4.2
# n=int(input("enter the no to get sum"))
# sum=0
# for i in range(1,n+1):
#     if i%7==0 and i%9==0 :
#         sum=sum+i
# print(sum)




# q4.3

n = int(input("Enter a number: "))


prime_sum = 0


for num in range(2, n + 1):

    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    
    if is_prime:
        prime_sum += num


print(f"The sum of prime numbers up to {n} is: {prime_sum}")
