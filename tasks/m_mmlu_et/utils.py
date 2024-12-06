import datasets

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
        # modifies the contents of a single
        # document in our dataset.
        doc["choices"] = [doc["option_a"], doc["option_b"], doc["option_c"], doc["option_d"]]
        doc["answer"] = "ABCD".index(doc["answer"])
        return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object


def accuracy_by_categories(dataset: datasets.Dataset):
    file = open("test", "w")
    file.write(dataset)
    file.close()
    print(dataset)