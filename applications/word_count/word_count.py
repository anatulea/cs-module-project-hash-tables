def word_count(s):
    # Your code here
    table = {}
    bad_ch = [
            "+", "-", "&&", "||", "!", "(", ")", "{", "}", "[", "]", "^",
            "~", "*", "?", ":","\"","\\", ";",",", ".", "=", "/", "|","&" ] 
    for i in bad_ch:
        s = s.replace(i, '')

    for word in s.split():
        if word.lower() not in table:
            table[word.lower()] = 1
        else:
            table[word.lower()] += 1
    return table

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))