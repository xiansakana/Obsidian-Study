# Easy

## Array / String

### [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/) （删除有序数组中的重复项）

```
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
```

```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
```

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        while right < len(nums):
            if(nums[left] == nums[right]):
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
        return left+1
```

时间复杂度：O(n)，其中 n 是数组的长度。快指针和慢指针最多各移动 n 次。

空间复杂度：O(1)，只需要使用常数的额外空间。



### [27. Remove Element](https://leetcode.com/problems/merge-sorted-array/description/) （[移除元素](https://leetcode.cn/problems/remove-element/)）

```
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
```

```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
```

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0
        while(i < len(nums)):          
            if nums[right]!=val:
                nums[left]=nums[right]
                left+=1
            right+=1
        return left
```

时间复杂度：O(n)，其中 n 为序列的长度。我们只需要遍历该序列至多两次。

空间复杂度：O(1)。我们只需要常数的空间保存若干变量。



### [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/) （[合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/)）

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

```python
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = 0;
        int p2 = 0;
        int[] sorted = new int[m + n];
        int cur;
        while (p1 < m || p2 < n){
            if(p1 == m){
                cur = nums2[p2];
                p2++;
            }else if(p2 == n){
                cur = nums1[p1];
                p1++;
            }else if(nums1[p1] < nums2[p2]){
                cur = nums1[p1];
                p1++;
            }else{
                cur = nums2[p2];
                p2++;
            }
            sorted[p1 + p2 - 1] = cur;
        }
        for(int i = 0; i < m + n; i++){
            nums1[i] = sorted[i];
        }
    }
}
```

时间复杂度：O(m+n)。指针移动单调递增，最多移动 m+n 次。

空间复杂度：O(m+n)。需要建立长度为 m+n 的中间数组 sorted。



### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) （[买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)）

```
Input: prices = [7,1,5,3,6,4]
Output: 5
```

```
Input: prices = [7,6,4,3,1]
Output: 0
```

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        profit = 0
        for p in prices:
            if p < cost:
                cost = p
            if profit < p - cost:
                profit = p - cost
        return profit
```

时间复杂度：O(n)。

空间复杂度：O(1)。



### [169. Majority Element](https://leetcode.com/problems/majority-element/description/) （[多数元素](https://leetcode.cn/problems/majority-element/)）

```\
Input: nums = [3,2,3]
Output: 3
```

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Boyer–Moore majority vote algorithm**

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj = 0
        for i in range(len(nums)):
            if count == 0:
                maj = nums[i]
            if maj == nums[i]:
                count += 1
            else:
                count -= 1
        return maj
```

时间复杂度：O(n)，Boyer-Moore 算法只对数组进行了一次遍历。

空间复杂度：O(1)，Boyer-Moore 算法只需要常数级别的额外空间。



```java
class Solution {
      private static int countNums(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<Integer, Integer>();
        int highestFreqNum = '\0';
        int highestFreq = 0;

        for (int num : nums) {
            if (!counts.containsKey(num)) {
                counts.put(num, 1);
            } else {
                counts.put(num, counts.get(num) + 1);
            }
            if (counts.get(num) > highestFreq) {
                highestFreq = counts.get(num);
                highestFreqNum = num;
            }
        }
        return highestFreqNum;
    }

    public int majorityElement(int[] nums) {
        return countNums(nums);
    }
}
```

时间复杂度：O(n)。

空间复杂度：O(n)。



# Medium

## Array / String

### [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) （[跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/)）

Return *the minimum number of jumps to reach* `nums[n - 1]`.

```
Input: nums = [2,3,1,1,4]
Output: 2
```

```
Input: nums = [2,3,0,1,4]
Output: 2
```

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_p = end = 0
        count = 0
        for i in range(len(nums)-1):
            if max_p >= i and nums[i] + i >= max_p:
                max_p = nums[i] + i
            if i == end:
                end = max_p
                count += 1
        return count

```

时间复杂度：一重循环遍历的时间复杂度是 O(n)，所以总体时间复杂度为 O(n)。
空间复杂度：只用到了常数项的变量，所以总体空间复杂度为 O(1)。



### [55. Jump Game](https://leetcode.com/problems/jump-game/) （[跳跃游戏](https://leetcode.cn/problems/jump-game/)）

Return `true` *if you can reach the last index, or* `false` *otherwise*.

```
Input: nums = [2,3,1,1,4]
Output: true
```

```
Input: nums = [3,2,1,0,4]
Output: false
```

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max = 0
        for i in range(len(nums)):
            if max >= i and i + nums[i] >= max:
                max = i + nums[i]
        return max >= len(nums) - 1
```

时间复杂度 O(n)。

空间复杂度 O(1)。



### [80. Remove Duplicates from Sorted II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/) （[删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/)）

```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
```

```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3]
```

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 1, 2
        while right < len(nums):
            if(nums[left] == nums[right] and nums[left-1] == nums[left]):
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
        return left + 1
```

时间复杂度：O(n)，其中 nnn 是数组的长度。我们最多遍历该数组一次。

空间复杂度：O(1)，我们只需要常数的空间存储若干变量。



### [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) （[买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)）

```
Input: prices = [7,1,5,3,6,4]
Output: 7
```

```
Input: prices = [1,2,3,4,5]
Output: 4
```

```
Input: prices = [7,6,4,3,1]
Output: 0
```

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        profit = 0
        total = 0
        for p in prices:
            if p < cost:
                cost = p
            if profit < p - cost:
                profit = p - cost
                total += profit
                cost = p
                profit = 0    
        return total
```

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit
```



### [134. Gas Station](https://leetcode.com/problems/gas-station/)（[加油站](https://leetcode.cn/problems/gas-station/)）

```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```

```
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        while i < len(gas):
            tank = 0
            count = 0
            while count < len(gas):
                j = (i + count) % len(gas)
                tank += gas[j]
                tank -= cost[j] 
                if tank < 0:
                    break
                count += 1
            if count == len(gas):
                return i
            else:
                i = i + count + 1
        return -1       
```

- 时间复杂度：O(N)，其中 N 为数组的长度。我们对数组进行了单次遍历。
- 空间复杂度：O(1)。



### [189. Rotate Array](https://leetcode.com/problems/rotate-array/description/) （[轮转数组](https://leetcode.cn/problems/rotate-array/)）

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
```

时间复杂度：O(n)。

空间复杂度：O(n)。



| 操作                              | 结果          |
| :-------------------------------- | ------------- |
| 原始数组                          | 1 2 3 4 5 6 7 |
| 翻转所有元素                      | 7 6 5 4 3 2 1 |
| 翻转 [0, (k mod n) -1] 区间的元素 | 5 6 7 4 3 2 1 |
| 翻转 [k mod n, n - 1] 区间的元素  | 5 6 7 1 2 3 4 |



```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums: List[int], start: int, end: int) -> None:
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1

        k %= len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
```

时间复杂度：O(n)，其中 n 为数组的长度。每个元素被翻转两次，一共 n 个元素，因此总时间复杂度为 O(2n)=O(n)。

空间复杂度：O(1)。



```java
class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start += 1;
            end -= 1;
        }
    }
}
```

时间复杂度：O(n)，其中 n 为数组的长度。每个元素被翻转两次，一共 n 个元素，因此总时间复杂度为 O(2n)=O(n)。

空间复杂度：O(1)。



### [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) （[除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/)）

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

左右乘积列表

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [0] * len(nums)
        R = [0] * len(nums)
        result = [0] * len(nums)

        L[0] = 1
        for i in range(1, len(nums)):
            L[i] = nums[i-1] * L[i-1]

        R[len(nums)-1] = 1
        for i in reversed(range(len(nums)-1)):
            R[i] = nums[i+1] * R[i+1]
        
        for i in range(len(nums)):
            result[i] = L[i] * R[i]

        return result
```

时间复杂度：O(N)，其中 N 指的是数组 nums 的大小。预处理 L 和 R 数组以及最后的遍历计算都是 O(N) 的时间复杂度。
空间复杂度：O(N)，其中 N 指的是数组 nums 的大小。使用了 L 和 R 数组去构造答案，L 和 R 数组的长度为数组 nums 的大小。



空间复杂度 O(1)O(1)*O*(1) 的方法

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        result[0] = 1
        for i in range(1, len(nums)):
            result[i] = nums[i-1] * result[i-1]
        
        R = 1
        for i in reversed(range(len(nums))):
            result[i] *= R
            R *= nums[i]

        return result
```

时间复杂度：O(N)，其中 N 指的是数组 nums 的大小。分析与方法一相同。
空间复杂度：O(1)，输出数组不算进空间复杂度中，因此我们只需要常数的空间存放变量。



### [274. H-Index](https://leetcode.com/problems/h-index/) （[H 指数](https://leetcode.cn/problems/h-index/)）

```
Input: citations = [3,0,6,1,5]
Output: 3
```

```
Input: citations = [1,3,1]
Output: 1
```

排序

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        i = 0
        citations_sorted = sorted(citations, reverse=True)
        while i < len(citations_sorted):
            if h < citations_sorted[i]:
                h += 1
            i += 1
        return h
```

时间复杂度：O(nlog⁡n)，其中 n 为数组 citations 的长度。即为排序的时间复杂度。

空间复杂度：O(log⁡n)，其中 n 为数组 citations 的长度。即为排序的空间复杂度。



二分搜索

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right = 0,len(citations)
        while left<right:
            # +1 防止死循环
            mid = (left+right+1)>>1
            cnt = 0
            for v in citations:
                if v>=mid:
                    cnt+=1
            if cnt>=mid:
                # 要找的答案在 [mid,right] 区间内
                left=mid
            else:
                # 要找的答案在 [0,mid) 区间内
                right=mid-1
        return left
```

时间复杂度：O(nlogn)，其中 n 为数组 citations 的长度。需要进行 logn 次二分搜索，每次二分搜索需要遍历数组 citations 一次。
空间复杂度：O(1)，只需要常数个变量来进行二分搜索。



### [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) （[O(1) 时间插入、删除和获取随机元素](https://leetcode.cn/problems/insert-delete-getrandom-o1/)）

```
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]
```

```python
class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        # add the new element to the end of the array
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        # get the index of the num to be removed
        index = self.indices[val]
        # assign the index of the num to be removed to the last element of the hash table
        # so that the corresponding index in the hash table is synchronized with the array 
        self.indices[self.nums[-1]] = index
        # set the last element of the array to the position of the num to be removed
        self.nums[index] = self.nums[-1]
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```



# Hard

## Array / String

### [2. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)（[接雨水](https://leetcode.cn/problems/trapping-rain-water/)）

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

![img](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        water = left = leftMax = rightMax = 0
        right = len(height) - 1
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                water += leftMax - height[left]
                left += 1
            else:
                water += rightMax - height[right]
                right -= 1
        return water
```

时间复杂度：O(n)，其中 n 是数组 height 的长度。两个指针的移动总次数不超过 n。

空间复杂度：O(1)。只需要使用常数的额外空间。



### [135. Candy](https://leetcode.com/problems/candy/)（[分发糖果](https://leetcode.cn/problems/candy/)）

```
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
```

```
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
```

两次遍历

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        
        right = ret = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)
        
        return ret

```

时间复杂度：O(n)，其中 n 是孩子的数量。我们需要遍历两次数组以分别计算满足左规则或右规则的最少糖果数量。

空间复杂度：O(n)，其中 n 是孩子的数量。我们需要保存所有的左规则对应的糖果数量。



常数空间遍历

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        total = 1
        candy = 1
        countUp = 1
        countDown = 0
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i-1]:
                countDown = 0
                if ratings[i] == ratings[i-1]:
                    candy = 1
                else:
                    candy += 1
                total += candy
                countUp = candy
            else:
                countDown += 1
                if countDown == countUp:
                    countDown += 1
                total += countDown
                candy = 1
        return total
```

时间复杂度：O(n)，其中 n 是孩子的数量。我们需要遍历两次数组以分别计算满足左规则或右规则的最少糖果数量。

空间复杂度：O(1)。我们只需要常数的空间保存若干变量。
