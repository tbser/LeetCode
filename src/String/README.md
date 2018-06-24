字符串面试题的特点
### A、广泛性
1、字符串可以看做字符类型的数组，与数组排序、查找、调整有关 <br>
2、很多其他类型的面试题可以看做字符串类型的面试题 <br>
### B、需掌握的概念
1、回文 <br>
2、子串（连续）<br>
3、子序列（不连续）<br>
4、前缀树（Trie树）<br>
5、后缀树和后缀数组 <br>
6、匹配 <br>
7、字典序 <br>
### C、需掌握的操作


### 205 isomorphic-strings  字符串同构
eg: paper title    比较两个字符串的每个对应位置字符上一次出现的位置

定义两个字典preIndexOfS和preIndexOfT，以其中一个字符串的长度进行for循环range(len(s))，当做下标(0,len(s)-1)，遍历两个字符串当前位置的字母，
作为字典的Key（s[i] t[i]），对应value为该字母之前出现的位置（i+1）（defaultdict[int]: 默认为0）。<br>
如果两个字符串中的字符上次出现的位置一样，那么就属于同构。

### 242 valid-anagram  两个字符串包含的字符是否完全相同
eg: anagram nagaram    比较每个字符出现次数

定义一个字典count，遍历其中一个字符串：for c in s, 将每个字符作为key，对应value为该字符出现次数，每次+1；然后再遍历另一个字符串，将当前字符
作为key对应的value -1，如果value<0，说明字符串s中没有该字符，return False。

### 409 longest-palindrome  计算一组字符集合可以组成的回文字符串的最大长度
eg: "abccccdd"  ->  "dccaccd"  7   统计每个字符出现次数

定义一个字典count，统计每个字符出现次数，然后统计有多少个出现偶数次的字符。如果还有出现奇数次（1次）的字符，最后+1，没有则直接返回出现偶数次的字符的个数。

### 009 palindrome-number  判断一个整数是否是回文数
eg:  121 True  -121 False   转置，判断相等

对于一个整数x，x % 10得到x最右边的数字，然后x / 10得到x除去最右边数字剩下的部分。

### 647 palindromic-substrings  回文子字符串
eg: input:"aaa" output:6 （"a", "a", "a", "aa", "aa", "aaa"）

s = "aaa"  <br>'#'.join(s) -> "a#a#a"

### 696 count-binary-substrings  统计二进制字符串中连续 1 和连续 0 数量相同的子字符串个数
eg: input:"00110011" output:6 ("0011", "01", "1100", "10", "0011", "01")

preLen=0: 上一个数字的长度(如果当前为0, 前面1的长度)  curLen=1: 当前数字的长度  result=0: 符合条件子串个数<br>
只要上一个数字的长度 大于或者等于 当前数字的长度, 就算一个结果子串.

