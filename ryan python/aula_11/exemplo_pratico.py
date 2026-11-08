class TerminalAtendimento:
    def __init__(self,indentificador):
        self.indentificador = indentificador
        self.ativo = False


    def ligar(self):
        self.ativo = True

        print(f"[SISTEMA]{self.indentificador}inicializado.")

meu_terminal = TerminalAtendimento("TERM-01")
meu_terminal.ligar()