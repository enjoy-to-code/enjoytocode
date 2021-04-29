import wikipedia

# search for 'python' keys in wikipedia
python_defs = wikipedia.search("Python")
# check if key contains the word 'programming'
for key in python_defs:
    if key.find('programming'):
        # print article summary
        print(wikipedia.summary("Python (programming language)"))



