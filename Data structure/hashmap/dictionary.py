glossary = {"BDFL": "Benevolent Dictator For Life"}
glossary["GIL"] = "Global Interpreter Lock" 
glossary['BDFL'] = "Guido van Rossum"

del glossary['GIL']

print(glossary)
print(glossary['BDFL'])