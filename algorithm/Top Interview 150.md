---
title: Top Interview 150
tags:
  - Leetcode
  - 算法
cover: https://cdn.jsdelivr.net/npm/xiansakana-blog-img/202403050327460.jpg
categories: 算法
abbrlink: b6d1a2e5
date: 2024-03-05 03:41:00
---

# Easy

## [1. Two Sum](https://leetcode.com/problems/two-sum/)（[两数之和](https://leetcode.cn/problems/two-sum/)）

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in hashtable:
                return [i, hashtable[target - nums[i]]]
            hashtable[nums[i]] = i
```

时间复杂度：O(N)，其中 N 是数组中的元素数量。对于每一个元素 i，我们可以 O(1) 地寻找 target - i。

空间复杂度：O(N)，其中 N 是数组中的元素数量。主要为哈希表的开销。

## [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)（[整数转罗马数字](https://leetcode.cn/problems/integer-to-roman/)）

```
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
```

```
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        Int2Roman = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        Roman = ''
        for value, symbol in Int2Roman:
            while num >= value:
                num -= value
                Roman += symbol
            if num == 0:
                break
        return Roman
```

时间复杂度：O(1)。由于 value Symbols 长度是固定的，且字符中的每个字符的出现次数均不会超过 3，因此循环次数有一个确定的上限。对于本题给出的数据范围，循环次数不会超过 15 次。

空间复杂度：O(1)。

## [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)（[罗马数字转整数](https://leetcode.cn/problems/roman-to-integer/)）

```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        Roman2Int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Int = 0
        n = len(s)
        for i in range(n - 1):
            if Roman2Int[s[i]] < Roman2Int[s[i + 1]]:
                Int -= Roman2Int[s[i]]
            else:
                Int += Roman2Int[s[i]]
        return Int + Roman2Int[s[-1]]
```

时间复杂度：O(N)。遍历了一遍数组。

空间复杂度：O(1)。使用了 `Int`。

## [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)（[最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/)）

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

```python
class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        length = len(word)
        ans = ''
        for i in range(length):
            char = word[i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return ans
            ans += char
        return ans
```

时间复杂度：O(mn)，其中 m 是字符串数组中的字符串的平均长度，n 是字符串的数量。最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。

空间复杂度：O(1)。使用的额外空间复杂度为常数。

## [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/) （[删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)）

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

## [27. Remove Element](https://leetcode.com/problems/merge-sorted-array/description/) （[移除元素](https://leetcode.cn/problems/remove-element/)）

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

## [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)（[找出字符串中第一个匹配项的下标](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/)）

```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

**暴力解**

```python
for i in range(0,len(haystack)-len(needle)+1):
	if haystack[i:i+len(needle)] == needle:
		return i
return -1
```

时间复杂度：O(n×m)，其中 n 是字符串 haystack 的长度，m 是字符串 needle 的长度。最坏情况下我们需要将字符串 needle 与字符串 haystack 的所有长度为 m 的子串均匹配一次。

空间复杂度：O(1)。我们只需要常数的空间保存若干变量。

## [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)（[最后一个单词的长度](https://leetcode.cn/problems/length-of-last-word/)）

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in s[::-1]:
            if i !=' ':
                length +=1
            elif i ==' ' and length != 0:
                break
        return length
```

时间复杂度：O(n)，其中  n  是字符串的长度。最多需要反向遍历字符串一次。

空间复杂度：O(1)。

## [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/) （[合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/)）

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

## [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) （[买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)）

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

## [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)（[验证回文串](https://leetcode.cn/problems/valid-palindrome/)）

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**筛选和判断**

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # s_lower = ''.join([char.lower() for char in s if char.isalnum()])
        return s_lower == s_lower[::-1]
```

时间复杂度：O(∣s∣)，其中 ∣s∣ 是字符串 sss 的长度。

空间复杂度：O(∣s∣)。由于我们需要将所有的字母和数字字符存放在另一个字符串中，在最坏情况下，新的字符串 s_lower 与原字符串 s 完全相同，因此需要使用 O(∣s∣) 的空间。

**双指针**

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
```

时间复杂度：O(∣s∣)，其中 ∣s∣ 是字符串 s 的长度。

空间复杂度：O(1)。

## [169. Majority Element](https://leetcode.com/problems/majority-element/description/) （[多数元素](https://leetcode.cn/problems/majority-element/)）

```
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

## [202. Happy Number](https://leetcode.com/problems/happy-number/)（[快乐数](https://leetcode.cn/problems/happy-number/)）

```
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

```
Input: n = 2
Output: false
```

**Hashset**

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(num):
            sum = 0
            while num:
                sum += (num % 10) ** 2
                num = num // 10
            return sum
        mid = set()
        while True:
            n = getNext(n)
            if n == 1:
                return True
            if n in mid:
                return False
            else:
                mid.add(n)
```

对于 3 位数的数字，它不可能大于 243。这意味着它要么被困在 243 以下的循环内，要么跌到 1。4 位或 4 位以上的数字在每一步都会丢失一位，直到降到 3 位为止。

时间复杂度：O(243⋅3+log⁡n+log⁡log⁡n+log⁡log⁡log⁡n)... = O(log⁡n)。
- 查找给定数字的下一个值的成本为 O(log⁡n)，因为我们正在处理数字中的每位数字，而数字中的位数由 log⁡n 给定。
- 要计算出总的时间复杂度，我们需要仔细考虑循环中有多少个数字，它们有多大。
- 我们在上面确定，一旦一个数字低于 243，它就不可能回到 243 以上。因此，我们就可以用 243 以下最长循环的长度来代替 243，不过，因为常数无论如何都无关紧要，所以我们不会担心它。
- 对于高于 2433 的 n，我们需要考虑循环中每个数高于 243 的成本。通过数学运算，我们可以证明在最坏的情况下，这些成本将是 O(log⁡n)+O(log⁡log⁡n)+O(log⁡log⁡log⁡n)...。幸运的是，O(log⁡n) 是占主导地位的部分，而其他部分相比之下都很小（总的来说，它们的总和小于log⁡n），所以我们可以忽略它们。

空间复杂度：O(log⁡n)。与时间复杂度密切相关的是衡量我们放入哈希集合中的数字以及它们有多大的指标。对于足够大的 n，大部分空间将由 n 本身占用。我们可以很容易地优化到 O(243⋅3)=O(1)，方法是只保存集合中小于 243 的数字，因为对于较高的数字，无论如何都不可能返回到它们。

**双指针**

```python
def isHappy(self, n: int) -> bool:  
    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner == 1
```

时间复杂度：O(log⁡n)。该分析建立在对前一种方法的分析的基础上，但是这次我们需要跟踪两个指针而不是一个指针来分析，以及在它们相遇前需要绕着这个循环走多少次。
- 如果没有循环，那么快跑者将先到达 1，慢跑者将到达链表中的一半。我们知道最坏的情况下，成本是 O(2⋅log⁡n)=O(log⁡n)=O(logn)。
- 一旦两个指针都在循环中，在每个循环中，快跑者将离慢跑者更近一步。一旦快跑者落后慢跑者一步，他们就会在下一步相遇。假设循环中有 k 个数字。如果他们的起点是相隔 k−1 的位置（这是他们可以开始的最远的距离），那么快跑者需要 k−1 步才能到达慢跑者，这对于我们的目的来说也是不变的。因此，主操作仍然在计算起始 n 的下一个值，即 O(log⁡n)。

空间复杂度：O(1)，对于这种方法，我们不需要哈希集来检测循环。指针需要常数的额外空间。

## [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)（[同构字符串](https://leetcode.cn/problems/isomorphic-strings/)）

```
Input: s = "egg", t = "add"
Output: true
```

```
Input: s = "foo", t = "bar"
Output: false
```

```
Input: s = "paper", t = "title"
Output: true
```

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
```

时间复杂度：O(n)，其中 n 为字符串的长度。我们只需同时遍历一遍字符串 s 和 t 即可。

空间复杂度：O(∣Σ∣)，其中 Σ 是字符串的字符集。哈希表存储字符的空间取决于字符串的字符集大小，最坏情况下每个字符均不相同，需要 O(∣Σ∣) 的空间。

## [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)（[有效的字母异位词](https://leetcode.cn/problems/valid-anagram/)）

```
Input: s = "anagram", t = "nagaram"
Output: true
```

```
Input: s = "rat", t = "car"
Output: false
```

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

时间复杂度：O(n)，其中 n 为 s 的长度。

空间复杂度：O(S)，其中 S 为字符集大小，此处 S=26。

## [290. Word Pattern](https://leetcode.com/problems/word-pattern/)（[单词规律](https://leetcode.cn/problems/word-pattern/)）

```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```

```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        return len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s)))
```

时间复杂度：O(n+m)，其中 n 为 pattern 的长度，m 为 str 的长度。插入和查询哈希表的均摊时间复杂度均为 O(n+m)。每一个字符至多只被遍历一次。

空间复杂度：O(n+m)，其中 n 为 pattern 的长度，m 为 str 的长度。最坏情况下，我们需要存储 pattern 中的每一个字符和 str 中的每一个字符串。


## [383. Ransom Note](https://leetcode.com/problems/ransom-note/)（[赎金信](https://leetcode.cn/problems/ransom-note/)）

```
Input: ransomNote = "a", magazine = "b"
Output: false
```

```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

**暴力解**

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,'',1)
            else:
                return False
        return True
```

时间复杂度：O(mn)，其中 m 是字符串 ransomNote 的长度，n 是字符串 magazine 的长度。

空间复杂度：O(∣S∣)，S 是字符集，这道题中 S 为全部小写英语字母，因此 ∣S∣=26。

**Hash Table**

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)
```

时间复杂度：O(m+n)，其中 m 是字符串 ransomNote 的长度，n 是字符串 magazine 的长度，我们只需要遍历两个字符一次即可。

空间复杂度：O(∣S∣)，S 是字符集，这道题中 S 为全部小写英语字母，因此 ∣S∣=26。

## [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)（[判断子序列](https://leetcode.cn/problems/is-subsequence/)）

```
Input: s = "abc", t = "ahbgdc"
Output: true
```

```
Input: s = "axc", t = "ahbgdc"
Output: false
```

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        if len(s) == 0:
            return True
        while p2 < len(t):      
            if s[p1] == t[p2]:
                if p1 == len(s) - 1:
                    return True
                p1 += 1
            p2 += 1
        return False
```

时间复杂度：O(n+m)，其中 n 为 s 的长度，m 为 t 的长度。每次无论是匹配成功还是失败，都有至少一个指针发生右移，两指针能够位移的总距离为 n+m。

空间复杂度：O(1)。


# Medium

## [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)（[无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)）

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**双指针滑动窗口**

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        right = -1
        max_len = 0
        for left in range(len(s)):
            if left != 0:
                hashset.remove(s[left - 1])
            while right < len(s) - 1 and s[right + 1] not in hashset:
                hashset.add(s[right + 1])
                right += 1
            max_len = max(max_len, right - left + 1)
        return max_len
```

时间复杂度：O(N)，其中 N 是字符串的长度。左指针和右指针分别会遍历整个字符串一次。

空间复杂度：O(∣Σ∣)，其中 Σ 表示字符集（即字符串中可以出现的字符），∣Σ∣ 表示字符集的大小。在本题中没有明确说明字符集，因此可以默认为所有 ASCII 码在 \[0,128) 内的字符，即 ∣Σ∣=128|。我们需要用到哈希集合来存储出现过的字符，而字符最多有 ∣Σ∣ 个，因此空间复杂度为 O(∣Σ∣)。

## [6. Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/)（[Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/)）

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

```
Input: s = "A", numRows = 1
Output: "A"
```

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [""] * numRows
        mod = numRows * 2 - 2
        for i in range(len(s)):
            j = min(i % mod, mod - i % mod)
            res[j] += s[i]
        return "".join(res)
```

时间复杂度：O(n)。

空间复杂度：O(n)。

## [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) （[盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)）

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

```
Input: height = [1,1]
Output: 1
```

**双指针**

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        water = 0
        while left < right:
            water = max(water, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water
```

时间复杂度：O(N)，双指针总计最多遍历整个数组一次。

空间复杂度：O(1)，只需要额外的常数级别的空间。

## [15. 3Sum](https://leetcode.com/problems/3sum/)（[三数之和](https://leetcode.cn/problems/3sum/)）

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

**双指针

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                else:
                    arr.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return arr
```

时间复杂度：O(N<sup>2</sup>)，其中 N 是数组 nums 的长度。

空间复杂度：O(log⁡N)。我们忽略存储答案的空间，额外的排序的空间复杂度为 O(log⁡N)。然而我们修改了输入的数组 nums，在实际情况下不一定允许，因此也可以看成使用了一个额外的数组存储了 nums的副本并进行排序，空间复杂度为 O(N)。

## [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)（[有效的数独](https://leetcode.cn/problems/valid-sudoku/)）

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    box_index = (i // 3) * 3 + j // 3  
                    if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)
        return True
```

时间复杂度：O(1)。数独共有 81 个单元格，只需要对每个单元格遍历一次即可。

空间复杂度：O(1)。由于数独的大小固定，因此哈希表的空间也是固定的。

## [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) （[跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/)）

Return _the minimum number of jumps to reach_ `nums[n - 1]`.

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

## [48. Rotate Image](https://leetcode.com/problems/rotate-image/)（[旋转图像](https://leetcode.cn/problems/rotate-image/)）

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```


![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```
![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

**原地旋转**

- 当 n 为偶数时

![](https://assets.leetcode-cn.com/solution-static/48/1.png)

- 当 n 为奇数时

![](https://assets.leetcode-cn.com/solution-static/48/2.png)

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = matrix[n -j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
```


时间复杂度：O(N<sup>2</sup>)，其中 N 是 matrix 的边长。我们需要枚举的子矩阵大小为 O((n/2)×((n+1)/2))=O(N<sup>2</sup>)。

空间复杂度：O(1)。为原地旋转。

**用翻转代替旋转**

$$  
\left[  
\begin{matrix}  
5 & 1 & 9 & 11\\  
2 & 4 & 8 & 10\\  
13 & 3 & 6 & 7\\
15 & 14 & 12 & 16\\
\end{matrix}  
\right] 
\stackrel{水平反转}{\Longrightarrow}
\left[  
\begin{matrix}  
15 & 14 & 12 & 16\\
13 & 3 & 6 & 7\\
2 & 4 & 8 & 10\\  
5 & 1 & 9 & 11\\  
\end{matrix}  
\right]
\stackrel{主对角线翻转}{\Longrightarrow}
\left[  
\begin{matrix}  
15 & 13 & 2 & 5\\
14 & 3 & 4 & 1\\
12 & 6 & 8 & 9\\  
16 & 7 & 10 & 11\\  
\end{matrix}  
\right]
$$


```python
class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
		n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

时间复杂度：O(N<sup>2</sup>)，其中 N 是 matrix 的边长。对于每一次翻转操作，我们都需要枚举矩阵中一半的元素。

空间复杂度：O(1)。为原地翻转得到的原地旋转。

## [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)（[字母异位词分组](https://leetcode.cn/problems/group-anagrams/)）

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

```
Input: strs = [""]
Output: [[""]]
```

```
Input: strs = ["a"]
Output: [["a"]]
```

**排序**

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            if ''.join(sorted(s))  not in res:
                res[''.join(sorted(s))] = [s]
            else:
                res[''.join(sorted(s))].append(s)
        return list(res.values())
```

时间复杂度：O(nklog⁡k)，其中 n 是 strs 中的字符串的数量，k 是 strs 中的字符串的的最大长度。需要遍历 n 个字符串，对于每个字符串，需要 O(klog⁡k) 的时间进行排序以及 O(1) 的时间更新哈希表，因此总时间复杂度是 O(nklog⁡k)。

空间复杂度：O(nk)，其中 n 是 strs 中的字符串的数量，k 是 strs 中的字符串的的最大长度。需要用哈希表存储全部字符串。

**计数**

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            mp[tuple(counts)].append(st)
        return list(mp.values())
```

时间复杂度：O(n(k+∣Σ∣))，其中 n 是 strs 中的字符串的数量，k 是 strs 中的字符串的的最大长度，Σ 是字符集，在本题中字符集为所有小写字母，∣Σ∣=26。需要遍历 n 个字符串，对于每个字符串，需要 O(k) 的时间计算每个字母出现的次数，O(∣Σ∣)) 的时间生成哈希表的键，以及 O(1) 的时间更新哈希表，因此总时间复杂度是 O(n(k+∣Σ∣))。

空间复杂度：O(n(k+∣Σ∣))，其中 n 是 strs 中的字符串的数量，k 是 strs 中的字符串的最大长度，Σ 是字符集，在本题中字符集为所有小写字母，∣Σ∣=26。需要用哈希表存储全部字符串，而记录每个字符串中每个字母出现次数的数组需要的空间为 O(∣Σ∣)，在渐进意义下小于 O(n(k+∣Σ∣))，可以忽略不计。

## [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)（[螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)）

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```
![]()
![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

**模拟**

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            # 削头（第一层）
            res += matrix.pop(0)
            # 将剩下的逆时针转九十度，等待下次被削
            # The unpacking operator `*` is used here to unpack the rows of the matrix as separate arguments to the `zip` function.
            matrix = list(zip(*matrix))[::-1]
        return res
```

时间复杂度：O(mn)，其中 m 和 n 分别是输入矩阵的行数和列数。矩阵中的每个元素都要被访问一次。

空间复杂度：O(mn)。需要创建一个大小为 m×nm 的矩阵 visited 记录每个位置是否被访问过。

**按层模拟**

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        left, right , top, bottom = 0, cols - 1, 0, rows - 1
        while left <= right >= 0 and top <= bottom:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right - 1, left, -1):
                    res.append(matrix[bottom][col])
                for row in range(bottom, top, -1):
                    res.append(matrix[row][left])
            left, right , top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res
```

![](https://assets.leetcode-cn.com/solution-static/54/54_fig1.png)

时间复杂度：O(mn)，其中 m 和 n 分别是输入矩阵的行数和列数。矩阵中的每个元素都要被访问一次。

空间复杂度：O(1)。除了输出数组以外，空间复杂度是常数。

## [55. Jump Game](https://leetcode.com/problems/jump-game/) （[跳跃游戏](https://leetcode.cn/problems/jump-game/)）

Return `true` _if you can reach the last index, or_ `false` _otherwise_.

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

## [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)（[矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes/)）

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

**使用标记数组**

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row0 = set()
        col0 = set()
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row0.add(row)
                    col0.add(col)
        for row in row0:
            for col in range(cols):
                matrix[row][col] = 0
        for col in col0:
            for row in range(rows):
                matrix[row][col] = 0
```

时间复杂度：O(mn)，其中 m 是矩阵的行数，n 是矩阵的列数。我们至多只需要遍历该矩阵两次。

空间复杂度：O(m+n)，其中 m 是矩阵的行数，n 是矩阵的列数。我们需要分别记录每一行或每一列是否有零出现。


**使用两个标记变量**

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0
        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0
```

时间复杂度：O(mn)，其中 m 是矩阵的行数，n 是矩阵的列数。我们至多只需要遍历该矩阵两次。

空间复杂度：O(1)。我们只需要常数空间存储若干变量。

## [80. Remove Duplicates from Sorted II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/) （[删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/)）

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

## [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) （[买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)）

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

## [134. Gas Station](https://leetcode.com/problems/gas-station/)（[加油站](https://leetcode.cn/problems/gas-station/)）

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

## [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)（[反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/)）

```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

```
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

**使用语言特性**

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split()
        result.reverse()
        result = " ".join(result)
        return result
```

时间复杂度：O(n)，其中  n  为输入字符串的长度。

空间复杂度：O(n)，用来存储字符串分割之后的结果。

**双指针遍历**

```java
class Solution {
    public String reverseWords(String s) {
        s = ' ' + s;
        int n = s.length();
        StringBuilder ans = new StringBuilder();
        for (int left = n - 1, right = n; left >= 0; left--) {
            char ch = s.charAt(left);
            if (ch == ' ') {
                if (left + 1 < right) {
                    ans.append(s, left + 1, right).append(' ');
                }
                right = left;
            }
        }
        return ans.substring(0, ans.length() - 1);
    }
}
```

时间复杂度：O(n)，其中  n  为输入字符串的长度。

空间复杂度：O(1)。

## [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)（[两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)）

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

**双指针**

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]
```

时间复杂度：O(n)，其中 n 是数组的长度。两个指针移动的总次数最多为 n 次。

空间复杂度：O(1)。


## [189. Rotate Array](https://leetcode.com/problems/rotate-array/description/) （[轮转数组](https://leetcode.cn/problems/rotate-array/)）

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


## [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)（[长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/)）

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

**双指针滑动窗口**

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = len(nums) + 1
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1
        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len
```

时间复杂度：O(n)，其中 n 是数组的长度。指针 left 和 right 最多各移动 n 次。

空间复杂度：O(1)。


## [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) （[除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/)）

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

空间复杂度 O(1)O(1)_O_(1) 的方法

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

## [274. H-Index](https://leetcode.com/problems/h-index/) （[H 指数](https://leetcode.cn/problems/h-index/)）

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

## [289. Game of Life](https://leetcode.com/problems/game-of-life/)（[生命游戏](https://leetcode.cn/problems/game-of-life/)）

1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

![](https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg)

```
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

![](https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg)

```
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
```

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
  
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2
                if board[row][col] == 1 and (live_neighbors > 3 or live_neighbors < 2):
                    board[row][col] = -1

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
```

时间复杂度：O(mn)，其中 m，n 分别为 board 的行数和列数。

空间复杂度：O(1)，除原数组外只需要常数的空间存放若干变量。

## [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) （[O(1) 时间插入、删除和获取随机元素](https://leetcode.cn/problems/insert-delete-getrandom-o1/)）

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

## [2. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)（[接雨水](https://leetcode.cn/problems/trapping-rain-water/)）

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

## [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)（[串联所有单词的子串](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/)）

```
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.
```

```
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 in s that is equal to the concatenation of any permutation of words.
We return an empty array.
```

```
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
```

**滑动窗口+哈希表**

```python
class Solution:
    def findSubstring(self, s: str, words):
        if not words or not s:
            return []

        word_length = len(words[0])
        words_total_length = len(words) * word_length
        word_count = len(words)
        word_map = {}
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1

        result = []

        for i in range(word_length):
            left = i
            right = i
            current_map = {}
            count = 0
            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length
                if word in word_map:
                    current_map[word] = current_map.get(word, 0) + 1
                    count += 1
                    while current_map[word] > word_map[word]:
                        left_word = s[left:left + word_length]
                        current_map[left_word] -= 1
                        count -= 1
                        left += word_length
                    if count == word_count:
                        result.append(left)
                else:
                    current_map.clear()
                    count = 0
                    left = right
        return result
```

时间复杂度：O(ls×n)，其中 ls 是输入 s 的长度，n 是 words 中每个单词的长度。需要做 n 次滑动窗口，每次需要遍历一次 s。

空间复杂度：O(m×n)，其中 m 是 words 的单词数，n 是 words 中每个单词的长度。每次滑动窗口时，需要用一个哈希表保存单词频次。


## [68. Text Justification](https://leetcode.com/problems/text-justification/)（[文本左右对齐](https://leetcode.cn/problems/text-justification/)）

```
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

```
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
```

```python
# blank 返回长度为 n 的由空格组成的字符串
def blank(n: int) -> str:
    return ' ' * n

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        right, n = 0, len(words)
        while True:
            left = right  # 当前行的第一个单词在 words 的位置
            sumLen = 0  # 统计这一行单词长度之和
            # 循环确定当前行可以放多少单词，注意单词之间应至少有一个空格
            while right < n and sumLen + len(words[right]) + right - left <= maxWidth:
                sumLen += len(words[right])
                right += 1

            # 当前行是最后一行：单词左对齐，且单词之间应只有一个空格，在行末填充剩余空格
            if right == n:
                s = " ".join(words[left:])
                ans.append(s + blank(maxWidth - len(s)))
                break

            numWords = right - left
            numSpaces = maxWidth - sumLen

            # 当前行只有一个单词：该单词左对齐，在行末填充空格
            if numWords == 1:
                ans.append(words[left] + blank(numSpaces))
                continue

            # 当前行不只一个单词
            avgSpaces = numSpaces // (numWords - 1)
            extraSpaces = numSpaces % (numWords - 1)
            s1 = blank(avgSpaces + 1).join(words[left:left + extraSpaces + 1])  # 拼接额外加一个空格的单词
            s2 = blank(avgSpaces).join(words[left + extraSpaces + 1:right])  # 拼接其余单词
            ans.append(s1 + blank(avgSpaces) + s2)

        return ans
```

时间复杂度：O(m)，其中 m 是数组 words 中所有字符串的长度之和。

空间复杂度：O(m)。


## [135. Candy](https://leetcode.com/problems/candy/)（[分发糖果](https://leetcode.cn/problems/candy/)）

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
