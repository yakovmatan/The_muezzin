import hashlib


# Function to generate a unique identifier
def get_unique_identifier(documents_json: dict, num_of_doc: str):
    unique_identifier = num_of_doc  # Initialization with a unique number
    unique_identifier += ''.join([str(val) for val in documents_json.values()])
    return hashlib.md5(unique_identifier.encode('utf-8')).hexdigest()
