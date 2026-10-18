sentence = input()

# Clean and normalized the sentence
cleaned = sentence.strip()
lowered = cleaned.lower()
normalized = lowered.replace(".","")

# Split the sentence and create the slug
slug = normalized.replace(" ", "-")
uppercase_sentence = normalized.upper()
words = normalized.split()
search_index = normalized.find('python')

# Display all processed values
print(f"Cleaned: {cleaned}")
print(f"Normalized: {normalized}")
print(f"Words: {words}")
print(f"Slug: {slug}")
print(f"Uppercase: {uppercase_sentence}")
print(f"Python Position: {search_index}")

