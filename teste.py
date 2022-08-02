from Models.cliente import Cliente
from Models.conta import Conta

carlos: Cliente = Cliente('Carlos André', 'carlosandre91@hotmail.com', '123.456.789-01', '11/01/1991')
gilmara: Cliente = Cliente('Gilmara', 'gilmara_soares@hotmail.com', '123.456.987-12', '12/11/1989')

#print(carlos)
#print(gilmara)

contaf: Conta = Conta(carlos)
contaa: Conta = Conta(gilmara)

#print(contaa)
#print(contaf)