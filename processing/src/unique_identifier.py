def get_unique_identifier(documents_json: dict, num_of_doc):
    unique_identifier = str(num_of_doc)
    for field in documents_json:
        unique_identifier += documents_json[field][0]

    return unique_identifier