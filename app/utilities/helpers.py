from collections import OrderedDict
from wtforms import StringField, Form
import json
# from app.setup import log


# ###################################### UTILITY FUNCTIONS ###########################################
# Create class for forms dynamically
def create_form_class(iterable):
    var_dict = {}
    for variable_name in iterable:
        print("adding {} to dict".format(variable_name))
        var_dict[variable_name] = StringField("{}".format(variable_name))
    class_output = type("SearchSelect", (Form,), var_dict)
    # At this point we have a class that analogous to SearchForm
    return class_output


# To clean inputs, we need to create a mutable dictionary
def create_new_dict(url_paramaters):
    mutable_dict = {}
    for key in url_paramaters.keys():
        mutable_dict[key] = url_paramaters[key]
    return mutable_dict


# Remove arbitary spaces from the inputs
def clean_search_parameters(url_parameters):
    for key in url_parameters.keys():
        url_parameters[key] = url_parameters[key].replace(" ", "")
    return url_parameters


# Build the URI to connect to the business layer. The strings that are appended to the
# urlConnect string are search parameters, of the form PARAMETER=VALUE;
def build_uri(url_parameters):
    """
    :param url_parameters: dictionary
    :return: String
    Takes a dict and constructs the URL to the business layer
    """
    url_connect = ""
    for keys in url_parameters.keys():
        if url_parameters[keys] == "":
            continue
        url_connect += "{}={};".format(keys, url_parameters[keys])
    url_connect = url_connect[:-1]
    return url_connect


def build_uri_2(url_parameters):
    """
    :param url_parameters: dictionary
    :return: String
    Takes a dict and constructs the URL to the business layer
    """
    url_connect = ""
    for keys in url_parameters.keys():
        if url_parameters[keys] == "":
            continue
        url_connect += "{}={}&".format(keys, url_parameters[keys])
    url_connect = url_connect[:-1]
    return url_connect


# Takes a string which should be either True or False and returns the bool value or ValueError
def str_to_bool(string_to_convert):
    """

    :param string_to_convert: String
    :return: boolean
    Takes a string which should be either True or False and returns the bool value or ValueError
    """
    if string_to_convert == "True":
        return True
    if string_to_convert == "False":
        return False
    raise ValueError


def decompose_data(data: dict) -> dict:
    """
    :param data: Dictionary of the form {"qCode:Number|inst:Number":"Response"}
    :return: Dictionary of the form {Updated Responses: {qCode: {instance: Responce}}}
    """

    data_atoms = []
    # Create tuple to hold data atoms
    for key in sorted(data.keys()):
        if key == "action":
            continue
        # data_atoms.append((hold_data[0], hold_data[1], data[key]))

        data_atoms.append({key: data[key]})

    print("Output data: " + str(data_atoms))
    return {"Updated Responses": data_atoms}


def build_json(data):
    data_atoms = []
    data = OrderedDict(data)
    # print("build_json data: {}".format(data))
    for key in data.keys():
        data_atoms.append(
            {form_key: data[key].get(form_key) for form_key in data[key].keys()}
        )
        data_atoms[-1]["questionCode"] = key
    return data_atoms


def get_user():
    # In the future this will get a cookie from the browser
    return "fisdba"


def build_links(links_list, name_of_link):
    """
    :param links_list: List, name_of_link: String
    :return: String
    Takes a list of links which and returns the correct one depending on parameter
    """
    extracted_link = ""
    for link in links_list:
        if link["rel"] == name_of_link:
            extracted_link = link["href"]
    return extracted_link


def find_nodes(data: dict, node_to_find: str) -> (dict, list, str):
    if node_to_find in data:
        return data[node_to_find]
    for att in data:
        if att not in (node_to_find) and isinstance(data[att], dict):
            item = find_nodes(data[att], node_to_find)
            if item is not None:
                return item
    raise KeyError(f'No node with name "{node_to_find}" found')

def json_validator(data, log):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        log.info("invalid json: %s" % error)
        return False


# This function reordes the questions based off the displayorder value 
def question_order(response_and_validations, log):
    try:
        questions = response_and_validations["form_validation_outputs"]
        sorted_questions = (sorted(questions, key = lambda i: i['displayorder']))
        sorted_response_and_validations = {'form_validation_outputs': sorted_questions}
        return sorted_response_and_validations

    except KeyError as key_error:
        log.error("Data missing displayorder" + str(key_error))

    except TypeError as type_error:
        log.error("Error with data type converting to JSON " + str(type_error))

    except Exception as error:
        log.error("Error: " + error)
