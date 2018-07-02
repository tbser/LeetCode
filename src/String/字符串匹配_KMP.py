# 从字符串s中查找是否有p子串


def kmp_match(s, p):
    lens = len(s)
    lenp = len(p)
    table = partial_match(p)
    cur = 0
    while cur <= lens - lenp:
        for i in range(lenp):
            if s[cur + i] != p[i]:
                # 移动位数 = 已匹配的字符数(i) - 对应的部分匹配值(最后一个匹配值 i-1)
                cur += max(1, i - table[i - 1])
                break
        else:
            return True
    return False


def partial_match(p):
    res = [0]  # 第一个字母 前缀后缀都为空集,共有元素长度为0
    prefix = set()
    postfix = set()

    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i+1] for j in range(1, i+1)}

        res.append(len((prefix & postfix or {''}).pop()))

    return res