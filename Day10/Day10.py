# Docstrings
def format_name(f_name, l_name):
    """Take a first and last name and
    format it into a Title String"""
    if l_name == "" or f_name == "":
        return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

format_name()
