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