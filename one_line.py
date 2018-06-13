"""
script only one line could be awesome

updating continuously

author: will

"""

# filter prime numbers between 2 and 100
print([i for i in range(2, 100) if all(i % j for j in range(2, int(i ** 0.5) + 1))])

# print code itself
_='_=%r;print(_%%_)';print(_%_)

# print love
print('\n'.join([''.join([('Love'[(x - y) % 4] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-40, 40)]) for y in range(15, -15, -1)]))

