import datasets

from Levenshtein import distance as levv

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
      # modifies the contents of a single
      # document in our dataset.
      #doc["answer"] = "ABCDEFGHIJKLMNOPQ".index(doc["answer"])
      return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object

def lev(items):
    return items

def lev_agg(items):
    goodness = 0
    for item in items:
      dist = levv(item[0], item[1])
      goodness += 1 / (1 + dist)
    return goodness / len(items)

def raw_lev(items):
    return items

def raw_lev_agg(items):
    total_lev = 0
    for item in items:
      dist = levv(item[0], item[1])
      total_lev += dist
    return total_lev / len(items)

def precise(items):
    return items

def precise_agg(items):
    goodness = 0
    for item in items:
      if item[0] == item[1]:
        goodness += 1
    return goodness / len(items)

