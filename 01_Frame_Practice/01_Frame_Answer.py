import numpy as np


def vec_length(v):
    return np.sqrt(sum([x * x for x in v]))


def dot_product(v1, v2):
    return sum([x * y for x, y in zip(v1, v2)])


def cross_product(v1, v2):
    result = [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0],
    ]
    return result


def frame_from_3_points(N, C_alpha, C):
    v1 = [x - y for x, y in zip(C, C_alpha)]
    v2 = [x - y for x, y in zip(N, C_alpha)]
    v1_length = vec_length(v1)
    e1 = [x / v1_length for x in v1]

    dot = dot_product(e1, v2)
    u2 = [x - y * dot for x, y in zip(v2, e1)]
    u2_length = vec_length(u2)
    e2 = [x / u2_length for x in u2]
    e3 = cross_product(e1, e2)

    R = np.array([e1, e2, e3]).T
    t = C_alpha
    return R, t


if __name__ == '__main__':
    N = [0, 0, 1]
    C_alpha = [3, 0, 4]
    C = [1, -1, 2]
    R, t = frame_from_3_points(N, C_alpha, C)
    print(R)
    print(t)
