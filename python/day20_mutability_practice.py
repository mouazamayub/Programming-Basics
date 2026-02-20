print("===== Refrence Behavior =====")
a = [1, 2, 3]
b = a
b[0] = 99
print("a: ", a)
print("b: ", b)

print("\n=== Shallow Copy Behaviour ===")
c = [1,2,3]
d = c.copy()
d[0] = 100
print("c: ", c)
print("d: ", d)

print("\n=== Nested List Shallow Copy ===")
x = [[1,2], [3,4]]
y = x.copy()
y[0][0] = 500
print("x: ", x)
print("y: ", y)