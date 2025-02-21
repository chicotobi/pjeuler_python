import time
from functools import cache

mod = 10**9+7

@cache
def mult_mat(m1, m2):
    # Computes the product of two matrices modulo mod.                          
    N = len(m1)
    res = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][k] += m1[i][j]*m2[j][k]
    for i in range(N):
        for j in range(N):
            res[i][j] %= mod
    return res

@cache
def mat_power(mat, exponent):
    # Computes mat up to the power exponent modulo mod.                         
    start = time.time()
    N = len(mat)
    res = [[0]*N for i in range(N)]
    for i in range(N):
        res[i][i] = 1
    power = mat
    while exponent > 0:
        if exponent & 1:
            res = mult_mat(power, res)
        exponent //= 2
        print("exponent = "+str(exponent)+" time = "+str(time.time()-start))
        power = mult_mat(power, power)
    return res

@cache
def mult(mat, vec):
    # Performs matrix multiplication multiplying the matrix by the vector.      
    N = len(mat)
    assert len(mat[0]) == N
    assert len(vec) == N
    res = [0]*N
    for i in range(N):
        for j in range(N):
                res[i] += mat[i][j]*vec[j]
    return res

letters = {'A', 'E', 'F', 'R'}

# A map of the keywords to unique indices.                                      
keywords = {'FREE':8, 'FARE':4, 'AREA':2, 'REEF':1}

# A map from each of the prefixes (of length 3 or less) of the keywords to      
# unique indices.                                                               
terms = list(set([word[:i] for i in range(1,4) for word in keywords]))
terms = {terms[i]:i for i in range(len(terms))}
terms[''] = len(terms)

l = len(terms)
N = 16*l

# Compute the transition matrix.                                                
transition = [[0]*N for i in range(N)]
for term in terms:
    # Loop over the possible combinations of keywords that might have already   
    # been completed.                                                           
    for completed in range(16):
        state = completed*l+terms[term]
        for letter in letters:
            new_term = term+letter
            if new_term in keywords:
                if keywords[new_term] & completed:
                    # A keyword has been repeated.  So we can forget about this
                    # string.                                                   
                    pass
                else:
                    new_completed = completed+keywords[new_term]
                    new_term = new_term[1:]
                    while new_term not in terms:
                        new_term = new_term[1:]
                    transition[terms[new_term]+new_completed*l][state] += 1
            else:
                while new_term not in terms:
                    assert new_term != ""
                    new_term = new_term[1:]
                transition[terms[new_term]+completed*l][state] += 1

def f(q, mod):
    initial_state = [0]*N
    initial_state[11] = 1
    state = mult(mat_power(transition, q), initial_state)
    return sum([state[i] for i in range(15*l, 16*l)]) % mod

print(f(10**18, 10**9+7))