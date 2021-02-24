class CreditCard:
    # Atributo de clase
    TASA_SOBREGIRO = 0.05

    # No definimos directamente los atributos.
    # Los constructores se definen de la siguiente manera (INICIALIZADOR)
    def __init__(self):
        #Atributos de clase
        self.fecha_emision = None
        self.fecha_vencimiento = None
        self.__cvv = '1234'
        self.numero_cuenta = None
        self.cliente = None
        # Si es Visa, MasterCard, AMEX, etc.
        self.emisor = None
        self.banco = None
        self.__limite = 10000
        self.__saldo = 0.0

        # Variable local
        monto = 0

    def get_cvv(self):
        return self.__cvv

    def set_saldo(self, saldo:float) -> None:
        if (self.__saldo + saldo <= self.__limite):
            self.__saldo += saldo

    def get_saldo(self) -> float:
        return self.__saldo

    def __str__(self):
        return "Banco: " + self.banco + "\nEmisor: " + self.emisor + "\nCliente: " + self.cliente

# Creacion de un objeto
cc = CreditCard()
cc.banco = 'BAC'
cc.emisor = 'Visa'
cc.cliente = 'Armando Rincon'
print(cc.get_cvv())
cc.set_saldo(2500)
print(cc.get_saldo())
cc.set_saldo(66000)
print(cc.get_saldo())
# Aqui llama al metodo __str__
print(cc)
# Impresion del diccionario con los atributos del objeto
print(cc.__dict__)

# Manipulacion del atributo de clase (estatico)
print('Tasa antes: ', CreditCard.TASA_SOBREGIRO)
CreditCard.TASA_SOBREGIRO = 0.07

print('Tasa despues: ', CreditCard.TASA_SOBREGIRO)
print(cc.TASA_SOBREGIRO)

cc1 = CreditCard()
print(cc1.TASA_SOBREGIRO)