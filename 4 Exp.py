 # 4.Read a multi-digit number(as chars) from the console. Develop a program to print the frequency of each digit with a suitable message.

digits = input("enter numbers: ")
freq={}

for digit in digits:
    if digit.isdigit():
        if digit in freq:
            freq[digit] += 1
        else:
            freq[digit] = 1

    for digit in sorted(freq):
    print(f"Digit {digit} occurs {freq[digit]} time(s)")
