text = input("Enter the text: ").lower()
print(text)


if ("make a lot of money" in text or
    "buy now" in text or
    "subscribe this" in text or
    "click this" in text):
    print("🚫 It's a spam")

else:
    print(" ✅ NOT a spam")