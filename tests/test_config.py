from app import form_response
from src.data.load_data import read_params

class  NotANumber(Exception):
    def __init__(self, message="Values entered are not Numerical"):
        self.message = message
        super().__init__(self.message)

input_data = {
    "incorrect_values": 
    {"number_vmail_messages": 3, 
    "total_day_calls": 4, 
    "total_eve_minutes": 'as', 
    "total_eve_charge": 12, 
    "total_intl_minutes": 1, 
    "number_customer_service_calls": 'ab', 
    },

    "correct_values": 
    {"number_vmail_messages": 3, 
    "total_day_calls": 4, 
    "total_eve_minutes": 2, 
    "total_eve_charge": 12, 
    "total_intl_minutes": 1, 
    "number_customer_service_calls": 4, 
    }
}


path_data = {
    "incorrect_path": { "config_path":  "./par.yaml"},
    "correct_path": {"config_path": "./params.yaml"}
}

def test_form_response_incorrect_values(data=input_data["incorrect_values"]):
    res=form_response(data)
    assert res == NotANumber().message

def test_load_params_incorrect_path(data = path_data["incorrect_path"]):
    res = read_params(data["config_path"])
    assert res == "Error loading file"
