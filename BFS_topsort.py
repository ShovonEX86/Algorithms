# -*- coding: utf-8 -*-
"""task1B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EU876MJzxWHyaWhvgTc3BczPSJ3koOmr
"""

input = open('input1b.txt','r')
output = open('output1b.txt','w')

num_courses , lines = tuple(map(int,input.readline().split()))
g = {}

for i in range(1,num_courses+1):
    g[i] = []
for j in range(lines):
    a , b  = tuple(map(int,input.readline().split()))
    g[a].append(b)

visit = {i:False for i in g}
visit2 = {i:False for i in g}
def has_cycle(v, stack):
    visit2[v] = True
    stack.append(v)

    for u in g[v]:
        if not visit2[u]:
            if has_cycle(u,stack):
                return True
        elif u in stack:
            return True

    stack.pop()
    return False

def cycle(g):
    stack = []
    for v in g:
        if not visit2[v]:
            if has_cycle(v,stack):
                return True
    return False

def BFS_topsort(g,s):
    deg = [0]*(num_courses+1)
    for i in g:
        for j in g[i]:
            deg[j] += 1
    queue = []
    insert = []
    for i in range(1,num_courses):
        if deg[i] == 0:
            queue.append(i)
    while len(queue)>0:
        u = queue.pop(0)
        insert.append(u)
        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 0 :
                queue.append(v)
    return insert

if cycle(g):
    output.write(f"IMPOSSIBLE")
else:
    for i in g:
        if visit[i] == False:
            a=BFS_topsort(g,i)
    for i in a:
        output.write(f"{i} ")
input.close()
output.close()