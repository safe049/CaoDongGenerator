import re
import random

# TODO:增加使用txt文件作为输入源的功能，并且一次性支持多个输入源
# TODO:添加更多歌词

# 歌词列表
lyrics = [
    "预备 各就各位 一二三 跳 跳进染缸 看谁先 游向欲望 膨胀 膨胀 再膨胀 就像那数字一样 谁没有信仰 谁没有思想 谁没有最便宜的酒 来陪葬",
    "我想要说的 前人们都说过了 我想要做的 有钱人都做过了 我想要的公平都是不公们虚构的 噢多么干净的一幅画 怎么会 怎么会 充满了悲伤 噢多么天真的一句话 怎么会 怎么会 像噩梦一样",
    "于是转身向山里走去 他明白 他明白 我给不起 于是转身向大海走去 我听着那少年的声音 在还有未来的过去 渴望着 美好结局 却没能成为自己",
    "你说你不想在这里 我也不想在这里 但天黑的太快想走早就来不及 喔 我爱你 可惜关系变成没关系 问题是没问题 于是我们继续 拿着笔想写点东西 以为是武器能伸张正义",
    "哭啊 喊啊 叫你妈妈带你去买玩具啊 快 快拿到学校炫耀吧 孩子 交点朋友吧 哎呀呀你看你手上拿的是什么啊 那东西我们早就不屑啦",
    "从没想过要伤害谁 对一切也都感到抱歉 可是我的自卑胜过了一切爱我的 于是我把爱人们都杀死了 可是你的伤悲胜过了一切爱你的 于是你把我给杀死了",
    "别再说让它去吧 别再说让它去吧 杀了它 顺便杀了我 拜托你了 杀了它 顺便杀了我 拜托你了 你说是梦所以才痛 睡醒了再说 但那挫折和恐惧依旧 但那挫折和恐惧依旧 我把故乡给卖了 爱人给骗了",
    "又忍着失望的不解的痛恨的 又只用空瓶把今天砸碎 然后又哭着对离开了自己的影子道歉 别气了没有谁再跟你作对 别哭了没有谁会心碎 没有勇敢的人 你卖光了一切 你的肝和你的肺 他们扔了你的世界 去成为更好的人类 那廉价的眼泪就别挂在嘴边 什么也没改变 什么也不改变 请别举起手枪 这里没有反抗的人",
    "我们在原野上找一面墙 我们在标签里找方向 我们在废墟般的垃圾里找一块红砖 我们在工整的巷子里找家 找家 找 我们义无反顾的试着后悔 我们声嘶力竭的假装呐喊 我们万分惋惜的浪费着 用尽一切换来的纸张",
    # 添加 《老张》
    "抹上了一身的泥巴 以为能消失在山上 却像个智障一样 醉倒在柏油路上 醉倒在柏油路上 还差一点 还差一点就把它抹上 还差一点 还差一点就不致于绝望 还差一点 就能跟他们都站在一起 还差一点 就能跟他们一起取笑我自己",
    # 添加《床》
    "看着窗外的光 分不清是路灯还是太阳 仔细搜索着自己的身体 试着找出一道合理的伤 却还是得说谎 筑起了对快乐的心防 说什么也放不下 从何时开始 对悲剧的向往 填满了整个心脏 筑起了对快乐的心防 说什么也放不下 从何时开始 对悲剧的向往 填满了整个心脏",
    #添加 《八》
    "喝得再醉 太阳还是出来了 学姐她最后还是嫁了个 王!八! 欸 交个朋友吧 欸 交个朋友吧 欸 交个朋友好吗 能不能也分我点说剩的话 可惜啊 我不是你想找的那个艺术家 从来没潇洒 可恨啊 怎么连烟跟酒都帮他 那到底是谁说的话",
    # 添加 《如常》
    "再给我一点 一点就好 好让我回到家 再看一眼 一眼就好 好让我回忆它 再说一遍 一遍就好 好让我放弃吧 再见一面 一面就好 聊聊那盆掉下楼的白花 空心的城墙 慌乱了日常 我们没差 就像昨天我们也没差 偷走了夕阳 黑白了无常 你们没差 就像明天你们也没差"
]

# 犬儒列表
lyrics_cynic = [
    # 添加《脏》
    "她扮成一朵受伤的花朵 殊不知是一个吃人的恶魔 站弱势的立场嫁祸又栽赃 黑色的心还要用圣洁来裹藏 好一朵白莲花 我怎么洗的掉 你泼给我的脏 祖安的国度隐身的指环 欲望被释放幽暗在扩散 无脑的狍子和跟风的猪狗 焚化了真相由不得你来解说 那光里面的黑 把正义化成匕首 刺向了他的咽喉",
    # 添加《天才艺术家》
    "他们在我的背后露出尖牙利爪 再往我的身上涂满口水泥巴 他们想拼命的把我往下拽啊 拽到那阴沟让污泥淹没我嘴巴 我懒得说 我也懒得讲 那你就继续做你的天才艺术家 画地为牢 保持风雅 继续在那井底里孤芳自赏",
    # 添加《病》
    "它赐我那种 让我生不如死的痛 而我却只能拥有一无所有的空 看着那些所谓正义和高尚的 百拙千丑的在咒骂着 他赐我那种笑着指鹿为马的疯 而我却只能拥有慷慨赴死的梦 看着那些所谓文明和胜利的 千夫所指地在审判着 我病了",
    # 添加《志铭》
    "谁来杀死那个巨婴 吸吮着霓虹和酒精 谁来审判他的罪行 无知的正义沦为笑柄 所以失落吧 呐喊无人倾听 所以回头吧 彼岸没有宿命 所以停步吧 出口禁止通行 所以放弃吧 理想化为泡影"
]

def lyrics_source_choose():
    """
    随机选择歌词来源，返回选中的歌词列表
    """
    if random.choice([True, False]):
        return lyrics
    else:
        return lyrics_cynic

# 分词函数 - 支持随机歌词来源
def tokenize_lyrics(lyrics):
    """
    将歌词列表进行分词处理，支持随机选择的歌词来源

    Args:
        lyrics: 歌词列表（可以是lyrics或lyrics_cynic中的任意一个）

    Returns:
        list: 分词后的歌词列表，每个元素是一个单词列表
    """
    tokenized_lyrics = []
    for line in lyrics:
        # 使用正则表达式分词，保留中文字符和空格
        tokens = re.findall(r'\S+|[^\s\w]+', line)
        tokenized_lyrics.append(tokens)
    return tokenized_lyrics

# 检查用户输入是否包含歌词中的字，并输出匹配中的单词或中文字符最多的歌词 - 支持随机歌词来源
def check_user_input(user_input, original_lyrics, previous_line, skip_count):
    """
    检查用户输入与歌词的匹配度，支持随机选择的歌词来源

    Args:
        user_input: 用户输入的文本
        original_lyrics: 原始歌词列表（可以是lyrics或lyrics_cynic中的任意一个）
        previous_line: 上一次匹配的歌词行
        skip_count: 跳过计数器

    Returns:
        tuple: (匹配的歌词行, 新的skip_count值)
    """
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

# 主函数 - 支持随机歌词来源选择
def main():
    """
    主程序入口，每次运行时随机选择歌词来源（普通歌词或犬儒歌词）
    """
    # 随机选择歌词来源 - 每次运行程序时都会随机选择使用lyrics或lyrics_cynic
    selected_lyrics = lyrics_source_choose()
    tokenized_lyrics = tokenize_lyrics(selected_lyrics)
    previous_line = None
    skip_count = 0

    while True:
        user_input = input("请输入内容（输入'q'以结束程序）：")
        if user_input == 'q':
            break

        previous_line, skip_count = check_user_input(user_input, selected_lyrics, previous_line, skip_count)

if __name__ == "__main__":
    main()
