#### 205 isomorphic-strings  字符串同构
eg: paper title   
定义两个字典preIndexOfS和preIndexOfT，以其中一个字符串的长度进行for循环range(len(s))，当做下标(0,len(s)-1)，遍历两个字符串当前位置的字母，
作为字典的Key（s[i] t[i]），对应value为该字母之前出现的位置（i+1）（defaultdict[int]: 默认为0）。
如果两个字符串中的字符上次出现的位置一样，那么就属于同构。

#### 242 valid-anagram  两个字符串包含的字符是否完全相
eg: anagram nagaram 
定义一个字典count，遍历其中一个字符串：for c in s, 将每个字符作为key，对应value为该字符出现次数，每次+1；然后再遍历另一个字符串，将当前字符
作为key对应的value -1，如果value<0，说明字符串s中没有该字符，return False。

