guests = ['Madona', 'Raul Seixas', 'Bita']

print("Olá " + guests[0] + ", você é meu convidado!")
print("Olá " + guests[1] + ", você é meu convidado!")
print("Olá " + guests[2] + ", você é meu convidado!\n")

print("O convidado " + guests.pop(0) + " não poderá comparecer ao evento.\n")

guests.insert(0, 'Peralta')

print("Olá " + guests[0] + ", você é meu convidado!")
print("Olá " + guests[1] + ", você é meu convidado!")
print("Olá " + guests[2] + ", você é meu convidado!\n")

print("Consegui uma mesa de jantar maior!\n")

guests.insert(0, 'Rosa Diaz')
guests.insert(2, 'Terry')
guests.append('Linete')

print("Olá " + guests[0] + ", você é meu convidado!")
print("Olá " + guests[1] + ", você é meu convidado!")
print("Olá " + guests[2] + ", você é meu convidado!")
print("Olá " + guests[3] + ", você é meu convidado!")
print("Olá " + guests[4] + ", você é meu convidado!")
print("Olá " + guests[5] + ", você é meu convidado!")
