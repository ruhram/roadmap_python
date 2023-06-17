def hash_function(key) :
    print(sum(ord(character) for character in str(key)))

hash_function('Hello')
hash_function('3.14')
hash_function(3.14)