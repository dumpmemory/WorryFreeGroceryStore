## intent:ask_joke
- 不开心
- 我需要安慰
- 能不能给我讲一下笑话
- 给我讲个笑话呗
- 可以给我讲个笑话么？
- 听笑话
- 来个笑话
- 给我讲笑话
- 我想听笑话

## intent:ask_tea
- 请问，这边有什么茶呢？
- 有什么好茶推荐么？
- 这里比较热门的是什么茶？
- 好茶推荐

## intent:ask_refreshments
- 请问，这边有什么好吃的？
- 有什么好吃的推荐么？
- 这里比较热门的是什么小吃？
- 小吃推荐

## intent:ask_address
- 请问送货地址在哪里呢？
- 麻烦，留个收货地址！

## intent:ask_phone_number
- 需要手机号么？

## intent:request_tea
- 点[茶](tea)
- 喝[茶](tea)
- 帮我来杯[茶](tea)
- 我想来杯[茉莉花茶](tea)
- 我想来杯[少冰](temperature)[低糖](sugar)[茉莉花茶](tea)
- 我想来杯[热](temperature)[低糖](sugar)[碧螺春](tea)
- 我想来杯[常温](temperature)[无糖](sugar)[绿茶](tea)
- 我想来杯[常温](temperature)[龙井](tea)
- [无糖](sugar)
- [常温](temperature)
- [低糖](sugar)
- [热](temperature)
- [少冰](temperature)
- [加冰](temperature)
- [茉莉花茶](tea)
- [碧螺春](tea)
- [绿茶](tea)
- [龙井](tea)

## intent:request_refreshments
- 点餐
- 来个[蛋糕](refreshments)吧！
- 来点[好吃的](refreshments)吧！
- 来点[小吃](refreshments)吧！
- 上[菜](refreshments)吧！
- [蛋糕](refreshments)
- [肠粉](refreshments)
- [糕点](refreshments)

## intent:request_constellation
- 查星座
- 帮我查一下[巨蟹座](constellation)吧
- 帮我查一下[白羊座](constellation)呀
- 能不能和我说一下[双子座](constellation)
- 你知不知道[摩羯座](constellation)的女生这么样
- 可以和我说一下[巨蟹座](constellation)的男生么
- [天蝎座](constellation)
- [水瓶座](constellation)的介绍
- 介绍一下[金牛座](constellation)

## intent:request_takeway
- 点外卖
- 点份外卖
- 送份[蛋糕](refreshments)到[南山区阿里中心](address)
- 我要点外卖
- 点一份[肠粉](refreshments)，一杯[茉莉花茶](tea)，送到[南山区阿里中心](address)，电话号码为[13025240602](phone_number)
- 来一份[蛋糕](refreshments)和[肠粉](refreshments)，一杯[碧螺春](tea)，电话号码为[13025240602](phone_number)
- 麻烦送一份[蛋糕](refreshments)到[南山区](address)

<!--Regular Expression Features-->
## regex:phone_number
- ((\d{3,4}-)?\d{7,8})|(((\+86)|(86))?(1)\d{10})

## lookup:constellation
- data/lookup_tables/constellation.txt

## intent:greet
- 你好
- 你好啊
- 早上好
- 晚上好
- hello
- hi
- 嗨
- 嗨喽
- 见到你很高兴
- 嘿
- 早
- 上午好
- hello哈喽
- 哈喽哈喽
- hello hello
- 喂喂

## intent:goodbye
- goodbye
- bye
- bye bye
- 88
- 886
- 再见
- 拜
- 拜拜
- 拜拜，下次再聊
- 下次见
- 回头见
- 下次再见
- 下次再聊
- 有空再聊
- 先这样吧
- 好了，就说这么多了
- 好了，先这样
- 没事

## intent:whoareyou
- 你是谁
- 我知道你吗
- 谁
- 我认识你吗
- 这是谁啊
- 是谁
- 请问你是谁
- 请问我认识你吗
- 你是哪位
- 你是？
- 是谁？
- 可以告诉我你的名字吗
- 你叫什么名字

## intent:whattodo
- 你支持什么功能
- 你有什么功能
- 你能干什么
- 你能做什么

## intent:thanks
- 谢谢
- thanks
- thank you
- 真的太感谢你了，帮了我大忙
- 谢谢你帮了我大忙
- 你帮了我大忙，谢谢你小智
- 非常感谢
- 谢了

## intent:deny
- 不
- no
- 不可以
- 不是的
- 不认同
- 否定
- 不是这样子的
- 我不同意你的观点
- 不同意
- 不好
- 你长得很美，就不要想得太美。
- 拒绝
- 不行

## intent:affirm
- 是的
- 当然
- 好的
- ok
- 嗯
- 可以
- 你可以这么做
- 你做得可以啊
- 同意
- 听起来不错
- 是这样的
- 的确是这样子的
- 我同意你的观点
- 对的
- 好滴
- 行
- 还行
- 当然可以
