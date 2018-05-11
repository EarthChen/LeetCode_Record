# 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志
# 写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，
# 有一天他向Fish借来翻看，但却读不懂它的意思。
# 例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
# 正确的句子应该是“I am a student.”


class Solution:
    def ReverseSentence(self, s):
        # 使用空格进行字符串切割转换为列表
        l = s.split(' ')
        # 使用空格将字符串倒序拼成一个新的字符串
        return ' '.join(l[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.ReverseSentence(' '))
