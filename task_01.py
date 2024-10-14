import heapq

def min_cost_to_connect_cables(cables):
    #ініціалізація купи з кабелями
    heapq.heapify(cables)

    total_cost = 0

    #поки більше 1 кабеля в купі
    while len(cables) > 1:
        #витягуємо 2 найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        #обчислення витрат на з'єднання цих двох кабелів
        cost = first + second
        total_cost += cost

        #додавання нового кбаеля (сумму) назад в купу
        heapq.heappush(cables, cost)

    return total_cost

cables = [4, 3, 2, 6]
result = min_cost_to_connect_cables(cables)
print(f"Мінімальна вартість з'єднання: {result}")

