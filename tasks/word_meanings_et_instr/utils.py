import datasets
import random

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
      # modifies the contents of a single
      # document in our dataset.
      #doc["answer"] = "ABCDEFGHIJKLMNOPQ".index(doc["answer"])
      #doc["definition"] = random.choice(doc["definition"])
      return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object
