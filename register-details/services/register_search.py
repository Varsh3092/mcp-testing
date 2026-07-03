import re


def find_register_content(
    document_text: str,
    register_name: str
):
    """
    Find register section from PDF text.
    """

    index = document_text.lower().find(
        register_name.lower()
    )

    if index == -1:
        return None

    start = max(0, index - 500)

    end = min(
        len(document_text),
        index + 2000
    )

    return document_text[start:end]
