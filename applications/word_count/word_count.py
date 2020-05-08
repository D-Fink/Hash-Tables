def word_count(s, cache=None):
    # Implement me.
    cache = {}

    arr = s.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ').split(' ')

    for i in arr:
        i.replace('\t', '')

    ignore_char = map(lambda i : i.strip('":;,.-+=/\\|[]{}()*^&').lower(), arr)
    for i in ignore_char:
        if i == "":
            continue
        if i not in cache:
            cache[i] = 1
        else:
            cache[i] += 1

    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))