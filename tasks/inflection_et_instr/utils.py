import datasets

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
      # modifies the contents of a single
      # document in our dataset.
      #doc["answer"] = "ABCDEFGHIJKLMNOPQ".index(doc["answer"])
      return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object

def test(items):
    """
    # passthrough for efficiency
    """
    print(items)
    return items
  
def test_agg(items):
    return 0.77
