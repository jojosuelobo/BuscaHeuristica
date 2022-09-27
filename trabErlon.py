
class Vertice:

    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo # Nome
        self.visitado = False # Se o vértice já foi visitado
        self.distancia_objetivo = distancia_objetivo # Distância entre vértice e objetivo
        self.adjacentes = [] # Lista de adjacentes, vértices vizinhos ao vértice 

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)


class Adjacente:

    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo

        # Novo atributo
        self.distancia_mapa = vertice.distancia_objetivo + self.custo

class Grafo:
  # Criamos as cidades
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)

  # Adição de cidades adjacentes
  # PS: É adicionado o mesmo valor 2x, para da a intenção de Ida e Vola
    arad.adiciona_adjacente(Adjacente(zerind, 75)) # Ex: Ida
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))
     
    zerind.adiciona_adjacente(Adjacente(arad, 75)) # Ex: Volta
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

    dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacente(Adjacente(craiova, 120))

    craiova.adiciona_adjacente(Adjacente(dobreta, 120))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))
    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))

grafo = Grafo()

import numpy as np

class VetorOrdenado: # Armazena as cidades adjacentes

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

    # Referência para o vértice e comparação com a distância para o objetivo
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1): # Percorre todo o vetor
            posicao = i
            if self.valores[
                    i].distancia_mapa > adjacente.distancia_mapa:
                break
            if i == self.ultima_posicao: # Caso para atualizar útima posição
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x] # Desloca valores para inserção
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.rotulo, ' - ',
                      self.valores[i].custo, ' - ',
                      self.valores[i].vertice.distancia_objetivo, ' - ',
                      self.valores[i].distancia_mapa)


grafo.arad.adjacentes
grafo.arad.adjacentes[0].vertice.rotulo, grafo.arad.adjacentes[
    0].vertice.distancia_objetivo

grafo.arad.adjacentes[0].distancia_mapa, grafo.arad.adjacentes[0].custo

vetor = VetorOrdenado(20)
vetor.insere(grafo.arad.adjacentes[0])
vetor.insere(grafo.arad.adjacentes[1])
vetor.insere(grafo.arad.adjacentes[2])

vetor.imprime()

class mapa:

    def __init__(self, objetivo):
        self.objetivo = objetivo # Self.parametro -> Atributo
        self.encontrado = False

    def buscar(self, atual): # Função de teste de objetivo
        print('------------------')
        print('Atual: {}'.format(atual.rotulo))
        atual.visitado = True # Marca o atual como visitado

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes)) # Cria um vetor ordenado com tamanho da quantidade
            for adjacente in atual.adjacentes: # Percorre a lista de vizinhos do grafo atual
                if adjacente.vertice.visitado == False: # Se o vizinho ainda não for visitado
                    adjacente.vertice.visitado = True # Marca-o como visitado
                    vetor_ordenado.insere(adjacente) # Insere dentro do vetor ordenado como um vizinho do nó atual
            vetor_ordenado.imprime() # Mostra o vizinho como nó do atual

            if vetor_ordenado.valores[0] != None: # Se o vetor ordenado tiver algum objeto de início
                self.buscar(vetor_ordenado.valores[0].vertice) # Busca pelo inicio do vetor ordenado


#busca_heuristica = mapa(grafo.bucharest)
#busca_heuristica.buscar(grafo.arad) 

busca_heuristica = mapa(grafo.sibiu)
busca_heuristica.buscar(grafo.arad) 
