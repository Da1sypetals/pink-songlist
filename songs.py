"""
name is expected to be a string.
singers is expected to be a string or a list of string.
tags is expected to be a string or a list of string.

I used Python file because it reports better syntax error than json
    and has loose syntax restrictions on trailing commas.
"""

songs = [
    {
        "name": "迟迟",
        "singers": ["银临"],
        "tags": ["古风"],
    },
    {
        "name": "宽窄巷",
        "singers": ["李常超"],
        "tags": ["古风"],
    },
    {
        "name": "扶摇",
        "singers": ["锦零"],
        "tags": ["原耽", "古风"],
    },
    {
        "name": "九万字",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "红白",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "人间不值得",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "来都来了",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "惊鹊",
        "singers": ["星尘", "忘川风华录"],
        "tags": ["古风"],
    },
    {
        "name": "万梦星",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "腐草为萤",
        "singers": ["银临"],
        "tags": ["古风", "古早"],
    },
    {
        "name": "棠梨煎雪",
        "singers": ["银临"],
        "tags": ["古风", "古早"],
    },
    {
        "name": "牵丝戏",
        "singers": ["Aki阿杰", "银临"],
        "tags": ["古风", "假声"],
    },
    {
        "name": "何以歌",
        "singers": ["Aki阿杰"],
        "tags": ["古风", "假声", "原耽"],
    },
    {
        "name": "落",
        "singers": ["艾辰"],
        "tags": ["古风"],
    },
    {
        "name": "愿",
        "singers": ["艾辰"],
        "tags": ["古风"],
    },
    {
        "name": "是风动",
        "singers": ["银临", "河图"],
        "tags": ["古风", "古早", "对唱"],
    },
    {
        "name": "泸沽寻梦",
        "singers": ["银临"],
        "tags": ["古风"],
    },
    {
        "name": "流光记",
        "singers": ["银临"],
        "tags": ["古风"],
    },
    {
        "name": "眉南边",
        "singers": ["银临"],
        "tags": ["古风"],
    },
    {
        "name": "卑微情书",
        "singers": ["银临"],
        "tags": ["情歌"],
    },
    {
        "name": "记忘歌",
        "singers": ["银临"],
        "tags": ["情歌"],
    },
    {
        "name": "青白",
        "singers": ["银临", "黄诗扶"],
        "tags": ["古风", "故事"],
    },
    {
        "name": "月球",
        "singers": ["银临"],
        "tags": ["梦幻"],
    },
    {
        "name": "怀梦之泽",
        "singers": ["银临", "泠鸢yousa"],
        "tags": ["古风"],
    },
    {
        "name": "予你成歌",
        "singers": ["千月兔"],
        "tags": ["大合唱"],
    },
    {
        "name": "迢迢",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "吹梦到西洲",
        "singers": ["黄诗扶", "妖扬"],
        "tags": ["古风"],
    },
    {
        "name": "由此去",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "孽海记",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "四万秋",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "过江寒",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "女驸马-她与她的花烛前",
        "singers": ["三无Marblue", "祖娅纳惜"],
        "tags": ["古风", "戏剧"],
    },
    {
        "name": "有鹿来",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "木兰行",
        "singers": ["忘川风华录"],
        "tags": ["古风", "燃曲"],
    },
    {
        "name": "  ",
        "singers": ["黄诗扶", "Winky诗"],
        "tags": ["古风", "合唱"],
    },
    {
        "name": "山湖共语",
        "singers": ["黄诗扶"],
        "tags": ["古风", "盗墓笔记"],
    },
    {
        "name": "一拜天地",
        "singers": ["Ay君", "畅畅酱"],
        "tags": ["古风", "原耽"],
    },
    {
        "name": "红拂夜奔",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "山花寻海树",
        "singers": ["黄诗扶"],
        "tags": ["古风", "轻快"],
    },
    {
        "name": "楚歌起",
        "singers": ["黄诗扶"],
        "tags": ["古风", "故事", "古代"],
    },
    {
        "name": "长相思",
        "singers": ["黄诗扶"],
        "tags": ["古风", "古代"],
    },
    {
        "name": "若风起时",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "你是我年少时求剑刻的舟",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "地久",
        "singers": ["黄诗扶"],
        "tags": ["故事", "流行"],
    },
    {
        "name": "纸伞",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "上邪",
        "singers": ["小曲儿"],
        "tags": ["古风"],
    },
    {
        "name": "山僧",
        "singers": ["小曲儿"],
        "tags": ["古风", "和风"],
    },
    {
        "name": "丹青客",
        "singers": ["HITA", "小曲儿"],
        "tags": ["古风", "对唱"],
    },
    {
        "name": "红尘",
        "singers": ["小曲儿"],
        "tags": ["古风"],
    },
    {
        "name": "不老梦",
        "singers": ["银临"],
        "tags": ["故事", "古风", "三拍子"],
    },
    {
        "name": "雪姬",
        "singers": ["黄诗扶"],
        "tags": ["古风", "三拍子"],
    },
    {
        "name": "紫禁城里的似水流年",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "珍珠",
        "singers": ["银临"],
        "tags": ["神话", "古风", "三拍子"],
    },
    {
        "name": "清平误",
        "singers": ["小曲儿"],
        "tags": ["古风"],
    },
    {
        "name": "谓我",
        "singers": ["小曲儿"],
        "tags": ["古风"],
    },
    {
        "name": "忘川",
        "singers": ["小曲儿"],
        "tags": ["古风"],
    },
    {
        "name": "于归",
        "singers": ["小曲儿"],
        "tags": ["古风"],
    },
    {
        "name": "松烟入墨",
        "singers": ["Winky诗"],
        "tags": ["古风"],
    },
    {
        "name": "梦望断",
        "singers": ["Winky诗"],
        "tags": ["古风"],
    },
    {
        "name": "何必诗债换酒钱",
        "singers": ["Winky诗", "佑可猫"],
        "tags": ["古风", "合唱"],
    },
    {
        "name": "楚天阔",
        "singers": ["Winky诗"],
        "tags": ["古风"],
    },
    {
        "name": "飞雪落红尘",
        "singers": ["KBShinya", "三无Marblue", "五音Jw"],
        "tags": ["古风", "未定事件簿"],
    },
    {
        "name": "红尘共长生",
        "singers": ["KBShinya", "三无Marblue", "陈亦洺"],
        "tags": ["古风", "未定事件簿"],
    },
    {
        "name": "晚夜微雨问海棠",
        "singers": ["陈亦洺", "喧笑"],
        "tags": ["古风", "原耽"],
    },
    {
        "name": "问情",
        "singers": ["陈亦洺", "尚辰"],
        "tags": ["古风", "原耽"],
    },
    {
        "name": "给某某",
        "singers": ["陈亦洺", "Mario"],
        "tags": ["原耽"],
    },
    {
        "name": "海棠又落微雨时",
        "singers": ["陈亦洺", "哦漏"],
        "tags": ["古风", "原耽"],
    },
    {
        "name": "千秋迭梦",
        "singers": ["陈亦洺", "尚辰"],
        "tags": ["古风", "原耽"],
    },
    {
        "name": "为龙",
        "singers": ["河图"],
        "tags": ["古风"],
    },
    {
        "name": "悦神",
        "singers": ["KBShinya"],
        "tags": ["古风"],
    },
    {
        "name": "致：黯淡星",
        "singers": ["KBShinya", "三无Marblue"],
        "tags": ["古风"],
    },
    {
        "name": "昔言",
        "singers": ["HITA"],
        "tags": ["古风", "假声", "无伴奏"],
    },
    {
        "name": "千梦",
        "singers": ["Aki阿杰", "HITA"],
        "tags": ["古风"],
    },
    {
        "name": "眉间雪",
        "singers": ["HITA"],
        "tags": ["古风", "剑网3", "故事"],
    },
    {
        "name": "霜雪千年",
        "singers": ["洛天依"],
        "tags": ["古风", "虚拟歌手"],
    },
    {
        "name": "琴师",
        "singers": ["音频怪物"],
        "tags": ["古风"],
    },
    {
        "name": "典狱司",
        "singers": ["音频怪物"],
        "tags": ["古风", "不会说唱"],
    },
    {
        "name": "长安忆",
        "singers": ["音频怪物"],
        "tags": ["古风"],
    },
    {
        "name": "我的一个道姑朋友",
        "singers": ["LON"],
        "tags": ["古风", "剑网3", "故事"],
    },
    {
        "name": "芳华慢",
        "singers": ["封茗囧菌"],
        "tags": ["古风"],
    },
    {
        "name": "伞下铭",
        "singers": ["封茗囧菌", "洛少爷"],
        "tags": ["古风", "对唱"],
    },
    {
        "name": "笛月",
        "singers": ["封茗囧菌", "双笙"],
        "tags": ["古风", "对唱"],
    },
    {
        "name": "巷",
        "singers": ["洛天依"],
        "tags": ["古风", "虚拟歌手"],
    },
    {
        "name": "繁华唱遍",
        "singers": ["乐正绫"],
        "tags": ["古风", "戏曲"],
    },
    {
        "name": "倘若无我",
        "singers": ["封茗囧菌", "洛少爷"],
        "tags": ["古风"],
    },
    {
        "name": "翩翩",
        "singers": ["封茗囧菌"],
        "tags": ["古风"],
    },
    {
        "name": "何日重到苏澜桥",
        "singers": ["泠鸢yousa"],
        "tags": ["古风", "故事"],
    },
    {
        "name": "今日重到苏澜桥",
        "singers": ["阿云嘎"],
        "tags": ["故事"],
    },
    {
        "name": "影子小姐",
        "singers": ["封茗囧菌"],
        "tags": ["伤情", "流行"],
    },
    {
        "name": "悟空",
        "singers": ["贰婶"],
        "tags": ["古风", "神话"],
    },
    {
        "name": "石楠小札",
        "singers": ["贰婶"],
        "tags": ["古风"],
    },
    {
        "name": "一首想不通的古风",
        "singers": ["玄觞", "贰婶"],
        "tags": ["古风"],
    },
    {
        "name": "狐言",
        "singers": ["河图", "洛天依"],
        "tags": ["古风", "假声"],
    },
    {
        "name": "伶人",
        "singers": ["排骨教主"],
        "tags": ["古风"],
    },
    {
        "name": "海棠",
        "singers": ["玄觞"],
        "tags": ["古风", "民国", "故事"],
    },
    {
        "name": "予君书",
        "singers": ["阿Yueyue"],
        "tags": ["古风"],
    },
    {
        "name": "云与海",
        "singers": ["阿Yueyue"],
        "tags": ["古风"],
    },
    {
        "name": "马文才",
        "singers": ["阿Yueyue"],
        "tags": ["古风", "故事", "梁祝"],
    },
    {
        "name": "沈园外",
        "singers": ["阿Yueyue"],
        "tags": ["古风"],
    },
    {
        "name": "无人诗",
        "singers": ["以冬"],
        "tags": ["古风"],
    },
    {
        "name": "多情岸",
        "singers": ["洛天依"],
        "tags": ["古风", "三拍子"],
    },
    {
        "name": "罚酒饮得",
        "singers": ["以冬"],
        "tags": ["古风"],
    },
    {
        "name": "未见青山老",
        "singers": ["以冬"],
        "tags": ["古风"],
    },
    {
        "name": "不觉秋色浅",
        "singers": ["以冬"],
        "tags": ["古风"],
    },
    {
        "name": "红叶寺",
        "singers": ["苏纬"],
        "tags": ["古风"],
    },
    {
        "name": "燃尽人间色",
        "singers": ["慕寒", "司夏", "河图", "子弥"],
        "tags": ["古风", "合唱"],
    },
    {
        "name": "人间应又雪",
        "singers": ["洛天依", "忘川风华录"],
        "tags": ["古风"],
    },
    {
        "name": "再见月光",
        "singers": ["河图"],
        "tags": ["古风"],
    },
    {
        "name": "霁夜茶",
        "singers": ["小曲儿"],
        "tags": ["古风"],
    },
    {
        "name": "鱼",
        "singers": ["西瓜JUN"],
        "tags": ["古风"],
    },
    {
        "name": "一花一剑",
        "singers": ["李鑫一"],
        "tags": ["原耽", "天官赐福"],
    },
    {
        "name": "红绝",
        "singers": ["胡夏"],
        "tags": ["古风"],
    },
    {
        "name": "千灯愿",
        "singers": ["弦森"],
        "tags": ["古风", "原耽", "天官赐福"],
    },
    {
        "name": "明月天涯",
        "singers": ["五音Jw"],
        "tags": ["古风", "燃曲"],
    },
    {
        "name": "雁城雪",
        "singers": ["小爱的妈"],
        "tags": ["古风"],
    },
    {
        "name": "江山雪",
        "singers": ["小爱的妈", "音频怪物"],
        "tags": ["古风"],
    },
    {
        "name": "白石溪",
        "singers": ["洛天依", "乐正绫"],
        "tags": ["古风", "古早"],
    },
    {
        "name": "Cinderella",
        "singers": ["泠鸢yousa"],
        "tags": ["童话", "故事"],
    },
    {
        "name": "木兰行",
        "singers": ["Assen捷", "双笙"],
        "tags": ["古风", "故事"],
    },
    {
        "name": "故人泪",
        "singers": ["麦小兜"],
        "tags": ["古风"],
    },
    {
        "name": "流光幻夜",
        "singers": ["司夏"],
        "tags": ["古风"],
    },
    {
        "name": "花开眉侧",
        "singers": ["慕寒", "三无Marblue"],
        "tags": ["古风"],
    },
    {
        "name": "杏花弦外雨",
        "singers": ["CRITTY", "司夏"],
        "tags": ["古风"],
    },
    {
        "name": "三月雨",
        "singers": ["洛天依", "泠鸢yousa"],
        "tags": ["古风"],
    },
    {
        "name": "步戏",
        "singers": ["五音Jw"],
        "tags": ["古风", "燃曲"],
    },
    {
        "name": "芊芊",
        "singers": ["回音哥"],
        "tags": ["古风"],
    },
    {
        "name": "吹灭小山河",
        "singers": ["司南"],
        "tags": ["古风"],
    },
    {
        "name": "朝露人间",
        "singers": ["司夏", "慕寒"],
        "tags": ["古风"],
    },
    {
        "name": "谓风",
        "singers": ["双笙", "流仙"],
        "tags": ["古风"],
    },
    {
        "name": "月出",
        "singers": ["双笙"],
        "tags": ["古风", "三拍子"],
    },
    {
        "name": "如是我闻",
        "singers": ["Winky诗"],
        "tags": ["古风", "三拍子"],
    },
    {
        "name": "雪落在先生肩上",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "赴鸿门",
        "singers": ["排骨教主"],
        "tags": ["古风", "对唱"],
    },
    {
        "name": "寻常歌",
        "singers": ["不才"],
        "tags": ["古风"],
    },
    {
        "name": "浮生未歇",
        "singers": ["音频怪物"],
        "tags": ["古早", "古风"],
    },
    {
        "name": "遇萤",
        "singers": ["CRITTY"],
        "tags": ["古风"],
    },
    {
        "name": "十年人间",
        "singers": ["李常超"],
        "tags": ["古风", "盗墓笔记"],
    },
    {
        "name": "东风志",
        "singers": ["Aki阿杰"],
        "tags": ["魔道祖师", "古风", "原耽"],
    },
    {
        "name": "三情旧雪",
        "singers": ["双笙"],
        "tags": ["古风"],
    },
    {
        "name": "桃花诺",
        "singers": ["邓紫棋"],
        "tags": ["古风", "古装剧"],
    },
    {
        "name": "折枝花满衣",
        "singers": ["泽典"],
        "tags": ["古风"],
    },
    {
        "name": "永定四十年",
        "singers": ["河图"],
        "tags": ["古风"],
    },
    {
        "name": "白马入芦花",
        "singers": ["河图"],
        "tags": ["古风"],
    },
    {
        "name": "第三十八年夏至",
        "singers": ["河图"],
        "tags": ["故事", "民国", "古风"],
    },
    {
        "name": "不谓侠",
        "singers": ["萧忆情"],
        "tags": ["古风"],
    },
    {
        "name": "若花怜蝶",
        "singers": ["萧忆情"],
        "tags": ["古风", "天官赐福", "原耽"],
    },
    {
        "name": "赐我",
        "singers": ["小时姑娘"],
        "tags": ["古风", "天官赐福", "原耽"],
    },
    {
        "name": "心上诗",
        "singers": ["黄诗扶"],
        "tags": ["古风", "故事"],
    },
    {
        "name": "云何住",
        "singers": ["黄诗扶"],
        "tags": ["古风", "故事"],
    },
    {
        "name": "良辰夜",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "蝶梦",
        "singers": ["黄诗扶"],
        "tags": ["古风", "梁祝"],
    },
    {
        "name": "晚来天欲雪",
        "singers": ["恋恋故人难", "云の泣"],
        "tags": ["古风"],
    },
    {
        "name": "心上秋",
        "singers": ["星尘", "忘川风华录"],
        "tags": ["古风"],
    },
    {
        "name": "盛世回首",
        "singers": ["Mario", "慕寒"],
        "tags": ["古风"],
    },
    {
        "name": "临安小记",
        "singers": ["西瓜JUN"],
        "tags": ["古风"],
    },
    {
        "name": "望江亭",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "周郎",
        "singers": ["音频怪物"],
        "tags": ["古风"],
    },
    {
        "name": "栖凰",
        "singers": ["三无MarBlue"],
        "tags": ["角色曲", "燃曲", "古风"],
    },
    {
        "name": "小城谣",
        "singers": ["洛少爷", "封茗囧菌"],
        "tags": ["对唱", "古风"],
    },
    {
        "name": "奈何天",
        "singers": ["黄诗扶"],
        "tags": ["古风"],
    },
    {
        "name": "夜奔",
        "singers": ["黄诗扶"],
        "tags": ["古风", "水浒", "燃曲", "三拍子"],
    },
    {
        "name": "剑与雪",
        "singers": ["星尘"],
        "tags": ["古风", "燃曲", "崩坏", "星穹铁道"],
    },
    {
        "name": "故事外的人",
        "singers": ["慕寒"],
        "tags": ["古风"],
    },
    {
        "name": "卧冰听雪",
        "singers": ["小爱的妈", "吾恩"],
        "tags": ["古风", "剑3"],
    },
    {
        "name": "逐浪飞花",
        "singers": ["贰婶"],
        "tags": ["古风"],
    },
]
