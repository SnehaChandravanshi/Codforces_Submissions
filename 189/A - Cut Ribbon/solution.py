n, a, b, c = map(int, input().split())
 
max_pieces = [-1] * (n + 1)
max_pieces[0] = 0
 
for i in range(1, n + 1):
    for piece_length in (a, b, c):
        if i >= piece_length and max_pieces[i - piece_length] != -1:
            max_pieces[i] = max(max_pieces[i], max_pieces[i - piece_length] + 1)
 
print(max_pieces[n])