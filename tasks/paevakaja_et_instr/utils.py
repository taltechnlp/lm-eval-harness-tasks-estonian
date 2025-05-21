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

def speakers(items):
    print(items)
    return items

def speakers_agg(items):
    goodness = 0
    print(items)
    for item in items:
        print([item[0]])
        print([item[1]])
        print("---------------------")
    return 0.78

def process_results_speakers(a, b):
    extracted = []
    cache = ""
    state = "out"
    string_char = None
    for ch in b[0]:
        if state == "out":
            if ch == "[":
                state = "in"
            continue
        if state == "in":
            if ch == '"' or ch == "'":
                state = "in_string"
                string_char = ch
            elif ch == "]":
                state = "out"
                break
            continue
        if state == "in_string":
            if ch == string_char:
                extracted.append(cache)
                cache = ""
                state = "in"
            else:
                cache += ch
    if cache:
        extracted.append(cache)
    if not extracted:
        extracted = list(set(b[0].split("\n")[0].strip(" .").split(", ")))
    print("Model output:")
    print(b)
    print("Extracted list:")
    print(extracted)
    print("Expected output:")
    print(a["speakers"])
    print("-----------------------------------")
    correct = list(set(a["speakers"]))
    guesses = list(set(extracted))
    tp_count = len(set(correct).intersection(set(guesses)))
    return {
        "precision": tp_count / max(len(guesses), 1),
        "recall": tp_count / max(len(correct), 1),
    }
