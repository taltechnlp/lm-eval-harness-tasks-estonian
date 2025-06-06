from functools import partial


def convert_choice(choice):
    return choice[0].lower() + choice[1:]


def doc_to_text(doc, connector):
    # Drop the period
    conn = connector[doc["question"]]
    return doc["premise"].strip()[:-1] + f" {conn}"


def doc_to_choice(doc):
    return [convert_choice(doc["choice1"]), convert_choice(doc["choice2"])]


doc_to_text_et = partial(
    doc_to_text,
    connector={
        "cause": "sest",
        "effect": "seetõttu",
    },
)