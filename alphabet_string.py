def solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_length = len(alphabet)
    repetitions = N // alphabet_length
    remainder = N % alphabet_length
    
    result = alphabet * repetitions
    
    result += alphabet[:remainder]
    
    return result

print(solution(3))   
print(solution(5))  
print(solution(30))
