# 解忧杂货店

> 作者：杨夕
> 
> 项目地址：https://github.com/km1994/nlp_paper_study
> 
> 个人介绍：大佬们好，我叫杨夕，该项目主要是本人在研读顶会论文和复现经典论文过程中，所见、所思、所想、所闻，可能存在一些理解错误，希望大佬们多多指正。

## 目录

- [解忧杂货店](#解忧杂货店)
  - [目录](#目录)
  - [一、动机](#一动机)
  - [二、开发手册](#二开发手册)
    - [2.1 在 data/nlu.md 添加 意图 intent 【以添加 点外卖为例】](#21-在-datanlumd-添加-意图-intent-以添加-点外卖为例)
    - [2.2 在 data/stories.md 添加 意图 intent 所对应的触发 事件 【以添加 点外卖为例】](#22-在-datastoriesmd-添加-意图-intent-所对应的触发-事件-以添加-点外卖为例)
    - [2.3 在 domain.yml 配置意图 和 事件 【以添加 点外卖为例】](#23-在-domainyml-配置意图-和-事件-以添加-点外卖为例)
    - [2.4 在 actions.py 自定义 Action 【以添加 点外卖为例】](#24-在-actionspy-自定义-action-以添加-点外卖为例)
  - [三、启动 服务](#三启动-服务)
    - [3.1 验证 配置数据](#31-验证-配置数据)
    - [3.2 模型训练](#32-模型训练)
    - [3.3 模型启动](#33-模型启动)
    - [3.4 模型测试](#34-模型测试)
  - [实现功能 介绍](#实现功能-介绍)
    - [V3.0 外卖配送员 夕仔 【2020.09.28】](#v30-外卖配送员-夕仔-20200928)
    - [V2.0 星座占卜师 夕酱 【2020.09.26】](#v20-星座占卜师-夕酱-20200926)
    - [V1.0 茶餐厅 店小二 小夕 【2020.09.25】](#v10-茶餐厅-店小二-小夕-20200925)

## 一、动机

```s
  现代人内心流失的东西，这家杂货店能帮你找回——

  僻静的街道旁有一家杂货店，只要写下烦恼投进卷帘门的投信口；
  
  第二天就会在店后的牛奶箱里得到回答。

  因男友身患绝症，年轻女孩静子在爱情与梦想间徘徊；

  克郎为了音乐梦想离家漂泊，却在现实中寸步难行；

  少年浩介面临家庭巨变，挣扎在亲情与未来的迷茫中……

  他们将困惑写成信投进杂货店，随即奇妙的事情竟不断发生。

  生命中的一次偶然交会，将如何演绎出截然不同的人生？

  如今回顾写作过程，我发现自己始终在思考一个问题：站在人生的岔路口，人究竟应该怎么做？
  
  我希望读者能在掩卷时喃喃自语：我从未读过这样的小说。
  
    ——东野圭吾
```

当你 看完 上面 那段话，是不是也觉得 蛮有 感触的？是的，我第一次看这一本，觉得特别有感触，所以 基于 该 动机，用 Rasa 框架，为自己写了一个 “解忧杂货店”。


## 二、开发手册

### 2.1 在 data/nlu.md 添加 意图 intent 【以添加 点外卖为例】

- 确定 意图 名称：request_takeway；
- 确定需要的 槽位：refreshments、tea、address、phone_number；
- 确定 用户 query；
- 确定 当 某个 槽位 为空时，Bot 通过回复 什么获取 对应 槽位值

> 举例

```s
## intent: ask_tea
- 请问，这边有什么茶呢？
...

## intent: ask_refreshments
- 请问，这边有什么好吃的？
...

## intent: ask_address
- 请问送货地址在哪里呢？
...

## intent: ask_phone_number
- 需要手机号么？

## intent: request_takeway
- 点份外卖
- 点一份[肠粉](refreshments)，一杯[茉莉花茶](tea)，送到[南山区](address)，电话号码为[13025240602](phone_number)
- 麻烦送一份[蛋糕](refreshments)到[南山区](address)
- ...
```

### 2.2 在 data/stories.md 添加 意图 intent 所对应的触发 事件 【以添加 点外卖为例】

```s
## request takeway
* request_takeway # 意图
 - takeway_form# 触发表单事件
 - form{"name": "takeway_form"}  # 表单事件名称
 - form{"name": null}
```

### 2.3 在 domain.yml 配置意图 和 事件 【以添加 点外卖为例】

- 设置 意图 intent
```s
intents:
  - ask_tea
  - ask_refreshments
  - ask_phone_number
  - ask_address
  - request_takeway
  ...
```
- 设置 槽位 slots
```s
slots:
  tea:
 type: unfeaturized
  refreshments:
 type: unfeaturized
  phone_number:
 type: unfeaturized
  address:
 type: unfeaturized
  ...
```
- 设置 实体 entities
```s
entities:
  - tea
  - refreshments
  - constellation
  - phone_number
  - address
  ...
```
- 设置 事件 actions
```s
actions:
  - utter_ask_refreshments
  - utter_ask_tea
  - utter_ask_phone_number
  - utter_ask_address
  ...
```
- 设置 表单事件 forms
```s
forms:
  - takeway_form
  ...
```
- 设置 Bot 回复
```s
responses:
  utter_ask_tea:
 - text: "您好！很高兴为您服务，我们这边目前茶可多了！有红茶、绿茶、普洱茶、铁观音、碧螺春、还有上好的龙井，请问你要哪一种呢？"

  utter_ask_refreshments:
 - text: "您好！很高兴为您服务，我们这边目前茶点可多了！有蛋糕、肠粉、还有好吃停不下来的糕点，请问你要哪一种呢？"
 
  utter_ask_phone_number:
 - text: "客官，请问您手机号码多少呀？"
 - text: "麻烦给我手机号呗！"
 - text: "麻烦给我一个联系方式"
 - text: "能否提供一下您的联系方式呢？"

  utter_ask_address:
 - text: "麻烦留个收货地址"
 - text: "请问，你在哪里呢？"

  utter_default:
 - text: "没听懂，请换种说法吧~"
```

### 2.4 在 actions.py 自定义 Action 【以添加 点外卖为例】
```s
# action tea_form
class TakewayForm(FormAction):
 def name(self) -> Text:
  """Unique identifier of the form"""
  return "takeway_form"

 @staticmethod
 def required_slots(tracker: Tracker) -> List[Text]:
  """A list of required slots that the form has to fill"""
  return ["refreshments", "tea", "address","phone_number"]

 def submit(
  self,
  dispatcher: CollectingDispatcher,
  tracker: Tracker,
  domain: Dict[Text, Any],
 ) -> List[Dict]:
  """Define what the form has to do
after all required slots are filled"""
  tea = tracker.get_slot('tea')
  refreshments = tracker.get_slot('refreshments')
  address = tracker.get_slot('address')
  phone_number = tracker.get_slot('phone_number')
  dispatcher.utter_message("{}和{}已经在制作中，麻烦十分钟后到{}拿，并保证手机号{}畅通".format(refreshments,tea,address,phone_number))
  return [Restarted()]
```

## 三、启动 服务

### 3.1 验证 配置数据

- 验证

```s
$ python -m rasa data validate
/home/amy/.conda/envs/rasa/lib/python3.6/site-packages/rasa/core/domain.py:151: FutureWarning: No tracker session configuration was found in the loaded domain. Domains without a session config will automatically receive a session expiration time of 60 minutes in Rasa version 2.0 if not configured otherwise.
  session_config = cls._get_session_config(data.get(SESSION_CONFIG_KEY, {}))
2020-09-25 09:15:00 INFO  rasa.validator  - Validating intents...
2020-09-25 09:15:00 INFO  rasa.validator  - Validating uniqueness of intents and stories...
2020-09-25 09:15:00 INFO  rasa.validator  - Validating utterances...
2020-09-25 09:15:00 INFO  rasa.validator  - Story structure validation...
Processed Story Blocks: 100%|█████████████████████████████████████| 17/17 [00:00<00:00, 4121.57it/s, # trackers=1]
2020-09-25 09:15:00 INFO  rasa.core.training.story_conflict  - Considering the preceding 6 turns for conflict analysis.
2020-09-25 09:15:00 INFO  rasa.validator  - No story structure conflicts found.
```

### 3.2 模型训练

```s
...
$python -m rasa train --config config.yml --domain domain.yml --data data/
C: 0.400586f-score: 0.909091
best C: 0.400586
test on train: 
12  0  0  0  0  0  0 
 0  5  0  0  0  0  0 
 0  0  7  0  0  0  0 
 0  0  0 10  0  0  0 
 0  0  0  0  8  0  0 
 0  0  0  0  0  2  0 
 0  0  0  0  0  0  2 

overall accuracy: 1
Part II: elapsed time: 734 seconds.
df.number_of_classes(): 7
2020-09-28 17:45:27 INFO  rasa.nlu.model  - Finished training component.
2020-09-28 17:45:27 INFO  rasa.nlu.model  - Starting to train component EntitySynonymMapper
2020-09-28 17:45:27 INFO  rasa.nlu.model  - Finished training component.
2020-09-28 17:45:27 INFO  rasa.nlu.model  - Starting to train component RegexFeaturizer
2020-09-28 17:45:27 INFO  rasa.nlu.model  - Finished training component.
2020-09-28 17:45:27 INFO  rasa.nlu.model  - Starting to train component MitieFeaturizer
2020-09-28 17:45:27 INFO  rasa.nlu.model  - Finished training component.
2020-09-28 17:45:27 INFO  rasa.nlu.model  - Starting to train component SklearnIntentClassifier
Fitting 2 folds for each of 6 candidates, totalling 12 fits
[Parallel(n_jobs=1)]: Using backend SequentialBackend with 1 concurrent workers.
[Parallel(n_jobs=1)]: Done  12 out of  12 | elapsed: 0.4s finished
2020-09-28 17:45:27 INFO  rasa.nlu.model  - Finished training component.
2020-09-28 17:45:28 INFO  rasa.nlu.model  - Successfully saved model into '/tmp/tmp1dq8kb7k/nlu'
NLU model training completed.
Your Rasa model is trained and saved at 'models/20200928-174528.tar.gz'.
```

### 3.3 模型启动

```s
(rasa) [amy@bjht-gpu-006 rasa_project]$ python -m rasa run actions --port 5055 --actions actions --debug
2020-09-28 19:45:05 INFO  rasa_sdk.endpoint  - Starting action endpoint server...
函数：loadDict() 共耗时约 0.00021 秒
...
2020-09-28 19:45:05 INFO  rasa_sdk.executor  - Registered function for 'action_default_fallback'.
2020-09-28 19:45:05 INFO  rasa_sdk.executor  - Registered function for 'tea_form'.
2020-09-28 19:45:05 INFO  rasa_sdk.executor  - Registered function for 'takeway_form'.
2020-09-28 19:45:05 INFO  rasa_sdk.executor  - Registered function for 'refreshments_form'.
2020-09-28 19:45:05 INFO  rasa_sdk.executor  - Registered function for 'constellation_form'.
2020-09-28 19:45:05 INFO  rasa_sdk.endpoint  - Action endpoint is up and running on http://localhost:5055
2020-09-28 19:45:05 DEBUG rasa_sdk.utils  - Using the default number of Sanic workers (1).

```

### 3.4 模型测试

- 客户端【注：需要另开出口】
```s
$ rasa shell
2020-09-28 20:39:12 INFO  root  - Connecting to channel 'cmdline' which was specified by the '--connector' argument. Any other channels will be ignored. To connect to all given channels, omit the '--connector' argument.
2020-09-28 20:39:12 INFO  root  - Starting Rasa server on http://localhost:5005
2020-09-28 20:39:17 INFO  rasa.nlu.components  - Added 'MitieNLP' to component cache. Key 'MitieNLP-/web/workspace/yangkm/python_wp/nlu/DSwP/rasa_project/data/total_word_feature_extractor_zh.dat'.
/home/amy/.conda/envs/rasa/lib/python3.6/site-packages/rasa/core/policies/keras_policy.py:265: FutureWarning: 'KerasPolicy' is deprecated and will be removed in version 2.0. Use 'TEDPolicy' instead.
  current_epoch=meta["epochs"],
2020-09-28 20:39:21 INFO  rasa.core.policies.ensemble  - MappingPolicy not included in policy ensemble. Default intents 'restart and back will not trigger actions 'action_restart' and 'action_back'.
2020-09-28 20:39:21 INFO  root  - Rasa server is up and running.
Bot loaded. Type a message and press enter (use '/stop' to exit): 
Your input ->  点外卖 
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 1.050 seconds.
Prefix dict has been built successfully.
您好！很高兴为您服务，我们这边目前茶点可多了！有蛋糕、肠粉、还有好吃停不下来的糕点，请问你要哪一种呢？
Your input ->  蛋糕
您好！很高兴为您服务，我们这边目前茶可多了！有红茶、绿茶、普洱茶、铁观音、碧螺春、还有上好的龙井，请问你要哪一种呢？
Your input ->  绿茶
麻烦留个收货地址
Your input ->  南山区 
麻烦给我一个联系方式
Your input ->  1234567890
蛋糕和绿茶已经在制作中，麻烦十分钟后到南山区拿，并保证手机号1234567890畅通
```

- 服务器响应【注：日志打印情况】
```s
2020-09-28 20:39:27 DEBUG    rasa_sdk.executor  - Received request to run 'takeway_form'
2020-09-28 20:39:27 DEBUG    rasa_sdk.forms  - There is no active form
2020-09-28 20:39:27 DEBUG    rasa_sdk.forms  - Activated the form 'takeway_form'
2020-09-28 20:39:27 DEBUG    rasa_sdk.forms  - No pre-filled required slots to validate.
2020-09-28 20:39:27 DEBUG    rasa_sdk.forms  - Validating user input '{'intent': {'name': 'request_takeway', 'confidence': 0.3650815377324046}, 'entities': [], 'intent_ranking': [{'name': 'request_takeway', 'confidence': 0.3650815377324046}, {'name': 'request_refreshments', 'confidence': 0.1283786319709406}, {'name': 'affirm', 'confidence': 0.09685220818783706}, {'name': 'deny', 'confidence': 0.06193598647737689}, {'name': 'greet', 'confidence': 0.05224842734238164}, {'name': 'request_tea', 'confidence': 0.050255186559431474}, {'name': 'ask_refreshments', 'confidence': 0.04790402495089106}, {'name': 'goodbye', 'confidence': 0.044566111991724715}, {'name': 'ask_tea', 'confidence': 0.03826858735731229}, {'name': 'thanks', 'confidence': 0.029488916301876618}], 'text': '点外卖'}'
2020-09-28 20:39:27 DEBUG    rasa_sdk.forms  - Validating extracted slots: {}
2020-09-28 20:39:27 DEBUG    rasa_sdk.forms  - Request next slot 'refreshments'
2020-09-28 20:39:27 DEBUG    rasa_sdk.executor  - Finished running 'takeway_form'
2020-09-28 20:39:39 DEBUG    rasa_sdk.executor  - Received request to run 'takeway_form'
2020-09-28 20:39:39 DEBUG    rasa_sdk.forms  - The form '{'name': 'takeway_form', 'validate': True, 'rejected': False, 'trigger_message': {'intent': {'name': 'request_takeway', 'confidence': 0.3650815377324046}, 'entities': [], 'intent_ranking': [{'name': 'request_takeway', 'confidence': 0.3650815377324046}, {'name': 'request_refreshments', 'confidence': 0.1283786319709406}, {'name': 'affirm', 'confidence': 0.09685220818783706}, {'name': 'deny', 'confidence': 0.06193598647737689}, {'name': 'greet', 'confidence': 0.05224842734238164}, {'name': 'request_tea', 'confidence': 0.050255186559431474}, {'name': 'ask_refreshments', 'confidence': 0.04790402495089106}, {'name': 'goodbye', 'confidence': 0.044566111991724715}, {'name': 'ask_tea', 'confidence': 0.03826858735731229}, {'name': 'thanks', 'confidence': 0.029488916301876618}], 'text': '点外卖'}}' is active
2020-09-28 20:39:39 DEBUG    rasa_sdk.forms  - Validating user input '{'intent': {'name': 'request_refreshments', 'confidence': 0.43804135774879477}, 'entities': [{'entity': 'refreshments', 'value': '蛋糕', 'start': 0, 'end': 2, 'confidence': None, 'extractor': 'MitieEntityExtractor'}], 'intent_ranking': [{'name': 'request_refreshments', 'confidence': 0.43804135774879477}, {'name': 'request_tea', 'confidence': 0.09640327838926412}, {'name': 'ask_tea', 'confidence': 0.06635970697107835}, {'name': 'affirm', 'confidence': 0.0658339469276381}, {'name': 'request_takeway', 'confidence': 0.061845170153657515}, {'name': 'ask_refreshments', 'confidence': 0.0463581040961074}, {'name': 'deny', 'confidence': 0.039133683849537956}, {'name': 'greet', 'confidence': 0.035469583713187966}, {'name': 'thanks', 'confidence': 0.03402896442851343}, {'name': 'whoareyou', 'confidence': 0.02642424236843663}], 'text': '蛋糕'}'
2020-09-28 20:39:39 DEBUG    rasa_sdk.forms  - Trying to extract requested slot 'refreshments' ...
2020-09-28 20:39:39 DEBUG    rasa_sdk.forms  - Got mapping '{'type': 'from_entity', 'entity': 'refreshments', 'intent': [], 'not_intent': [], 'role': None, 'group': None}'
2020-09-28 20:39:39 DEBUG    rasa_sdk.forms  - Successfully extracted '蛋糕' for requested slot 'refreshments'
2020-09-28 20:39:39 DEBUG    rasa_sdk.forms  - Validating extracted slots: {'refreshments': '蛋糕'}
2020-09-28 20:39:39 DEBUG    rasa_sdk.forms  - Request next slot 'tea'
2020-09-28 20:39:39 DEBUG    rasa_sdk.executor  - Finished running 'takeway_form'
2020-09-28 20:39:46 DEBUG    rasa_sdk.executor  - Received request to run 'takeway_form'
2020-09-28 20:39:46 DEBUG    rasa_sdk.forms  - The form '{'name': 'takeway_form', 'validate': True, 'rejected': False, 'trigger_message': {'intent': {'name': 'request_takeway', 'confidence': 0.3650815377324046}, 'entities': [], 'intent_ranking': [{'name': 'request_takeway', 'confidence': 0.3650815377324046}, {'name': 'request_refreshments', 'confidence': 0.1283786319709406}, {'name': 'affirm', 'confidence': 0.09685220818783706}, {'name': 'deny', 'confidence': 0.06193598647737689}, {'name': 'greet', 'confidence': 0.05224842734238164}, {'name': 'request_tea', 'confidence': 0.050255186559431474}, {'name': 'ask_refreshments', 'confidence': 0.04790402495089106}, {'name': 'goodbye', 'confidence': 0.044566111991724715}, {'name': 'ask_tea', 'confidence': 0.03826858735731229}, {'name': 'thanks', 'confidence': 0.029488916301876618}], 'text': '点外卖'}}' is active
2020-09-28 20:39:46 DEBUG    rasa_sdk.forms  - Validating user input '{'intent': {'name': 'request_tea', 'confidence': 0.7057777843669419}, 'entities': [{'entity': 'tea', 'value': '绿茶', 'start': 0, 'end': 2, 'confidence': None, 'extractor': 'MitieEntityExtractor'}], 'intent_ranking': [{'name': 'request_tea', 'confidence': 0.7057777843669419}, {'name': 'ask_tea', 'confidence': 0.05125603502962094}, {'name': 'goodbye', 'confidence': 0.03762581720064695}, {'name': 'request_refreshments', 'confidence': 0.03380424122576896}, {'name': 'request_takeway', 'confidence': 0.024729993288347185}, {'name': 'affirm', 'confidence': 0.020769895216799106}, {'name': 'greet', 'confidence': 0.02048504208087665}, {'name': 'ask_refreshments', 'confidence': 0.02018017851971949}, {'name': 'thanks', 'confidence': 0.01817229676035654}, {'name': 'request_constellation', 'confidence': 0.018102062378125068}], 'text': '绿茶'}'
2020-09-28 20:39:46 DEBUG    rasa_sdk.forms  - Trying to extract requested slot 'tea' ...
2020-09-28 20:39:46 DEBUG    rasa_sdk.forms  - Got mapping '{'type': 'from_entity', 'entity': 'tea', 'intent': [], 'not_intent': [], 'role': None, 'group': None}'
2020-09-28 20:39:46 DEBUG    rasa_sdk.forms  - Successfully extracted '绿茶' for requested slot 'tea'
2020-09-28 20:39:46 DEBUG    rasa_sdk.forms  - Validating extracted slots: {'tea': '绿茶'}
2020-09-28 20:39:46 DEBUG    rasa_sdk.forms  - Request next slot 'address'
2020-09-28 20:39:46 DEBUG    rasa_sdk.executor  - Finished running 'takeway_form'
2020-09-28 20:39:54 DEBUG    rasa_sdk.executor  - Received request to run 'takeway_form'
2020-09-28 20:39:54 DEBUG    rasa_sdk.forms  - The form '{'name': 'takeway_form', 'validate': True, 'rejected': False, 'trigger_message': {'intent': {'name': 'request_takeway', 'confidence': 0.3650815377324046}, 'entities': [], 'intent_ranking': [{'name': 'request_takeway', 'confidence': 0.3650815377324046}, {'name': 'request_refreshments', 'confidence': 0.1283786319709406}, {'name': 'affirm', 'confidence': 0.09685220818783706}, {'name': 'deny', 'confidence': 0.06193598647737689}, {'name': 'greet', 'confidence': 0.05224842734238164}, {'name': 'request_tea', 'confidence': 0.050255186559431474}, {'name': 'ask_refreshments', 'confidence': 0.04790402495089106}, {'name': 'goodbye', 'confidence': 0.044566111991724715}, {'name': 'ask_tea', 'confidence': 0.03826858735731229}, {'name': 'thanks', 'confidence': 0.029488916301876618}], 'text': '点外卖'}}' is active
2020-09-28 20:39:54 DEBUG    rasa_sdk.forms  - Validating user input '{'intent': {'name': 'request_takeway', 'confidence': 0.16058830618379846}, 'entities': [{'entity': 'address', 'value': '南山区', 'start': 0, 'end': 3, 'confidence': None, 'extractor': 'MitieEntityExtractor'}], 'intent_ranking': [{'name': 'request_takeway', 'confidence': 0.16058830618379846}, {'name': 'request_tea', 'confidence': 0.1252117355150431}, {'name': 'request_constellation', 'confidence': 0.1100547403087655}, {'name': 'greet', 'confidence': 0.1025569462982005}, {'name': 'goodbye', 'confidence': 0.0842501319411562}, {'name': 'affirm', 'confidence': 0.0840473869402992}, {'name': 'thanks', 'confidence': 0.06594307641312021}, {'name': 'ask_tea', 'confidence': 0.05479332814598188}, {'name': 'deny', 'confidence': 0.03802939657193075}, {'name': 'ask_refreshments', 'confidence': 0.03743333849618349}], 'text': '南山区'}'
2020-09-28 20:39:54 DEBUG    rasa_sdk.forms  - Trying to extract requested slot 'address' ...
2020-09-28 20:39:54 DEBUG    rasa_sdk.forms  - Got mapping '{'type': 'from_entity', 'entity': 'address', 'intent': [], 'not_intent': [], 'role': None, 'group': None}'
2020-09-28 20:39:54 DEBUG    rasa_sdk.forms  - Successfully extracted '南山区' for requested slot 'address'
2020-09-28 20:39:54 DEBUG    rasa_sdk.forms  - Validating extracted slots: {'address': '南山区'}
2020-09-28 20:39:54 DEBUG    rasa_sdk.forms  - Request next slot 'phone_number'
2020-09-28 20:39:54 DEBUG    rasa_sdk.executor  - Finished running 'takeway_form'
2020-09-28 20:39:59 DEBUG    rasa_sdk.executor  - Received request to run 'takeway_form'
2020-09-28 20:39:59 DEBUG    rasa_sdk.forms  - The form '{'name': 'takeway_form', 'validate': True, 'rejected': False, 'trigger_message': {'intent': {'name': 'request_takeway', 'confidence': 0.3650815377324046}, 'entities': [], 'intent_ranking': [{'name': 'request_takeway', 'confidence': 0.3650815377324046}, {'name': 'request_refreshments', 'confidence': 0.1283786319709406}, {'name': 'affirm', 'confidence': 0.09685220818783706}, {'name': 'deny', 'confidence': 0.06193598647737689}, {'name': 'greet', 'confidence': 0.05224842734238164}, {'name': 'request_tea', 'confidence': 0.050255186559431474}, {'name': 'ask_refreshments', 'confidence': 0.04790402495089106}, {'name': 'goodbye', 'confidence': 0.044566111991724715}, {'name': 'ask_tea', 'confidence': 0.03826858735731229}, {'name': 'thanks', 'confidence': 0.029488916301876618}], 'text': '点外卖'}}' is active
2020-09-28 20:39:59 DEBUG    rasa_sdk.forms  - Validating user input '{'intent': {'name': 'request_constellation', 'confidence': 0.19744570345854212}, 'entities': [{'entity': 'phone_number', 'value': '1234567890', 'start': 0, 'end': 10, 'confidence': None, 'extractor': 'MitieEntityExtractor'}], 'intent_ranking': [{'name': 'request_constellation', 'confidence': 0.19744570345854212}, {'name': 'request_takeway', 'confidence': 0.17183242632436677}, {'name': 'request_refreshments', 'confidence': 0.1277095508803687}, {'name': 'deny', 'confidence': 0.07725571777541991}, {'name': 'thanks', 'confidence': 0.07392116485545658}, {'name': 'affirm', 'confidence': 0.06934356400757544}, {'name': 'request_tea', 'confidence': 0.06356318293445108}, {'name': 'whoareyou', 'confidence': 0.04146817893809367}, {'name': 'ask_tea', 'confidence': 0.033264424419380226}, {'name': 'whattodo', 'confidence': 0.03069654116379351}], 'text': '1234567890'}'
2020-09-28 20:39:59 DEBUG    rasa_sdk.forms  - Trying to extract requested slot 'phone_number' ...
2020-09-28 20:39:59 DEBUG    rasa_sdk.forms  - Got mapping '{'type': 'from_entity', 'entity': 'phone_number', 'intent': [], 'not_intent': [], 'role': None, 'group': None}'
2020-09-28 20:39:59 DEBUG    rasa_sdk.forms  - Successfully extracted '1234567890' for requested slot 'phone_number'
2020-09-28 20:39:59 DEBUG    rasa_sdk.forms  - Validating extracted slots: {'phone_number': '1234567890'}
2020-09-28 20:39:59 DEBUG    rasa_sdk.forms  - No slots left to request, all required slots are filled:
	refreshments: 蛋糕
	tea: 绿茶
	address: 南山区
	phone_number: 1234567890
2020-09-28 20:39:59 DEBUG    rasa_sdk.forms  - Submitting the form 'takeway_form'
2020-09-28 20:39:59 DEBUG    rasa_sdk.forms  - Deactivating the form 'takeway_form'
2020-09-28 20:39:59 DEBUG    rasa_sdk.executor  - Finished running 'takeway_form'

```

## 实现功能 介绍


### V3.0 外卖配送员 夕仔 【2020.09.28】

```s
Your input ->  点外卖 
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 1.050 seconds.
Prefix dict has been built successfully.
您好！很高兴为您服务，我们这边目前茶点可多了！有蛋糕、肠粉、还有好吃停不下来的糕点，请问你要哪一种呢？
Your input ->  蛋糕
您好！很高兴为您服务，我们这边目前茶可多了！有红茶、绿茶、普洱茶、铁观音、碧螺春、还有上好的龙井，请问你要哪一种呢？
Your input ->  绿茶
麻烦留个收货地址
Your input ->  南山区 
麻烦给我一个联系方式
Your input ->  1234567890
蛋糕和绿茶已经在制作中，麻烦十分钟后到南山区拿，并保证手机号1234567890畅通
```

### V2.0 星座占卜师 夕酱 【2020.09.26】

```s
Your input ->  查星座  
小星卜小夕来啦？你想查询什么星座？白羊座？金牛座？双子座？巨蟹座？狮子座？处女座？天秤座？天蝎座？射手座？摩羯座？水瓶座？
Your input ->  白羊座  
白羊座的运势：时间：3-21-4-19，特点：热情活力，最大特征：控制，介绍：白羊座有一种让人看见就觉得开心的感觉，因为总是看起来都是那么地热情、阳光、乐观、坚强，对朋友也慷慨大方，性格直来直往，就是有点小脾气。白羊男有大男人主义的性格，而白羊女就是女汉子的形象。
Your input ->  双子座  
双子座的运势：时间：5-21-6-21，特点：花心多变，最大特征：思想，介绍：双子座喜欢追求新鲜感，有点儿小聪明，就是耐心不够，往往做事都是三分钟热度，难以坚持，但是你的可爱性格会让很多人都喜欢跟你做朋友。双子男表面很花心，其实深情，而双子女就喜欢求新和求变。
Your input ->  帮我查一下巨蟹座的男生 
巨蟹座的运势：时间：6-22-7-22，特点：敏感柔情，最大特征：感觉，介绍：巨蟹座的情绪容易敏感，也缺乏安全感，容易对一件事情上心，做事情有坚持到底的毅力，为人重情重义，对朋友、家人都特别忠实，巨蟹男是一等一的好男人，顾家爱家人，巨蟹女充满母性光环，非常有爱心。
```

### V1.0 茶餐厅 店小二 小夕 【2020.09.25】

```s
Your input ->  点餐 
您好！很高兴为您服务，我们这边目前茶点可多了！有蛋糕、肠粉、还有好吃停不下来的糕点，请问你要哪一种呢？
Your input ->  肠粉
肠粉 马上为您送上
Your input ->  点茶
您好！很高兴为您服务，我们这边目前茶可多了！有红茶、绿茶、普洱茶、铁观音、碧螺春、还有上好的龙井，请问你要哪一种呢？
Your input ->  红茶
请问，你要热的还是少冰或者常温？
Your input ->  加冰
请问，你要加糖么？
Your input ->  少糖
加冰少糖的红茶 马上为您送上

Your input ->  这边有什么好吃的？  
您好！很高兴为您服务，我们这边目前茶点可多了！有蛋糕、肠粉、还有好吃停不下来的糕点，请问你要哪一种呢？

Your input ->  这边有什么茶呢？ 
您好！很高兴为您服务，我们这边目前茶可多了！有红茶、绿茶、普洱茶、铁观音、碧螺春、还有上好的龙井，请问你要哪一种呢？
Your input ->  这边有什么好吃的？  
您好！很高兴为您服务，我们这边目前茶点可多了！有蛋糕、肠粉、还有好吃停不下来的糕点，请问你要哪一种呢？

```

