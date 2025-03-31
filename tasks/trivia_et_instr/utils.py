import datasets

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
      answers = doc["vastusevariandid"]
      letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      doc["vastus"] = letters[int(doc["vastus"])]
      doc["vastusevariandid"] = "\n".join([f"{letters[i]}: {x}" for i, x in enumerate(answers)])
      return doc

    return dataset.map(_helper)