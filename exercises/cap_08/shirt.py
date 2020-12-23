def make_shirt(length, text_stamp):
    """ Exibe informações de tamanho e frase da camiseta. """
    print("O tamanho da camiseta é " + length.title() + ".\n")
    print("A frase da camiseta é a seguinte:\n" + text_stamp.title())


make_shirt('M', 'Rosas são vermelhas e o resto\nnão preciso dizer.\n')
make_shirt(length='G', text_stamp='Olá, mundo!')