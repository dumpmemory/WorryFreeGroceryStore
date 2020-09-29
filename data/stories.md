## Generated Story 5914322956106259965
* greet
    - utter_answer_greet
* request_search{"item": "的情况"}
    - slot{"item": "消费"}
    - slot{"item": "的情况"}
    - action_search_consume
* request_search{"item": "消费"}
    - slot{"item": "消费"}
    - action_search_consume
* inform_time{"time": "上个月"}
    - slot{"time": "上个月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_answer_goodbye
    - export

## Generated Story 1131691423643832225
* request_search{"item": "消费"}
    - slot{"item": "消费"}
    - utter_ask_time
* inform_time{"time": "十月份"}
    - slot{"time": "十月份"}
    - action_search_consume
    - utter_ask_morehelp
* thanks
    - utter_answer_thanks
    - export

## Generated Story -6529474466838218787
* greet
    - utter_answer_greet
* request_search{"item": "消费"}
    - slot{"item": "消费"}
    - utter_ask_time
* inform_time{"time": "上月"}
    - slot{"time": "上月"}
    - action_search_consume
    - utter_ask_morehelp
* request_search{"time": "还", "item": "消费"}
    - slot{"time": "还"}
    - slot{"item": "消费"}
    - utter_ask_morehelp
    - utter_ask_time
* inform_time{"time": "十月"}
    - slot{"time": "十月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_answer_goodbye
* request_search{"time": "还", "item": "流量"}
    - slot{"time": "还"}
    - slot{"item": "流量"}
    - utter_ask_time
* inform_time{"time": "八月"}
    - slot{"time": "八月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_answer_goodbye
    - utter_answer_thanks
* greet
    - utter_answer_greet
* goodbye
    - utter_answer_goodbye
    - export

## Generated Story 7046379915386561772
* request_search{"item": "流量"}
    - slot{"item": "流量"}
    - utter_ask_time
* inform_time{"time": "上个月"}
    - slot{"time": "上个月"}
    - action_search_consume
    - utter_ask_morehelp
* request_search{"item": "消费"}
    - slot{"item": "消费"}
    - utter_ask_time
* inform_time{"time": "上个月"}
    - slot{"time": "上个月"}
    - action_search_consume
    - utter_ask_morehelp
* request_search{"time": "还", "item": "号码"}
    - slot{"time": "还"}
    - slot{"item": "消费"}
    - slot{"item": "号码"}
    - utter_ask_time
* inform_time{"time": "上月"}
    - slot{"time": "上月"}
    - action_search_consume
    - utter_ask_morehelp
* affirm
    - utter_ask_morehelp
* deny
    - utter_answer_goodbye
    - export

## Generated Story 3510639764351215934
* greet
    - utter_answer_greet
* request_search{"item": "东西"}
    - slot{"item": "东西"}
    - utter_ask_time
* inform_time{"time": "三月"}
    - slot{"time": "三月"}
    - action_search_consume
* request_search{"item": "流量"}
    - slot{"item": "流量"}
    - utter_ask_time
* inform_time{"time": "四月"}
    - slot{"time": "四月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_answer_goodbye
    - export

## Generated Story 3510639764351215934
* greet
    - utter_answer_greet
* request_search{"item": "东西"}
    - slot{"item": "东西"}
    - utter_ask_time
* inform_time{"time": "三月"}
    - slot{"time": "三月"}
    - action_search_consume
* request_search{"item": "流量"}
    - slot{"item": "流量"}
    - utter_ask_time
* inform_time{"time": "四月"}
    - slot{"time": "四月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_answer_goodbye
    - export

## Generated Story 1131691423643832225
* request_search{"item": "消费"}
    - slot{"item": "消费"}
    - utter_ask_time
* inform_time{"time": "十月份"}
    - slot{"time": "十月份"}
    - action_search_consume
    - utter_ask_morehelp
* thanks
    - utter_answer_thanks
    - export

## Generated Story -6529474466838218787
* greet
    - utter_answer_greet
* request_search{"item": "消费"}
    - slot{"item": "消费"}
    - utter_ask_time
* inform_time{"time": "上月"}
    - slot{"time": "上月"}
    - action_search_consume
    - utter_ask_morehelp
* request_search{"time": "还", "item": "消费"}
    - slot{"time": "还"}
    - slot{"item": "消费"}
    - utter_ask_morehelp
    - utter_ask_time
* inform_time{"time": "十月"}
    - slot{"time": "十月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_answer_goodbye
* request_search{"time": "还", "item": "流量"}
    - slot{"time": "还"}
    - slot{"item": "流量"}
    - utter_ask_time
* inform_time{"time": "八月"}
    - slot{"time": "八月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_answer_goodbye
    - utter_answer_thanks
* greet
    - utter_answer_greet
* goodbye
    - utter_answer_goodbye
    - export

## say joke
* ask_joke
    - utter_ask_joke

## ask tea
* ask_tea
    - utter_ask_tea

## ask refreshments
* ask_refreshments
    - utter_ask_refreshments

## request tea
* request_tea
    - tea_form
    - form{"name": "tea_form"}
    - form{"name": null}

## request refreshments
* request_refreshments
    - refreshments_form
    - form{"name": "refreshments_form"}
    - form{"name": null}

## request constellation
* request_constellation
    - constellation_form
    - form{"name": "constellation_form"}
    - form{"name": null}

## request takeway
* request_takeway
    - takeway_form
    - form{"name": "takeway_form"}

## greet
* greet
    - utter_answer_greet

## say affirm  with greet
* greet
    - utter_answer_greet
* affirm
    - utter_answer_affirm
    
## say affirm 
* affirm
    - utter_answer_affirm
    
## say no with greet
* greet
    - utter_answer_greet
* deny
    - utter_answer_deny
    
## say no 
* deny
    - utter_answer_deny


## say goodbye
* goodbye
    - utter_answer_goodbye
    
## thanks with greet
* greet
    - utter_answer_greet
* thanks
    - utter_answer_thanks
    
## thanks
* thanks
    - utter_answer_thanks
    
## who are you with greet
* greet
    - utter_answer_greet
* whoareyou
    - utter_answer_whoareyou
    
## who are you
* whoareyou
    - utter_answer_whoareyou
    
## who are you with greet
* greet
    - utter_answer_greet
* whoareyou
    - utter_answer_whoareyou
    
## what to do
* whattodo
    - utter_answer_whattodo
    
## what to do with greet
* greet
    - utter_answer_greet
* whattodo
    - utter_answer_whattodo

