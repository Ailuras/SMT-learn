a = [1,2,3]

n = len(a)
a.append(4)
if n := len(a) > 3: 
    print(f"List is too long ({n} elements, expected <= 10)")
print(n)
