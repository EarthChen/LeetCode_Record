# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。
# 模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）
# 在本题中，匹配是指字符串的所有字符匹配整个模式。
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:  # 若均为空，返回true
            return True
        if len(s) > 0 and len(pattern) == 0:  # 若模式串为空，而字符串不为空，返回False
            return False
        if len(pattern) > 1 and pattern[1] == '*':  # 若模式串的第二个字符为*
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):  # 若s不为0，且第一个字符匹配
                return self.match(s[1:], pattern) or self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:])
            # 有三种情况：**表示模式串的第一个字符个数为2即重复了；*表示模式串的第一个字符个数为0；*表示模式串的第一个字符个数为1
            else:  # s的长度为0时，看模式串后面是否还有未匹配的项
                return self.match(s, pattern[2:])
        if len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0]):  # 只匹配一个字符的情况
            return self.match(s[1:], pattern[1:])  # 继续匹配该字符之后的字符串
