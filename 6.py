paths = (
    [(3, 'GLSL'), (2, 1994), (1, 'JSON5')],
    [(3, 'GLSL'), (2, 1994), (1, 'OZ')],
    [(3, 'GLSL'), (2, 1994), (1, 'FORTH')],
    [(3, 'GLSL'), (2, 1965)],
    [(3, 'GLSL'), (2, 1984), (1, 'JSON5'), (4, 'NIT')],
    [(3, 'GLSL'), (2, 1984), (1, 'JSON5'), (4, 'JULIA')],
    [(3, 'GLSL'), (2, 1984), (1, 'OZ')],
    [(3, 'GLSL'), (2, 1984), (1, 'FORTH')],
    [(3, 'LOGOS'), (0, 'DART')],
    [(3, 'LOGOS'), (0, 'SELF')]
)


def main(x):
    for i, path in enumerate(paths):
        for item in path:
            if item[1] != x[item[0]]:
                break
        else:
            return i
