t = int(input())
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    
    left = 0
    right = n - 1
    alice_total = 0
    bob_total = 0
    prev_eaten = 0
    moves = 0
    is_alice_turn = True
    
    while left <= right:
        current_eaten = 0
        moves += 1
        
        if is_alice_turn:
            while left <= right and current_eaten <= prev_eaten:
                current_eaten += candies[left]
                left += 1
            alice_total += current_eaten
        else:
            while left <= right and current_eaten <= prev_eaten:
                current_eaten += candies[right]
                right -= 1
            bob_total += current_eaten
            
        prev_eaten = current_eaten
        is_alice_turn = not is_alice_turn
        
    print(moves, alice_total, bob_total)