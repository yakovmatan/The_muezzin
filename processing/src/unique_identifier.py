#Function to generate a unique identifier
def get_unique_identifier(documents_json: dict, num_of_doc: str):
    unique_identifier = num_of_doc #Initialization with a unique number
    for field in documents_json:
        unique_identifier += documents_json[field][0] #First letter in each field

    return unique_identifier