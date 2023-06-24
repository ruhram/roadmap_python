def hash_function(key):
    return sum( index * ord(character) for index, character in enumerate(repr(key), start=1))

def hash_function_new(key):
    return sum(
        index * ord(character) for index, character in enumerate(repr(key).rstrip("'"), start=1)
    )

print(hash_function("Tiny"))

print(hash_function("This has a somewhat medium length."))

print(hash_function('a'))
print(hash_function('b'))
print(hash_function('c'))
print('\n')
print(hash_function_new('a'))
print(hash_function_new('b'))
print(hash_function_new('c'))