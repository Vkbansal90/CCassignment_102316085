

L = [10, 20, 30, 40, 50, 60, 70, 80]


L.extend([200, 300])



L.remove(10)
L.remove(30)

L_ascending = sorted(L)

L_descending = sorted(L, reverse=True)

print("List after additions:", L)
print("List in ascending order:", L_ascending)
print("List in descending order:", L_descending)


#2



scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
highest_score = max(scores)
highest_index = scores.index(highest_score)

lowest_score = min(scores)
lowest_count = scores.count(lowest_score)

reversed_list = list(scores[::-1])

score_to_check = 76  
if score_to_check in scores:
    first_occurrence = scores.index(score_to_check)
    print(f"The score {score_to_check} is present at index {first_occurrence}.")
else:
    print(f"The score {score_to_check} is not present.")


print("Highest score:", highest_score, "at index:", highest_index)
print("Lowest score:", lowest_score, "occurs", lowest_count, "times.")
print("Reversed tuple as list:", reversed_list)

#3
import random


random_numbers = [random.randint(100, 900) for _ in range(100)]


odd_numbers = [num for num in random_numbers if num % 2 != 0]


even_numbers = [num for num in random_numbers if num % 2 == 0]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [num for num in random_numbers if is_prime(num)]


print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
print("Prime numbers:", prime_numbers)

#4

A = {34, 56, 78, 90}
B = {78, 45, 90, 23}


unique_scores = A | B


common_scores = A & B


exclusive_scores = A ^ B


is_subset = A <= B
is_superset = B >= A


score_to_remove = int(input("Enter a score to remove from A: "))
if score_to_remove in A:
    A.remove(score_to_remove)
    print(f"Score {score_to_remove} removed from A.")
else:
    print(f"Score {score_to_remove} is not present in A.")


print("Unique scores (Union):", unique_scores)
print("Common scores (Intersection):", common_scores)
print("Exclusive scores (Symmetric Difference):", exclusive_scores)
print("Is A a subset of B?", is_subset)
print("Is B a superset of A?", is_superset)
print("Set A after removal:", A)

#5

locations = {"city": "New York", "state": "New York", "country": "USA"}

if "city" in locations:
    locations["location"] = locations.pop("city")

print("Updated dictionary:", locations)

