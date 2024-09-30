def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"Word count: {word_count}")

        num_count = num_of_times(file_contents)
        sorted_count = sorting(num_count)

        print("Number of times each letter appears:")
        for char, count in sorted_count:
             print (f"'{char}': {count}")
        

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def num_of_times(count):
    lower_text = count.lower()
    counting = {}
    for letter in lower_text:
            if letter.isalpha():
                if letter in counting:
                    counting[letter] += 1
                else:
                    counting[letter] = 1
    return counting

def sorting(counting):
     counting_tuples = list(counting.items())
     counting_tuples.sort()
     return counting_tuples
     
            

main()


