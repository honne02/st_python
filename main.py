def draw_triangle(fill, base):
    l = [i for i in range(1,base//2+2,)]
    l.extend([i for i in range(base//2, 0, -1)])
    for elem in l:
        print(fill * elem)

draw_triangle(input(), int(input()))