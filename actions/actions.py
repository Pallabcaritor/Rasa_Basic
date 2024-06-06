from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import random
import psycopg2

connection = psycopg2.connect(database="risl", user="root", password="root", host="localhost", port=5432)
cursor = connection.cursor()


#cursor.execute("SELECT * from portal.portal_users;")

def my_random(d):
    ''' Generates a random number with d digits '''
    return random.randint(int('1'+'0'*(d-1)), int('9'*d))

class ValidateDetailForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_details_form"

    def validate_applicant_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `applicant_name` value."""

        # If the name is super short, it might be wrong.
        name = slot_value
        if len(name) == 0:
            dispatcher.utter_message(text="Name cant be blank")
            return {"applicant_name": None}
        elif len(name) < 3:
            dispatcher.utter_message(text="That's a very short name. We fear a typo")
            return {"applicant_name": None}
        return {"applicant_name": name}
        

    def validate_father_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `father_name` value."""

        # If the name is super short, it might be wrong.
        name = slot_value
        if len(name) == 0:
            dispatcher.utter_message(text="Father's name can't be blank")
            return {"father_name": None}
        
        elif len(name) < 3:
            dispatcher.utter_message(text="That's a very short name. We fear a typo. Restarting!")
            return {"father_name": None}
        return {"father_name": name}
    
    def validate_connection_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `connection_type` value."""

        name = slot_value
        if len(name) == 0:
            dispatcher.utter_message(text="Connection Type can't be blank")
            return {"connection_type": None}
        if name.upper() not in ['DOMESTIC','INDUSTRIAL','COMMERCIAL']:
            dispatcher.utter_message(text="Please type properly from the mentioned option.")
            return {"connection_type": None}
        return {"connection_type": name}
    
    def validate_connection_load(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `connection_load` value."""

        name = slot_value
        if len(name) == 0:
            dispatcher.utter_message(text="Connection Load can't be blank")
            return {"connection_load": None}
        elif name.upper() not in ['2KVA','5KVA','MORE']:
            dispatcher.utter_message(text="Please type properly from the mentioned option.")
            return {"connection_load": None}
        return {"connection_load": name}
    
    def validate_contact_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `contact_number` value."""

        name = slot_value
        if len(name) == 0:
            dispatcher.utter_message(text="Contact Number can't be blank")
            return {"contact_number": None}
        elif len(name) != 10:
            dispatcher.utter_message(text="Please type your 10 digit Indian mobile number.")
            return {"contact_number": None}
        return {"contact_number": name}
    
    def validate_permanent_address(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `permanent_address` value."""

        name = slot_value
        if len(name) == 0:
            dispatcher.utter_message(text="That must've been a typo.")
            return {"permanent_address": None}
        elif len(name) < 3:
            dispatcher.utter_message(text="Your address length must be more than 3 words.")
            return {"permanent_address": None}
        return {"permanent_address": name}
    
    def validate_current_address(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `current_address` value."""

        name = slot_value
        if len(name) == 0:
            dispatcher.utter_message(text="This can't be blank")
            return {"current_address": None}
        elif len(name) < 3:
            dispatcher.utter_message(text="Your address length must be more than 3 words.")
            return {"current_address": None}
        return {"current_address": name}
    
    def validate_connection_purpose(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `connection_purpose` value."""

        name = slot_value
        if len(name) == 0:
            dispatcher.utter_message(text="This cant be blank")
            return {"connection_purpose": None}
        elif len(name) < 6:
            dispatcher.utter_message(text="Your connection purpose must have 6 minimum words.")
            return {"connection_purpose": None}
        application_no= 'RJEL' + str(my_random(8))
        
        return {"connection_purpose": name,"application_number": application_no}
    
    def run(
        self,
        #slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        print("_____________Slotted values_____________")
        slot_one = tracker.get_slot("connection_purpose")
        print("--------------------------------",slot_one)
        return []