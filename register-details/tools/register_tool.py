from services.pdf_reader import read_pdf

from services.register_search import (
    find_register_content
)

from services.llm_service import (
    explain_register
)


def get_register_details(
    pdf_path: str,
    register_name: str
):
    pdf_text = read_pdf(pdf_path)

    register_text = find_register_content(
        pdf_text,
        register_name
    )

    if not register_text:
        return f"{register_name} not found."

    result = explain_register(
        register_text
    )

    return result
