from typing import Dict, Text, Any, List

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
        dispatcher.utter_message("{}{}的{} 马上为您送上".format(temperature,sugar,tea))
        return [Restarted()]
            
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
        dispatcher.utter_message("{} 马上为您送上".format(refreshments))
        return [Restarted()]

# action_default_fallback
class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self):
        return 'action_default_fallback'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_default', tracker, silent_fail=True)
        return [UserUtteranceReverted()]