
import json


def save_dict(fileName, dictName):
  """ writes dict: dictName to file: fileName """
  with open(fileName, 'w') as outfile:
    outfile.write(json.dumps(dictName,
                    indent=4, sort_keys=True,
                    separators=(',', ': '), ensure_ascii=False))