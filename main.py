from pyscript import display, document
# Variables
Symbols = ["H", "He", "C", "N", "O", "F", "Ne", "P", "S", "Cl", "Ar", "Se", "Br", "Kr", "I", "Xe", "Rn",     ]
ElementName = ["Hydrogen", 'Helium', "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Phosphorus", "Sulfur", "Chlorine," "Argon", "Selenium", "Bromine", "Krypton", "Iodine", "Xenon", "Radon"]
# Function
def get_element(e):
    selected_Symbols = document.getElementById("Elements").value

    index = Symbols.index(selected_Symbols)
    selected_ElementName = ElementName[index]


    document.getElementById("result").innerText = selected_ElementName

