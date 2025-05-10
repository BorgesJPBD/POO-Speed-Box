from datetime import date

class Pedido:
    def __init__(self, id_pedido, status, data_criacao, entrega_prevista, rota, transporte, valor_total, avaliacao_cliente, comentarios):
    
        self.id_pedido = id_pedido  # Público
        self.status = status  # Público
        self.data_criacao = data_criacao  # Público
        self._entrega_prevista = entrega_prevista  # Protegido
        self._rota = rota  # Protegido
        self._transporte = transporte  # Protegido
        self._valor_total = valor_total  # Protegido
        self._avaliacao_cliente = avaliacao_cliente  # Protegido
        self._comentarios = comentarios  # Protegido
        self.__entregador = None  # Privado
        self.__coordenada = None  # Privado

   
    @property
    def id_pedido(self):
        return self._id_pedido

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        self._status = novo_status

    @property
    def data_criacao(self):
        return self._data_criacao

    @property
    def entrega_prevista(self):
        return self._entrega_prevista

    @entrega_prevista.setter
    def entrega_prevista(self, nova_data):
        if isinstance(nova_data, date):
            self._entrega_prevista = nova_data
        else:
            raise ValueError("A data de entrega prevista deve ser um objeto do tipo date.")

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def valor_total(self, valor):
        if valor >= 0:
            self._valor_total = valor
        else:
            raise ValueError("O valor total não pode ser negativo.")

    @property
    def avaliacao_cliente(self):
        return self._avaliacao_cliente

    @avaliacao_cliente.setter
    def avaliacao_cliente(self, nota):
        if 0 <= nota <= 5:
            self._avaliacao_cliente = nota
        else:
            raise ValueError("A nota deve estar entre 0 e 5 Estrelas.")

    @property
    def comentario(self):
        return self._comentario

    @comentario.setter
    def comentario(self, texto):
        self._comentario = texto

    @property
    def transporte(self):
        return self._transporte

    @transporte.setter
    def transporte(self, transporte):
        self._transporte = transporte

    def calcular_valor_entrega(self) -> float:
        if self._rota:
            return len(self._rota) * 5
        return 0.0

    def gerar_rota(self, endereco_origem: str, endereco_destino: str):
        self._rota = [endereco_origem, endereco_destino]

    def atribuir_entregador(self, entregador):
        self.__entregador = entregador

    def atualizar_localizacao(self, coordenada):
        self.__coordenada = coordenada

    def calcular_preco_final(self) -> float:
        return self.valor_total + self.calcular_valor_entrega()

    def registrar_avaliacao(self, nota: int, comentario: str):
        self.avaliacao_cliente = nota
        self.comentario = comentario
        

class Produto:
    def __init__(self, nomeProduto: str, peso: float, dimensoes: str, fragil: bool):
        self.nomeProduto = nomeProduto
        self.peso = peso
        self.dimensoes = dimensoes
        self.fragil = fragil
        
    @property
    def nomeProduto(self):
        return self._nomeProduto

    @nomeProduto.setter
    def nomeProduto(self, nomeProduto):
        self._nomeProduto = nomeProduto
        
    @property
    def peso(self):
        return self._peso
    @peso.setter
    def peso(self, peso):
        if peso > 0:
            self._peso = peso
        else:
            raise ValueError("O peso deve ser maior que zero.")
    
    @property
    def dimensoes(self):
        return self._dimensoes
    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self._dimensoes = dimensoes
        
    @property
    def fragil(self):
        return self._fragil
    @fragil.setter
    def fragil(self, fragil):
        self._fragil = fragil
        

class Conta:
    def __init__(self, id_conta, nome_cliente, email, telefone, endereco):
        self.id_conta = id_conta  # Público
        self.nome_cliente = nome_cliente  # Público
        self.email = email  # Público
        self.telefone = telefone  # Público
        self._endereco = endereco  # Protegido
        self.__senha = None  # Privado  
        
    @property
    def senha(self):
        return self.__senha    
    
    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) >= 8:
            self.__senha = nova_senha
        else:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")
        

def autenticar(self,email,senha):
    return self.email == email and self._senha == senha


def autenticar(self,email,senha):
    return self.email == email and self._senha == senha

def alterar_senha(self, nova_senha):
    
    self.senha = nova_senha
    
def alterar_endereco(self, novo_endereco):
    
    self._endereco = novo_endereco
        
        
        
            
   

