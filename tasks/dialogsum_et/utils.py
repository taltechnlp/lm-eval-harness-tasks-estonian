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


def rouge1(items):
    """
    # passthrough for efficiency
    """
    return items

def rouge2(items):
    """
    # passthrough for efficiency
    """
    return items

def rougeL(items):
    """
    # passthrough for efficiency
    """
    return items


def average_len(items):
    """
    # passthrough for efficiency
    """
    return items

def rouge1_agg(items):
    return rouge_agg(items, "1")

def rouge2_agg(items):
    return rouge_agg(items, "2")

def rougeL_agg(items):
    return rouge_agg(items, "L")

def rouge_agg(items, suffix):
    """
    Higher is better
    """
    
    refs = list(zip(*items))[0]
    refs = [[clean_text(ref)] for ref in refs]
    # print("refs", refs)
    preds = [clean_text(x) for x in list(zip(*items))[1]]
    # print("preds", preds)
    rouge_scorer = evaluate.load("rouge")
    return rouge_scorer.compute(predictions=preds, references=refs)[f"rouge{suffix}"]


def average_len_agg(items):
    """
    Higher is better
    """

    preds = [clean_text(x) for x in list(zip(*items))[1]]

    return sum(len(x.split()) for x in preds) / len(preds)
