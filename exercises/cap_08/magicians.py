magicians = ['Mr. M', 'Angel', 'Julius Dien']

def show_magicians(magicians_list):
    """Exibe mágicos de uma lista"""
    while magicians_list:
        print(magicians_list.pop())


show_magicians(magicians)