import datasets

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
      answers = doc["vastusevariandid"]
      letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      doc["vastus"] = letters[int(doc["vastus"])]
      doc["vastusevariandid"] = "\n".join([f"{letters[i]}: {x}" for i, x in enumerate(answers)])

      # A, B, C või D
      vastusevariante = ", ".join([letters[i] for i in range(len(answers) - 1)]) + " või " + letters[len(answers) - 1]
      
      doc["tekst"] = f"Sa oled ekspert ning vastad küsimustele korrektselt. Sulle antakse küsimus koos vastusevariantidega. Anna vastus kujul: “Vastus: X”, kus X on kas {vastusevariante}. Ära kirjuta midagi muud! Vasta eesti keeles!\nKüsimus: {doc['küsimus']}\nVastusevariandid:\n{doc['vastusevariandid']}"
      return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object

"""
|              Tasks              |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|---------------------------------|------:|------|-----:|-----------|---|-----:|---|-----:|
|exam_et_instr_ajalugu            |      1|nimi  |     0|exact_match|↑  |0.5594|±  |0.0308|
|exam_et_instr_bioloogia          |      1|nimi  |     0|exact_match|↑  |0.3671|±  |0.0336|
|exam_et_instr_eesti_keel_gymn    |      1|nimi  |     0|exact_match|↑  |0.2398|±  |0.0273|
|exam_et_instr_eesti_keel_pohikool|      1|nimi  |     0|exact_match|↑  |0.3151|±  |0.0302|
|exam_et_instr_fyysika            |      1|nimi  |     0|exact_match|↑  |0.3519|±  |0.0462|
|exam_et_instr_geograafia         |      1|nimi  |     0|exact_match|↑  |0.5135|±  |0.0477|
|exam_et_instr_keemia             |      1|nimi  |     0|exact_match|↑  |0.3759|±  |0.0422|
|exam_et_instr_yhiskond           |      1|nimi  |     0|exact_match|↑  |0.5000|±  |0.0284|

"""
