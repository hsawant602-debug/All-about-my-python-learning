import keyword

# Get the list of all Python keywords
keywords_list = keyword.kwlist

print("Python Reserved Keywords are:\n")
for kw in keywords_list:
    print(kw)

# Print total count of keywords
print("\nTotal number of keywords:", len(keywords_list))
