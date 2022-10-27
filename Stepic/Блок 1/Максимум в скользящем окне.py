m = int(input())
arr = list(map(int, input().split()))
n = int(input())


class myQueue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, append_element):
        maxima = append_element if not self.queue1 else max([append_element, self.queue1[-1][1]])
        self.queue1.append([append_element, maxima])

    def pop(self):
        if not self.queue2:
            while self.queue1:
                element = self.queue1.pop()[0]
                maxima = element if not self.queue2 else max([element, self.queue2[-1][1]])
                self.queue2.append([element, maxima])
        self.queue2.pop()

    def getMax(self):
        if not self.queue1 or not self.queue2:
            maxima = self.queue2[-1][1] if not self.queue1 else self.queue1[-1][1]
        else:
            maxima = max([self.queue1[-1][1], self.queue2[-1][1]])
        return maxima


my_que = myQueue()

for i in range(n - 1):
    my_que.push(arr[i])

for i in range(n - 1, len(arr)):
    my_que.push(arr[i])
    print(my_que.getMax())
    my_que.pop()