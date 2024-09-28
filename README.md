# Jogo de Campo Minado em Python com Flet

Este repositório contém a implementação de um clássico jogo de Campo Minado, desenvolvido em Python utilizando a biblioteca Flet para a interface gráfica. Esta versão foi projetada para oferecer uma experiência interativa e personalizável, trazendo novas funcionalidades em relação ao jogo original.

## Funcionalidades do Jogo

1. **Tabuleiro Personalizável:**
   - Dois tamanhos de tabuleiro disponíveis:
     - 16x16 com 40 minas.
     - 8x8 com 10 minas.
   - Opção para alternar entre os tamanhos durante o jogo através do botão "Mudar Tamanho".
2. **Interface Intuitiva:**
   - Desenvolvida com Flet, a interface gráfica é amigável e responsiva.
   - Uso de ícones para representar bandeiras e minas, seguindo um estilo similar ao jogo clássico.
3. **Sistema de Bandeiras:**
   - Clique com o botão direito para colocar uma bandeira vermelha (🚩) em células suspeitas.
   - Clique com o botão direito novamente para mudar a bandeira para o estado de "Não tenho certeza" (?).
   - Um terceiro clique remove a bandeira.
4. **Revelação Automática:**
   - Implementa a revelação automática de células vazias adjacentes ao clicar em uma célula vazia.
5. **Controles de Jogo:**
   - **Reiniciar:** Reinicia o tabuleiro atual.
   - **Pausar/Continuar:** Permite pausar o jogo, durante o qual as células não podem ser reveladas nem marcadas.
   - **Mudar Tamanho:** Alterna rapidamente entre os modos de tabuleiros 16x16 e 8x8.
6. **Gerenciamento de Tempo:**
   - Registra o tempo total de jogo, incluindo pausas. (A exibição do tempo pode ser adicionada conforme desejado.

## Ambiente de programação

Criamos o projeto com o `Poetry` com o comando `poetry new Minas`, acessamos o projeto pelo terminal e instalamos a biblioteca `Flet` pelo comando `poetry add flet` com esse comandos já está pronto o ambiente de trabalho.

```bash
❯ exa --tree
.
├── app.py
├── LICENSE
├── minas
│  └── __init__.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── tests
   └── __init__.py
```

## Rodando o código

Logo temos que escrever o código, que pode ser feito por qualquer editor de texto ou código, eu usei o `nano`, mas use o editor que mais for confortável programar, pela integração sugerimos o Pycharm que tem uma excelente integração com o Poetry.

Para rodar use `poetry run flet app.py` ou no navegador use `poetry run flet run -w app.py`.

![Minas_app](/Minas_app.png)





![Minas_web](/Minas_web.png)

## Instruções de Instalação

Para executar o jogo, siga os passos abaixo:

1. **Clone o Repositório:**

   bash

   ```bash
   git clone https://github.com/edius1987/minas.git
   cd Minas 
   ```

2. **Instale a Biblioteca Flet:** Use o gerenciador de pacotes `poetry` para instalar o Flet:

   bash

   ```bash
   poetry update
   ```

3. **Execute o Jogo:** Salve o código do jogo em um arquivo Python, por exemplo, `campo_minado.py`, e execute-o:

   bash

   ```bash
   poetry run flet app.py
   ```

## Como Jogar

- **Clique Esquerdo:** Revela o conteúdo de uma célula.
- **Clique Direito:** Alterna o estado da célula entre bandeira vermelha, ponto de interrogação e sem bandeira.

O objetivo é limpar todo o campo sem ativar nenhuma mina, usando bandeiras para ajudar a marcar possíveis minas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues para reportar problemas ou enviar pull requests com melhorias e novos recursos.

------

Esta descrição estendida deve informar adequadamente os usuários do GitHub sobre as características do jogo e como utilizá-lo, além de convidá-los a contribuir.



