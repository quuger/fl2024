import sys


layer = set()
new_layer = set()
ends = set()
graph = []


def update_layer(symbol):
    global layer, new_layer, graph
    for x in layer:
        new_layer.update(graph[x][symbol])
    layer, new_layer = new_layer, layer
    new_layer.clear()


def solve(word):
    global layer, ends, graph
    l = len(word)
    pos = 0
    while pos < l:
        update_layer(int(word[pos]))
        pos += 1
    return len(layer.intersection(ends)) != 0


def read_automat():
    global layer, ends, graph

    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        m = int(file.readline().strip())

        layer = set(map(int, file.readline().split()))
        ends = set(map(int, file.readline().split()))

        graph = [[[] for _ in range(m)] for _ in range(n)]

        for line in file:
            input_list = list(map(int, line.split()))
            if input_list:
                graph[input_list[0]][input_list[1]].append(input_list[2])


read_automat()

for line in sys.stdin:
    result = solve(line.strip())
    print(result)


