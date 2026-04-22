def algo(card_number):
    digits = [int(d) for d in str(card_number)]
    
    # Reverse the digits
    digits.reverse()
    
    total = 0

    for i in range(len(digits)):
        if i % 2 == 1: 
            digits[i] = digits[i] * 2
            
            if digits[i] > 9:
                digits[i] -= 9
        
        total += digits[i]

    if total % 10 == 0:
        return True
    else:
        return False

number = input("Enter card number: ")

if algo(number):
    print("Valid Number ")
else:
    print("Invalid Number ")
    
    #   Question no 2 
    
import string

def remove(text):
    punctuations = string.punctuation

    result = ""
    for char in text:
        if char not in punctuations:
            result += char
    
    return result

input_text = input("Enter a string: ")

clean_text = remove(input_text)

print("Original Text:", input_text)
print("Without Punctuations:", clean_text)



#     Question no 3 
def sort_sentence(sentence):
    
    words = sentence.split()
    
    words.sort()

    sorted_sentence = " ".join(words)
    
    return sorted_sentence

input_sentence = input("Enter a sentence: ")

result = sort_sentence(input_sentence)

print("Original Sentence:", input_sentence)
print("Sorted Sentence:", result)