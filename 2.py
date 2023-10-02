import heapq

def total_processing_time(m, n, processing_times):
    # 将作业按处理时间从小到大排序
    job_queue = [(t, i) for i, t in enumerate(processing_times)]
    job_queue.sort()

    # 初始化处理器队列、等待队列和总耗时
    processor_queue = []
    waiting_queue = job_queue[m:]
    total_time = 0

    while processor_queue or waiting_queue:
        while processor_queue and len(processor_queue) < m:
            # 将处理时间最短的作业加入处理器队列
            _, job_idx = job_queue.pop(0)
            processor_queue.append((processing_times[job_idx], job_idx))

        min_processing_time, min_job_idx = heapq.heappop(processor_queue)
        total_time += min_processing_time

        # 更新处理器队列中作业的剩余处理时间
        for i in range(len(processor_queue)):
            processor_queue[i] = (processor_queue[i][0] - min_processing_time, processor_queue[i][1])

        # 将等待队列中处理时间最短的作业加入处理器队列
        if waiting_queue:
            _, job_idx = heapq.heappop(waiting_queue)
            processor_queue.append((processing_times[job_idx], job_idx))

    return total_time

# # 示例用法
# m = 3
# n = 6
# processing_times = [5, 2, 7, 3, 6, 4]
# total_time = total_processing_time(m, n, processing_times)
# print(f"系统处理完所有作业的总耗时为: {total_time}")



import sys

def dijkstra(graph, start, end):
    # 获取地点的总数
    num_vertices = len(graph)
    
    # 创建一个列表，用于存储从起点到每个地点的最短路径长度
    shortest_distances = [sys.maxsize] * num_vertices
    shortest_distances[start] = 0
    
    # 创建一个列表，用于存储每个地点的前一个地点，以构建最短路径
    predecessors = [-1] * num_vertices
    
    # 创建一个集合，用于跟踪已经找到最短路径的地点
    unvisited = set(range(num_vertices))
    
    while unvisited:
        # 选择未访问的地点中距离最短的地点
        current_vertex = min(unvisited, key=lambda vertex: shortest_distances[vertex])
        
        # 从未访问的地点中移除当前地点
        unvisited.remove(current_vertex)
        
        # 遍历与当前地点相邻的地点
        for neighbor in range(num_vertices):
            if graph[current_vertex][neighbor] > 0:  # 如果有连接
                potential = shortest_distances[current_vertex] + graph[current_vertex][neighbor]
                if potential < shortest_distances[neighbor]:
                    # 更新最短路径和前一个地点
                    shortest_distances[neighbor] = potential
                    predecessors[neighbor] = current_vertex
    
    # 构建最短路径
    path = []
    current_vertex = end
    while current_vertex != -1:
        path.insert(0, current_vertex)
        current_vertex = predecessors[current_vertex]
    
    return path, shortest_distances[end]

# 示例用法
# 请将邻接矩阵graph和地点索引映射关系设置为实际数据
graph = [
    [0, 10, 15, 0, 0, 0],
    [10, 0, 0, 20, 0, 0],
    [15, 0, 0, 5, 25, 0],
    [0, 20, 5, 0, 0, 30],
    [0, 0, 25, 0, 0, 10],
    [0, 0, 0, 30, 10, 0]
]

start_location = 0  # A地点
end_location = 3    # D地点

path, shortest_time = dijkstra(graph, start_location, end_location)
print(f"从地点 {chr(ord('A')+start_location)} 到地点 {chr(ord('A')+end_location)} 的最短路径是: {' -> '.join([chr(ord('A')+i) for i in path])}")
print(f"预计最短耗时为: {shortest_time} 分钟")
