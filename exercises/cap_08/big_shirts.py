def make_shirt(length='G', text_stamp='Eu amo Python!'):
    """ Exibe informações de tamanho e frase da camiseta. """
    print("O tamanho da camiseta é " + length.title() + ".\n")
    print("A frase da camiseta é a seguinte:\n" + text_stamp.title())
    print("-" * 30)


make_shirt()
make_shirt(length='M')
make_shirt('P', 'Rosas são vermelhas e o resto\nnão preciso dizer.\n')