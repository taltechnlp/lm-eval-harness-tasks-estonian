import string

import evaluate


def clean_text(text: str) -> str:
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove newlines and multiple spaces
    text = text.replace("\n", " ").strip()
    text = " ".join(text.split()).strip()

    # lowercase
    text = text.lower()

    return text


