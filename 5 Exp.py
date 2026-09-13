""" 5. Develop a program to print 10 most frequently appearing words in a text file. [Hint: Use a dictionary with 
distinct words and their frequency of occurrences. Sort the dictionary in the reverse order of frequency and 
display the dictionary slice of the first 10 items . """

freq={} 
files=input("Enter file name(text.txt):")
with open(files,"r") as file:
    for line in file:
        words = line.lower().split()
        for word in words:            
            if word in freq:
                    freq[word] += 1 
            else:
                    freq[word] = 1

stored_value=sorted(freq.items(),key = lambda item:item[1],reverse=True)
stored_value=stored_value[:10]

print("The 10 most repeated words are:")
print(f"{'word':<15}  frequency ")
print("-"*24)

for word,num in stored_value:
    print(f"{word:<15}{num}")
  