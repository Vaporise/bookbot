def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"Word count: {word_count}")
        num_count = num_of_times(file_contents)
        print("Number of times each letter appears:")
        for char, count in num_count.items():
             print (f"'{char}': {count}")

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def num_of_times(count):
    lower_text = count.lower()
    counting = {}
    for letter in lower_text:
        if letter in counting:
                counting[letter] += 1
        else:
                counting[letter] = 1
    return counting

            

main()


