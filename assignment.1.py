# q1.1

i=0
for i in range(3):
    print("vishesh kumar bansal")




# q2.1
a=int(input("first no"))
b=int(input("second no"))
c=int(input("third no"))
print("sum of no ",a+b+c)





# q2.2
a=input("first st")
b=input("second st")
c=input("third st")
print("concatination  ",a+b+c ,end=" ")



# q4.1
for i in range(1,11):
    print("7 X ",i, " = ",7*i )

for i in range(1,11):
    print("9 X ",i, " = ",9*i )





# q4.2
n=int(input("enter the no to get table"))
for i in range(1,11):
    print(n," X ",i, " = ",n*i )


# q4.3
n=int(input("enter the no to get sum"))
sum=0
for i in range(1,n+1):

    sum=sum+i
print(sum)






# q5.1
a=int(input("first no"))
b=int(input("second no"))
c=int(input("third no"))
print(f"max of {a},{b},{c} is",max(a,b,c))





# q5.2
n=int(input("enter the no to get sum"))
sum=0
for i in range(1,n+1):
    if i%7==0 and i%9==0 :
        sum=sum+i
print(sum)




# q5.3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
p = int(input("Enter a number:"))
prime_sum=0
for i in range(1,p+1):
    if(is_prime(i)):
        prime_sum+=i
print("the sum of prime numbers upto n is:", prime_sum)



# q6.1
def add_odd(n):
    l = [i for i in range(1,n+1) if i%2!=0]
    return sum(l)
q=int(input("enter a number:"))
print("Sum of odd numbers upto n:", add_odd(q))

#q 6.2
def add_prime(n):
    l = [i for i in range(1,n+1) if is_prime(i)]
    return sum(l)
r=int(input("enter a number:"))
print("Sum of prime numbers upto n:", add_prime(r))


