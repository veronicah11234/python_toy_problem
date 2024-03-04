def check_alive(health):
    if health <= 0:
        return False    
    else:
        return True

player_health = 5
result = check_alive(player_health)
print(result) 

result = check_alive(0)
result1 = check_alive(3)

print(result)
print(result1)  

