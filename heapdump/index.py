import random
import time

from heapdump import api

c_list = ["枕上诗书闲处好，门前风景雨来佳。——李清照《摊破浣溪沙·病起萧萧两鬓华》",
          "我的成就，当归功于精力的思索。——牛顿",
          "学而时习之，不亦说乎？——佚名《论语十则》",
          "读书何所求，将以通事理。——张维屏",
          "书犹药也，善读之可以医愚。——刘向",
          "悲吟雨雪动林木，放书辍剑思高堂。——李白《留别于十一兄逖裴十三游塞垣》",
          "闲门向山路，深柳读书堂。——刘昚虚《阙题》",
          "读书时要深思多问。只读而不想，就可能人云亦云，沦为书本的奴隶；或者走马看花，所获甚微。——王梓坤",
          "学习有两忌，自高和自狭。——书摘",
          "不怕读得少，只怕记不牢。——徐特立",
          "富贵必从勤苦得，男儿须读五车书。——杜甫《柏学士茅屋》",
          "书当快意读易尽，客有可人期不来。——陈师道《绝句·书当快意读易尽》",
          "惜时专心苦读是做学问的一个好方法。——蔡尚思",
          "一日不读书，胸臆无佳想。——萧抡谓《读书有所见作》",
          "在读书上，数量并不列于首要，重要的是书的品质与所引起的思索的程度。——富兰克林",
          "从来没有人为了读书而读书，只有在书中读自己，在书中发现自己，或检查自己。——罗曼·罗兰",
          "归志宁无五亩园，读书本意在元元。——陆游《读书》",
          "奇文共欣赏，疑义相与析。——陶渊明《移居二首》",
          "黑发不知勤学早，白首方悔读书迟。——颜真卿《劝学诗》",
          "李杜诗篇万口传，至今已觉不新鲜。——赵翼《论诗五首》",
          "书本上的知识而外，尚须从生活的人生中获得知识。——茅盾",
          "生活在我们这个世界里，不读书就完全不可能了解人。——高尔基",
          "细读离骚还痛饮，饱看修竹何妨肉。——辛弃疾《满江红·山居即事》",
          "笔落惊风雨，诗成泣鬼神。——杜甫",
          "三更灯火五更鸡，正是男儿读书时。——颜真卿《劝学诗》",
          "因依老宿发心初，半学修心半读书。——王建《寄旧山僧》",
          "一月不读书，耳目失精爽。——萧抡谓《读书有所见作》",
          "知识有如人体血液一样宝贵。人缺了血液，身体就会衰弱；人缺少知识，头脑就要枯竭。——高士其",
          "三冬暂就儒生学，千耦还从父老耕。——陆游《观村童戏溪上》",
          "传屐朝寻药，分灯夜读书。——于鹄《题邻居》",
          "不去读书就没有真正的教养，同时也不可能有什么鉴别力。——赫尔岑",
          "灯前目力虽非昔，犹课蝇头二万言。——陆游《读书》",
          "读书不觉已春深，一寸光阴一寸金。——王贞白《白鹿洞二首·其一》",
          "夫所以读书学问，本欲开心明目，利于行耳。——颜之推",
          "谤书盈箧不复辩，脱身来看江南山。——谢逸《送董元达》",
          "读书，人才更加像人。——严文井",
          "年轻只知学习营利，乃生命中最黯淡之时刻。——格里尔",
          "出师一表通今古，夜半挑灯更细看。——陆游《病起书怀》",
          "旧书不厌百回读，熟读精思子自知。——苏轼",
          "学习这件事不在乎有没有人教你，最重要的是在于你自己有没有觉悟和恒心。——法布尔",
          "儿大诗书女丝麻，公但读书煮春茶。——黄庭坚《送王郎》",
          "不学而求知，犹愿鱼而无网。——葛洪",
          "学习是劳动，是充满思想的劳动。——乌申斯基",
          "活着就要学习，学习不是为了活着。——培根",
          "金鞍玉勒寻芳客，未信我庐别有春。——于谦《观书》",
          "理想的书籍是智慧的钥匙。——列夫·托尔斯泰",
          "一本书像一艘船，带领我们从狭獈的地方，驶向生活的无限广阔的海洋。——凯勒",
          "学者如登山焉，动而益高，如寤寐焉，久而益足。——徐干",
          "安居不用架高堂，书中自有黄金屋。——赵恒《劝学诗》",
          " 生活便是寻求新的知识。——门捷列夫",
          "理想的书籍，是智慧的钥匙。——列夫·托尔斯泰",
          "一本新书象一艘船，带领我们从狭隘的地方，驰向无限广阔的生活的海洋。——凯勒",
          "勤劳一日，可得一夜安眠；勤劳一生，可得幸福长眠。——达·芬奇",
          "当我们第一遍读一本好书的时候，我们仿佛觉得找到了一个朋友；当我们再一次读这本书的时候，仿佛又和老朋友重逢。——伏尔泰",
          "读书是我唯一的娱乐。我不把时间浪费于酒店、赌博或任何一种恶劣的游戏。——富兰克林",
          "知识是珍贵宝石的结晶，文化是宝石放出来的光泽。——泰戈尔",
          "不积跬步，无以至千里；不积小流，无以成江海。——荀况",
          "好奇心造就科学家和诗人。——法朗士",
          "没有任何动物比蚂蚁更勤奋，然而它却最沉默寡言。——富兰克林",
          "三日不读书，便觉语言无味。——朱舜水",
          "聪明出于勤奋，天才在于积累。——华罗庚",
          "我闭南楼看道书，幽帘清寂在仙居。——李白《早秋单父南楼酬窦公衡》",
          "对所学知识内容的兴趣可能成为学习动机。——赞科夫",
          "阅读一切好书如同和过去最杰出的人谈话。——笛卡儿",
          "书卷多情似故人，晨昏忧乐每相亲。——于谦",
          "弱龄寄事外，委怀在琴书。——陶渊明《始作镇军参军经曲阿作》",
          "粗缯大布裹生涯，腹有诗书气自华。——苏轼《和董传留别》",
          "学习知识要善于思考，思考，再思考。——爱因斯坦",
          "坑灰未冷山东乱，刘项原来不读书。——章碣《焚书坑》",
          "人学始知道，不学非自然。——孟郊《劝学》",
          "我们要像海绵一样吸收有用的知识。——加里宁",
          "灯火纸窗修竹里，读书声。——陈继儒《浣溪沙·初夏夜饮归》"]


def new_like_discuss(session, seq_id, content):
    # 点赞
    api.add_like(session, seq_id)
    # 评论
    api.discuss(session, seq_id, content)


def auto():
    session = api.session()
    session.cookies.set("serviceTicket", "e7ae53b20fc240e1a18555fbc3cce680")
    api.is_signin(session)
    i = random.randrange(1, 100)
    time.sleep(i)
    # 签到
    api.add_signin(session)
    # page = 1
    # size = 10
    # # 文章列表
    # new_list_result = api.new_list(session, page, size)
    # # 获取总页数
    # if new_list_result["extra"]["total"] % new_list_result["extra"]["pageSize"] == 0:
    #     sum_pages = int(new_list_result["extra"]["total"] / new_list_result["extra"]["pageSize"])
    # else:
    #     sum_pages = int(new_list_result["extra"]["total"] / new_list_result["extra"]["pageSize"]) + 1
    #
    # for i in range(5):
    #     print("开始第" + str(i + 1) + "次循环")
    #     time.sleep(10)
    #     page = random.randrange(1, sum_pages)
    #     new_list_result = api.new_list(session, page, size)
    #     time.sleep(15)
    #     new_list_index = random.randrange(1, size)
    #     seq_id = new_list_result["data"][new_list_index]["seqId"]
    #     time.sleep(36)
    #     new_like_discuss(session, seq_id, c_list[random.randrange(1, len(c_list))])
    #     print("结束第" + str(i + 1) + "次循环")


def test():
    session = api.session()
    session.cookies.set("serviceTicket", "e7ae53b20fc240e1a18555fbc3cce680a")
    r = api.current_month_sigin(session)
    print(r)
