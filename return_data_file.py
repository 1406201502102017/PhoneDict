from choice_file import choice_number_file

def data_file():
    nf = choice_number_file()
    with open(f'files/contacts_{nf}.txt', 'r', encoding='utf-8') as file:   # db/data_{nf}.txt
        data = file.readlines()
    return data, nf