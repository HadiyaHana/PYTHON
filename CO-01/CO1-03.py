print("LIST COMPREHENSIONS")
integers = [-5, -4, 3, 2, 1]
positive = [i for i in integers if i > 0]
print(positive)

num = int(input("Enter your number: "))
print("The list of squares:")
n_list = [i**2 for i in range(1, num+1)]
print(n_list)

vowels = ["a", "e", "i", "o", "u"]
word = input("Enter the word: ")
word_list = list(word)
w_vowels = [char for char in word_list if char in vowels]
print(w_vowels)
