import re
from validate_docbr import CPF

def valid_cpf(cpf_number):
    """"""
    return CPF().validate(cpf_number)

def valid_name(name):
    """"""
    return name.isalpha()

def valid_rg(rg_number):
    """"""
    return len(rg_number) == 9

def valid_cell_phone(phone_number):
    """"""
    return re.findall(r'[0-9]{2} [0-9]{5}-[0-9]{4}', phone_number)
