# def get_line(x0, y0, x1, y1):
#     points = [(x0, y0)]
#     dx = x1 - x0
#     dy = y1 - y0
#     xk = x0
#     yk = y0
#     # parametro de decision inicial
#     Pk = 2 * dy - dx

#     while xk < x1:
#         xk += 1
#         if Pk < 0:
#             Pk = Pk + 2 * dy
#         else:
#             Pk = Pk + 2 * dy - 2 * dx
#             yk += 1
#         points.append((xk, yk))

#     return points


# if __name__ == "__main__":
#     x0 = 3
#     y0 = 2
#     x1 = 15
#     y1 = 11
#     points = get_line(x0, y0, x1, y1)
#     print(points)


def get_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    return points