import flet as ft
import random
import time

class CampoMinado:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Campo Minado"
        self.tamanho = 16
        self.num_bombas = 40
        self.grid = []
        self.botoes = []
        self.game_over = False
        self.pausado = False
        self.tempo_inicio = None
        self.tempo_pausado = 0
        self.criar_interface()

    def criar_tabuleiro(self):
        self.grid = [[0 for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        bombas_colocadas = 0
        while bombas_colocadas < self.num_bombas:
            x, y = random.randint(0, self.tamanho-1), random.randint(0, self.tamanho-1)
            if self.grid[x][y] != -1:
                self.grid[x][y] = -1
                bombas_colocadas += 1

        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if self.grid[i][j] != -1:
                    self.grid[i][j] = self.contar_bombas_vizinhas(i, j)

    def contar_bombas_vizinhas(self, x, y):
        count = 0
        for i in range(max(0, x-1), min(self.tamanho, x+2)):
            for j in range(max(0, y-1), min(self.tamanho, y+2)):
                if self.grid[i][j] == -1:
                    count += 1
        return count

    def revelar_celula(self, x, y):
        if self.game_over or self.pausado or self.botoes[x][y].disabled:
            return

        self.botoes[x][y].disabled = True
        if self.grid[x][y] == -1:
            self.botoes[x][y].content = ft.Text("💣", color=ft.colors.RED)
            self.game_over = True
            self.mostrar_todas_bombas()
            self.mostrar_dialogo("Game Over!")
        else:
            num_bombas = self.grid[x][y]
            if num_bombas > 0:
                self.botoes[x][y].content = ft.Text(str(num_bombas), color=self.obter_cor_numero(num_bombas))
            else:
                self.revelar_celulas_vazias(x, y)

        self.verificar_vitoria()
        self.page.update()

    def revelar_celulas_vazias(self, x, y):
        for i in range(max(0, x-1), min(self.tamanho, x+2)):
            for j in range(max(0, y-1), min(self.tamanho, y+2)):
                if not self.botoes[i][j].disabled:
                    self.revelar_celula(i, j)

    def colocar_bandeira(self, x, y):
        if self.game_over or self.pausado or self.botoes[x][y].disabled:
            return

        if self.botoes[x][y].content is None:
            self.botoes[x][y].content = ft.Text("🚩", color=ft.colors.RED)
        elif isinstance(self.botoes[x][y].content, ft.Text) and self.botoes[x][y].content.value == "🚩":
            self.botoes[x][y].content = ft.Text("?", color=ft.colors.BLUE)
        else:
            self.botoes[x][y].content = None

        self.page.update()

    def mostrar_todas_bombas(self):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if self.grid[i][j] == -1:
                    self.botoes[i][j].content = ft.Text("💣", color=ft.colors.RED)
                    self.botoes[i][j].disabled = True

    def verificar_vitoria(self):
        celulas_reveladas = sum(1 for linha in self.botoes for botao in linha if botao.disabled)
        if celulas_reveladas == self.tamanho * self.tamanho - self.num_bombas:
            self.game_over = True
            self.mostrar_dialogo("Parabéns! Você venceu!")

    def mostrar_dialogo(self, mensagem):
        self.page.dialog = ft.AlertDialog(title=ft.Text(mensagem))
        self.page.dialog.open = True
        self.page.update()

    def obter_cor_numero(self, numero):
        cores = [ft.colors.BLUE, ft.colors.GREEN, ft.colors.RED, ft.colors.PURPLE,
                 ft.colors.ORANGE, ft.colors.CYAN, ft.colors.BROWN, ft.colors.GREY]
        return cores[numero - 1] if 0 < numero <= len(cores) else ft.colors.BLACK

    def reiniciar_jogo(self, e):
        self.game_over = False
        self.pausado = False
        self.tempo_inicio = time.time()
        self.tempo_pausado = 0
        self.criar_tabuleiro()
        self.atualizar_tabuleiro()
        self.botao_pausa.text = "Pausar"
        self.page.update()

    def pausar_continuar(self, e):
        if self.game_over:
            return
        self.pausado = not self.pausado
        if self.pausado:
            self.tempo_pausado = time.time() - self.tempo_inicio
            self.botao_pausa.text = "Continuar"
        else:
            self.tempo_inicio = time.time() - self.tempo_pausado
            self.botao_pausa.text = "Pausar"
        self.page.update()

    def mudar_tamanho_tabuleiro(self, e):
        if self.tamanho == 16:
            self.tamanho = 8
            self.num_bombas = 10
        else:
            self.tamanho = 16
            self.num_bombas = 40
        self.reiniciar_jogo(None)

    def atualizar_tabuleiro(self):
        self.tabuleiro.controls.clear()
        self.botoes.clear()
        for i in range(self.tamanho):
            linha = ft.Row(spacing=0)
            linha_botoes = []
            for j in range(self.tamanho):
                botao = ft.Container(
                    content=None,
                    width=30,
                    height=30,
                    border=ft.border.all(1, ft.colors.GREY),
                    on_click=lambda _, x=i, y=j: self.revelar_celula(x, y),
                    on_long_press=lambda _, x=i, y=j: self.colocar_bandeira(x, y)
                )
                linha.controls.append(botao)
                linha_botoes.append(botao)
            self.tabuleiro.controls.append(linha)
            self.botoes.append(linha_botoes)
        self.page.update()

    def criar_interface(self):
        self.botao_reiniciar = ft.ElevatedButton("Reiniciar", on_click=self.reiniciar_jogo)
        self.botao_pausa = ft.ElevatedButton("Pausar", on_click=self.pausar_continuar)
        self.botao_tamanho = ft.ElevatedButton("Mudar Tamanho", on_click=self.mudar_tamanho_tabuleiro)
        
        controles = ft.Row([self.botao_reiniciar, self.botao_pausa, self.botao_tamanho])
        self.page.add(controles)

        self.tabuleiro = ft.Column(spacing=0)
        self.page.add(self.tabuleiro)

        self.reiniciar_jogo(None)

def main(page: ft.Page):
    CampoMinado(page)

ft.app(target=main)
