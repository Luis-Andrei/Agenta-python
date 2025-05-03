import json
import os

class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

    def to_dict(self):
        return {
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email,
            "favorito": self.favorito
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nome=data["nome"],
            telefone=data["telefone"],
            email=data["email"],
            favorito=data["favorito"]
        )

class Agenda:
    def __init__(self):
        self.contatos = []
        self.arquivo = "contatos.json"
        self.carregar_contatos()

    def carregar_contatos(self):
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    self.contatos = [Contato.from_dict(contato) for contato in dados]
            except Exception as e:
                print(f"\nErro ao carregar contatos: {e}")
                self.contatos = []

    def salvar_contatos(self):
        try:
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump([contato.to_dict() for contato in self.contatos], f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"\nErro ao salvar contatos: {e}")

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        self.salvar_contatos()
        print("\n✅ Contato adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("\n📝 Nenhum contato cadastrado.")
            return
        
        print("\n📋 Lista de Contatos:")
        print("-" * 50)
        for i, contato in enumerate(self.contatos, 1):
            favorito = "★" if contato.favorito else "☆"
            print(f"{i}. {favorito} {contato.nome}")
            print(f"   📞 {contato.telefone}")
            print(f"   📧 {contato.email}")
            print("-" * 50)

    def editar_contato(self, indice, nome, telefone, email):
        if 0 <= indice < len(self.contatos):
            contato = self.contatos[indice]
            contato.nome = nome
            contato.telefone = telefone
            contato.email = email
            self.salvar_contatos()
            print("\n✅ Contato editado com sucesso!")
        else:
            print("\n❌ Índice inválido!")

    def marcar_favorito(self, indice):
        if 0 <= indice < len(self.contatos):
            contato = self.contatos[indice]
            contato.favorito = not contato.favorito
            self.salvar_contatos()
            status = "marcado" if contato.favorito else "desmarcado"
            print(f"\n✅ Contato {status} como favorito!")
        else:
            print("\n❌ Índice inválido!")

    def listar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if not favoritos:
            print("\n📝 Nenhum contato favorito.")
            return
        
        print("\n⭐ Contatos Favoritos:")
        print("-" * 50)
        for i, contato in enumerate(favoritos, 1):
            print(f"{i}. {contato.nome}")
            print(f"   📞 {contato.telefone}")
            print(f"   📧 {contato.email}")
            print("-" * 50)

    def apagar_contato(self, indice):
        if 0 <= indice < len(self.contatos):
            contato = self.contatos.pop(indice)
            self.salvar_contatos()
            print(f"\n✅ Contato '{contato.nome}' apagado com sucesso!")
        else:
            print("\n❌ Índice inválido!")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    agenda = Agenda()
    
    while True:
        limpar_tela()
        print("\n📱 === Agenda de Contatos ===")
        print("\n1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Editar contato")
        print("4. Marcar/Desmarcar favorito")
        print("5. Listar favoritos")
        print("6. Apagar contato")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            limpar_tela()
            print("\n📝 Adicionar Novo Contato")
            print("-" * 30)
            nome = input("Nome: ").strip()
            telefone = input("Telefone: ").strip()
            email = input("Email: ").strip()
            
            if nome and telefone and email:
                contato = Contato(nome, telefone, email)
                agenda.adicionar_contato(contato)
            else:
                print("\n❌ Todos os campos são obrigatórios!")
            
        elif opcao == "2":
            limpar_tela()
            agenda.listar_contatos()
            
        elif opcao == "3":
            limpar_tela()
            agenda.listar_contatos()
            if agenda.contatos:
                try:
                    indice = int(input("\nDigite o número do contato que deseja editar: ")) - 1
                    if 0 <= indice < len(agenda.contatos):
                        print("\n📝 Editar Contato")
                        print("-" * 30)
                        nome = input("Novo nome: ").strip()
                        telefone = input("Novo telefone: ").strip()
                        email = input("Novo email: ").strip()
                        
                        if nome and telefone and email:
                            agenda.editar_contato(indice, nome, telefone, email)
                        else:
                            print("\n❌ Todos os campos são obrigatórios!")
                    else:
                        print("\n❌ Índice inválido!")
                except ValueError:
                    print("\n❌ Por favor, digite um número válido!")
                    
        elif opcao == "4":
            limpar_tela()
            agenda.listar_contatos()
            if agenda.contatos:
                try:
                    indice = int(input("\nDigite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
                    agenda.marcar_favorito(indice)
                except ValueError:
                    print("\n❌ Por favor, digite um número válido!")
                    
        elif opcao == "5":
            limpar_tela()
            agenda.listar_favoritos()
            
        elif opcao == "6":
            limpar_tela()
            agenda.listar_contatos()
            if agenda.contatos:
                try:
                    indice = int(input("\nDigite o número do contato que deseja apagar: ")) - 1
                    agenda.apagar_contato(indice)
                except ValueError:
                    print("\n❌ Por favor, digite um número válido!")
                    
        elif opcao == "0":
            print("\n👋 Saindo da agenda...")
            break
            
        else:
            print("\n❌ Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main() 