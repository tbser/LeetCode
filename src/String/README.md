## 字符串面试题的特点
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
1、与数组有关的操作：增删改查 <br>
2、字符的替换 <br>
3、字符串的旋转 <br>

## 字符串题目的常见类型
### A、规则判断
1、判断字符串是否符合整数规则 <br>
2、判断字符串是否符合浮点数规则 <br>
3、判断字符串是否符合回文字符串规则 <br>
 。。。等等许多规则 <br>
### B、数字运算 
 int和long类型表达整数范围有限，所以经常用字符串实现大整数 <br>
 与大整数相关的加减乘除操作，需要模拟笔算的过程 <br>
### C、与数组操作有关的类型 
1、数组有关的调整、排序等操作需要掌握 <br>
2、快速排序的划分过程需要掌握和改写 <br>
### D、字符计数 
1、哈希表 <br>
2、固定长度的数组 <br>
3、滑动窗口问题、寻找无重复字符子串问题、计算变位词问题 <br>
### E、动态规划类型 
1、最长公共子串 <br>
2、最长公共子序列 <br>
3、最长回文子串 <br>
4、最长回文子序列 <br>
。。。等 <br>
### F、搜索类型 
1、宽度优先搜索 <br>
2、深度优先搜索 <br>
### G、高级算法与数据结构解决的问题
1、Manacher算法解决最长回文子串问题 <br>
2、KMP算法解决字符串匹配问题 <br>
3、前缀树结构（Trie树）<br>
4、后缀树和后缀数组 <br>
5、通常面试中很少出现 <br>

# LeetCode题
## 字符交换 —— 活用局部逆序函数 组合的过程
### 151 reverse-words-in-a-string  字符逆序
eg: "the sky is  blue ", return "blue is sky the".  List的reverse方法
```
t = s.split()  # 将字符串转换成包含一个个word的列表 ['the','sky','is','blue'] 
t.reverse()  # 返回已经逆序的列表t  ['blue', 'is', 'sky', 'the'] 
' '.join(t) # 返回以空格连接的字符串
```
**more**:
```
fpath = "/data/deep/learning/1.jpg" 
fpath.split('/')    # ['', 'data', 'deep', 'learning', '1.jpg'] 
file_path, file_name = os.path.split(fpath)   # '/data/deep/learning/', '1.jpg'
```
### 186 reverse-words-in-a-string-II  字符逆序 要求space:O(1)
eg: s = "the sky is blue"<br>
先把每个字符都逆转: "eulb si yks eht", <br>
然后把每个单词逆转: "blue is sky the"。<br>
写一个reverse函数，依次分别从字符串的开头和结尾遍历，交换字符位置 <br>

将字符串按每个字符划分: <br>
```
string = list(s)   # ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
```
### 557 reverse-words-in-a-string-III 将每个单词逆序，保持该单词在句子中的位置不变
eg: s = "Let's take LeetCode contest"   Output: "s'teL ekat edoCteeL tsetnoc"

与reverse-words-in-a-string-II比较：直接把每个单词逆转<br>
```
word = 'huang'
reversed_word = word[::-1]  # 'gnauh'

reversed_words = [word[::-1] for word in s.split(' ')]
reversed = ' '.join(reversed_words)
```
### 字符串移位
给定一个字符串str，和一个整数i。i代表str中的位置，将str[0...i]移动右侧，str[i+1...N-1]移到左侧。 <br>
eg: str="ABCDE", i=2  output: "DEABC". 要求时间复杂度为O(N), 额外空间复杂度为O(1)。<br>
```
1、将str[0...i]部分的字符逆序   ABCDE -> CBADE
2、将str[i+1...N-1]部分的字符逆序  CBADE -> CBAED
3、将str整体的字符逆序  CBAED -> DEABC
```

## 排序
### 拼接最小字典序
给定一个字符串类型的数组strs，请找到一种拼接顺序，使得将所有字符串拼接起来组成的大字符串是所有可能性中字典顺序最小的，并返回这个大字符串。<br>
eg：strs=["abc", "de"]。可以拼成"abcde"，也可以拼成"deabc"，但前者字典顺序更小，所以返回"abcde"。<br>
strs=["b", "ba"]。 output="bab" <br>  
最优解的时间复杂度：O(N\*logN),其实质是一种排序的实现。<br>  
```
如果str1+str2 < str2+str1，则str1放在前面，否则str2放在前面。
```

## 字符比较
### 205 isomorphic-strings  字符串同构
eg: paper title    比较两个字符串的每个对应位置字符上一次出现的位置

定义两个字典preIndexOfS和preIndexOfT，以其中一个字符串的长度进行for循环range(len(s))，当做下标(0,len(s)-1)，遍历两个字符串当前位置的字母，
作为字典的Key（s[i] t[i]），对应value为该字母之前出现的位置（i+1）（defaultdict[int]: 默认为0）。<br>
如果两个字符串中的字符上次出现的位置一样，那么就属于同构。

### 242 valid-anagram  两个字符串包含的字符是否完全相同
eg: anagram nagaram    比较每个字符出现次数

定义一个字典count，遍历其中一个字符串：for c in s, 将每个字符作为key，对应value为该字符出现次数，每次+1；然后再遍历另一个字符串，将当前字符
作为key对应的value -1，如果value<0，说明字符串s中没有该字符，return False。

## 回文规则
### 409 longest-palindrome  计算一组字符集合可以组成的回文字符串的最大长度
eg: "abccccdd"  ->  "dccaccd"  7   统计每个字符出现次数

定义一个字典count，统计每个字符出现次数，然后统计有多少个出现偶数次的字符。如果还有出现奇数次（1次）的字符，最后+1，没有则直接返回出现偶数次的字符的个数。

### 009 palindrome-number  判断一个整数是否是回文数
eg:  121 True  -121 False   转置，判断相等

对于一个整数x，x % 10得到x最右边的数字，然后x / 10得到x除去最右边数字剩下的部分。

### 647 palindromic-substrings  回文子字符串
eg: input:"aaa" output:6 （"a", "a", "a", "aa", "aa", "aaa"）
```
s = "aaa" 
'#'.join(s) -> "a#a#a"
```

## 字符子串
### 696 count-binary-substrings  统计二进制字符串中连续 1 和连续 0 数量相同的子字符串个数
eg: input:"00110011" output:6 ("0011", "01", "1100", "10", "0011", "01")

preLen=0: 上一个数字的长度(如果当前为0, 前面1的长度)  curLen=1: 当前数字的长度  result=0: 符合条件子串个数<br>
只要上一个数字的长度 大于或者等于 当前数字的长度, 就算一个结果子串.

