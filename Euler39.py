
def number_of_solutions(p):
    solution = 0
    for a in range(1,p+1):
        for b in range(a,p+1-a):
            if a**2 + b**2 == (p-a-b)**2:solution+=1
    return solution

# solution_dict  = dict()
# for i in range(1000):
#     solution_dict.update({i:0})
solution_dict = {i:0 for i in range(1000)}
for i in range(1000):
    solution_dict[i]+= number_of_solutions(i)
print(max(solution_dict,key=solution_dict.get))