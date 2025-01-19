import re
import random

# 歌词列表
lyrics = [
    "预备 各就各位 一二三 跳 跳进染缸 看谁先 游向欲望 膨胀 膨胀 再膨胀 就像那数字一样 谁没有信仰 谁没有思想 谁没有最便宜的酒来陪葬",
    "我想要说的 前人们都说过了 我想要做的 有钱人都做过了 我想要的公平都是不公们虚构的 噢多么干净的一幅画 怎么会 怎么会 充满了悲伤 噢多么天真的一句话 怎么会 怎么会 像噩梦一样",
    "于是转身向山里走去 他明白 他明白 我给不起 于是转身向大海走去 我听着那少年的声音 在还有未来的过去 渴望着 美好结局 却没能成为自己",
    "你说你不想在这里 我也不想在这里 但天黑的太快想走早就来不及 喔 我爱你 可惜关系变成没关系 问题是没问题 于是我们继续 拿着笔想写点东西 以为是武器能伸张正义",
    "哭啊 喊啊叫你妈妈带你去买玩具啊 快 快拿到学校炫耀吧 孩子 交点朋友吧 哎呀呀你看你手上拿的是什么啊 那东西我们早就不屑啦",
    "从没想过要伤害谁 对一切也都感到抱歉 可是我的自卑胜过了一切爱我的 于是我把爱人们都杀死了 可是你的伤悲胜过了一切爱你的 于是你把我给杀死了",
    "别再说让它去吧 别再说让它去吧 杀了它 顺便杀了我 拜托你了 杀了它 顺便杀了我 拜托你了 你说是梦所以才痛 睡醒了再说 但那挫折和恐惧依旧 但那挫折和恐惧依旧 我把故乡给卖了 爱人给骗了",
    "又忍着失望的不解的痛恨的 又只用空瓶把今天砸碎 然后又哭着对离开了自己的影子道歉 别气了没有谁再跟你作对 别哭了没有谁会心碎 没有勇敢的人 你卖光了一切 你的肝和你的肺 他们扔了你的世界 去成为更好的人类 那廉价的眼泪就别挂在嘴边 什么也没改变 X2 请别举起手枪 这里没有反抗的人",
    "我们在原野上找一面墙 我们在标签里找方向 我们在废墟般的垃圾里找一块红砖 我们在工整的巷子里找家 找家 找 我们义无反顾的试着后悔 我们声嘶力竭的假装呐喊 我们万分惋惜的浪费着 用尽一切换来的纸张"
]

# 分词函数
def tokenize_lyrics(lyrics):
    tokenized_lyrics = []
    for line in lyrics:
        # 使用正则表达式分词，保留中文字符和空格
        tokens = re.findall(r'\S+|[^\s\w]+', line)
        tokenized_lyrics.append(tokens)
    return tokenized_lyrics

# 检查用户输入是否包含歌词中的字，并输出匹配中的单词或中文字符最多的歌词
def check_user_input(user_input, original_lyrics, previous_line, skip_count):
    max_match_count = 0
    matching_line = None
    first_char_match_line = None
    
    for line in original_lyrics:
        if line == previous_line and skip_count < 2:
            continue  # 跳过上一次匹配的行，直到skip_count达到2
    
        match_count = sum(1 for char in line if char in user_input)
        if match_count > max_match_count:
            max_match_count = match_count
            matching_line = line
        
        # 检查用户输入的第一个字是否是当前行歌词的第一个字
        if user_input and line and user_input[0] == line[0]:
            first_char_match_line = line
    
    # 如果有匹配到用户输入的第一个字是歌词行的第一个字，则优先输出该行
    if first_char_match_line:
        print(first_char_match_line)
        return first_char_match_line, 0  # 重置skip_count
    elif matching_line:
        print(matching_line)
        return matching_line, skip_count + 1  # 增加skip_count
    else:
        print("无匹配")
        return previous_line, skip_count + 1  # 增加skip_count，但不输出特定行

# 主函数
def main():
    tokenized_lyrics = tokenize_lyrics(lyrics)
    previous_line = None
    skip_count = 0
    
    while True:
        user_input = input("请输入内容（输入'q'以结束程序）：")
        if user_input == 'q':
            break
        
        previous_line, skip_count = check_user_input(user_input, lyrics, previous_line, skip_count)

if __name__ == "__main__":
    main()
