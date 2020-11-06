# Your code here
with open("robin.txt") as f:
    words = f.read()
    words = words.replace("\n", " ")

bad_ch = [
        "+", "-", "&&", "||", "!", "(", ")", "{", "}", "[", "]", "^",
        "~", "*", "?", ":","\"","\\", ";",",", ".", "=", "/", "|","&" ] 
for i in bad_ch:
    words = words.replace(i, '')

split_words = words.split(" ")

cache ={}
def histo(words):
   

    for word in split_words:
        if word.lower() not in cache:
            cache[word.lower()]= "#"
        else:
            cache[word.lower()]+='#'
    by_key = sorted(cache.items(),reverse=False, key=lambda pair: pair[0])
    by_values= sorted(cache.items(),reverse=True, key=lambda pair: pair[1])

    print(by_values)
    # print(by_key)
   
histo(split_words)