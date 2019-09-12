friend = ['a', 'b', 'c', 'd', 'e']

handshakes = []

for x in range(0, len(friend) - 1):
    for y in range(x + 1, len(friend)):
        handshakes.append((friend[x], friend[y]))

print(handshakes)
