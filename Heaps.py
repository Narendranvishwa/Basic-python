heap = []

def insert(job, priority):
    heap.append((priority, job))
    i = len(heap) - 1

    while i > 0:
        parent = (i - 1) // 2

        if heap[i][0] > heap[parent][0]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break


def delete_max():
    if len(heap) == 0:
        print("Heap is empty")
        return

    max_job = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    i = 0
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(heap) and heap[left][0] > heap[largest][0]:
            largest = left

        if right < len(heap) and heap[right][0] > heap[largest][0]:
            largest = right

        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            i = largest
        else:
            break

    print("Deleted Job:", max_job[1])


def peek():
    if heap:
        print("Highest Priority Job:", heap[0][1])
    else:
        print("Heap is empty")


def display():
    print("Jobs in Heap Order:")
    for priority, job in heap:
        print(job, "-", priority)



insert("Job1", 17)
insert("Job2", 15)
insert("Job3", 10)
insert("Job4", 6)
insert("Job5", 10)
insert("Job6", 7)

display()
peek()
delete_max()
display()
