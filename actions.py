from typing import Dict, Text, Any, List

from base import *

from rasa_sdk import Tracker, Action
from rasa_sdk.events import UserUtteranceReverted, Restarted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from requests import (
    ConnectionError,
    HTTPError,
    TooManyRedirects,
    Timeout
)
support_search = ["消费", "流量"]

def extract_item(item):
    """
    check if item supported, this func just for lack of train data.
    :param item: item in track, eg: "流量"、"查流量"
    :return:
    """
    if item is None:
        return None
    for name in support_search:
        if name in item:
            return name
    return None

# 继承了 rasa 的 Action 类
class ActionSearchConsume(Action):
    # name() 返回 action name
    def name(self):
        return 'action_search_consume'
    # run()：
    # - dispatcher参数，机器人可能和很多用户对话，要dispatch 一下；
    # - domain参数：action 集合
    def run(self, dispatcher, tracker, domain):
        item = tracker.get_slot("item")
        item = extract_item(item)
        if item is None:
            dispatcher.utter_message("您好，我现在只会查话费和流量")
            dispatcher.utter_message("你可以这样问我：“帮我查话费”")
            return []
        userMess = tracker.latest_message
        print(f"userMess: {userMess}")
        events = tracker.events
        print(f"events: {events}")
        followup_action = tracker.followup_action
        print(f"followup_action: {followup_action}")
        slots = tracker.slots
        print(f"slots: {slots}")
        active_form = tracker.active_form
        print(f"active_form: {active_form}")
        latest_action_name = tracker.latest_action_name
        print(f"latest_action_name: {latest_action_name}")
        time = tracker.get_slot("time")
        if time is None:
            dispatcher.utter_message("您想查询哪个月的消费？")
            return []
        # query database here using item and time as key. but you may normalize time format first.
        dispatcher.utter_message("好，请稍等")
        if item == "流量":
            dispatcher.utter_message("您好，您{}共使用{}二百八十兆，剩余三十兆。".format(time, item))
        else:
            dispatcher.utter_message("您好，您{}共消费二十八元。".format(time))
        return []

# action tea_form
class TeaForm(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "tea_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["tea", "temperature", "sugar"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        tea = tracker.get_slot('tea')
        temperature = tracker.get_slot('temperature')
        sugar = tracker.get_slot('sugar')
        userMess = tracker.latest_message
        print(f"用户输入：{userMess}")
        dispatcher.utter_message("{}{}的{} 马上为您送上".format(temperature,sugar,tea))
        return [Restarted()]

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
        userMess = tracker.latest_message
        print(f"用户输入：{userMess}")
        dispatcher.utter_message("{}和{}已经在制作中，麻烦十分钟后到{}拿，并保证手机号{}畅通".format(refreshments,tea,address,phone_number))
        return []
            
# action tea_form
class RefreshmentsForm(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "refreshments_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["refreshments"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        refreshments = tracker.get_slot('refreshments')
        userMess = tracker.latest_message
        print(f"用户输入：{userMess}")
        dispatcher.utter_message("{} 马上为您送上".format(refreshments))
        return [Restarted()]

# action tea_form
class ConstellationForm(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "constellation_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["constellation"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        constellation = tracker.get_slot('constellation')
        mess = "来自遥远的星星你，是否也会怀念回家的路？"
        userMess = tracker.latest_message
        print(f"用户输入：{userMess}")
        if constellation in constellationDict:
            mess = f"{constellation}的运势：时间：{constellationDict[constellation]['startTime']}-{constellationDict[constellation]['endTime']}，特点：{constellationDict[constellation]['特点']}，最大特征：{constellationDict[constellation]['最大特征']}，介绍：{constellationDict[constellation]['介绍']}"
        dispatcher.utter_message(mess)
        return [Restarted()]

# action_default_fallback
class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self):
        return 'action_default_fallback'

    def run(self, dispatcher, tracker, domain):
        userMess = tracker.latest_message
        print(f"用户输入：{userMess}")
        dispatcher.utter_template('utter_default', tracker, silent_fail=True)
        return [UserUtteranceReverted()]