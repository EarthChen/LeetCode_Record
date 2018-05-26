# LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,
# 2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,
# 想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,
# 嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,
# 他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
# 上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
# LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何。
# 为了方便起见,你可以认为大小王是0。


class Solution:
    def IsContinuous(self, numbers):
        # 如果列表为空
        if not numbers:
            return numbers
        # 将列表中大于0的元素生成新列表
        new_list = [i for i in numbers if i > 0]
        # 排序
        new_list.sort()
        # 如果新列表长度为1
        if len(new_list) == 1:
            return True
        n = 0
        # 遍历列表
        for j in range(len(new_list) - 1):
            # 如果后一个元素减去前一个元素大于0
            if (new_list[j + 1] - new_list[j]) > 0:
                # 将加入他们的差
                n += (new_list[j + 1] - new_list[j])
            else:
                return False
        if n <= 4:
            return True
        else:
            return False
