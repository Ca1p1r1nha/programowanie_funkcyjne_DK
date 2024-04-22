def concat_string(*args):
    zdanie = ''
    for y in args:
        zdanie = zdanie + " " + y
    return zdanie

print(concat_string('ala', 'ma', 'kota', 'i', 'psa'))