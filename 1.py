sentence = input("Enter a sentence: ")
sentence_length = len(sentence)
print(sentence_length)

file_name = input("Enter a file name: ")
file_name = f"{file_name}.txt"

with open(file_name,"w") as f:
    f.write(sentence)
    f.close()

print(f"You have written {sentence_length} characters to {file_name}")