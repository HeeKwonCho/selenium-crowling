import sys

INF = int(1e9) # 10억으로 설정
n = int(input()) # 노드의 개수 및 간선의 개수를 입력받기
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화

for i in range(1, n+1): # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m): # 각 간선에 대한 정보를 입력, 그 값으로 만들기
    a, b, c = map(int, input().split()) # a에서 b로 가는 비용=c
    graph[a][b] = c

for k in range(1, n+1): # 점화식에 따라 플로이드 워셜 알고리즘 실행
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1): # 결과 출력
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("도달할 수 없음", end='') # 도달할 수 없는 경우, 도달할 수 없음이라고 출력
        else:
            print(graph[i][j], end='') # 도달할 수 있는 경우 거리를 출력
    print()