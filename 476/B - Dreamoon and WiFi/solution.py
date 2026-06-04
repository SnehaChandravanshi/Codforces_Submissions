s1 = input().strip()
s2 = input().strip()
 
target_pos = s1.count('+') - s1.count('-')
current_pos = s2.count('+') - s2.count('-')
unknowns = s2.count('?')
 
def solve(index, pos):
    if index == unknowns:
        return 1 if pos == target_pos else 0
    
    # Try putting a '+' and a '-' in the current '?' spot
    return solve(index + 1, pos + 1) + solve(index + 1, pos - 1)
 
valid_combinations = solve(0, current_pos)
total_combinations = 1 << unknowns  # 2 to the power of unknowns
 
print(f"{valid_combinations / total_combinations:.12f}")