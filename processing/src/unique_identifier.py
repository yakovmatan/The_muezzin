def get_unique_identifier(documents_json: dict, num_of_doc: str):
    unique_identifier = num_of_doc
    for field in documents_json:
        unique_identifier += documents_json[field][0]

    return unique_identifier