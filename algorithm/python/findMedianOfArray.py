import heapq

class MedianFinder:
    def __init__(self):
        # Initialize a min heap for the larger half of numbers
        self.minHeap = []
        # Initialize a max heap for the smaller half of numbers
        # We negate the numbers to simulate a max heap using Python's min heap
        self.maxHeap = []

    def addNum(self, num):
        # Add the new number to the appropriate heap
        # First, add to maxHeap (smaller half), we negate the num to use min heap as max heap
        heapq.heappush(self.maxHeap, -num)

        # Ensure every number in maxHeap is less than or equal to every number in minHeap
        # Move the largest number from maxHeap to minHeap
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        # Balance the heaps so that minHeap is not larger than maxHeap by more than one element
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self):
        # If the heaps are of equal size, the median is the average of the two middle numbers
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        # If they are not of equal size, the median is the middle number from the heap with more elements
        else:
            return -self.maxHeap[0]

# Example of using the MedianFinder
finder = MedianFinder()
nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

for num in nums:
    finder.addNum(num)
    print(f"Current median after adding {num}: {finder.findMedian()}")
