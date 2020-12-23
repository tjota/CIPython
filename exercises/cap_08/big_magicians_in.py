magicians = ['Mr. M', 'Angel', 'Julius Dien']

def show_magicians(magicians_list):
    """Exibe mágicos de uma lista"""
    while magicians_list:
        magician = magicians_list.pop()
        print(magician + " o Grande!")


show_magicians(magicians[:])
print(magicians)