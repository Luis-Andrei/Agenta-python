# Agenda de Contatos

Uma aplicação de linha de comando para gerenciar contatos, desenvolvida em Python como parte do desafio do módulo "Introdução ao Python".

## 🚀 Funcionalidades

- ✨ Adicionar contatos
- 📋 Listar todos os contatos
- ✏️ Editar contatos existentes
- ⭐ Marcar/desmarcar contatos como favoritos
- 📌 Listar contatos favoritos
- 🗑️ Apagar contatos
- 💾 Persistência de dados (salvamento automático)

## 📋 Requisitos

- Python 3.x
- Módulos padrão do Python (nenhum pacote externo necessário)

## 🛠️ Como Usar

1. Clone o repositório:
```bash
git clone https://github.com/Luis-Andrei/Agenta-python.git
```

2. Navegue até o diretório do projeto:
```bash
cd Agenta-python
```

3. Execute o programa:
```bash
python agenda.py
```

## 📝 Menu de Opções

1. **Adicionar contato**
   - Nome
   - Telefone
   - Email
   - Status de favorito (opcional)

2. **Listar contatos**
   - Mostra todos os contatos cadastrados
   - Contatos favoritos são marcados com ★

3. **Editar contato**
   - Permite atualizar todos os dados de um contato

4. **Marcar/Desmarcar favorito**
   - Alterna o status de favorito de um contato

5. **Listar favoritos**
   - Mostra apenas os contatos marcados como favoritos

6. **Apagar contato**
   - Remove um contato da agenda

0. **Sair**
   - Encerra o programa

## 💾 Armazenamento de Dados

- Os contatos são salvos automaticamente em um arquivo JSON (`contatos.json`)
- Os dados são carregados automaticamente ao iniciar o programa
- Todas as alterações são salvas em tempo real

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido como parte do desafio do módulo "Introdução ao Python", com os seguintes objetivos:

- Praticar conceitos básicos de Python
- Implementar uma aplicação de linha de comando
- Gerenciar dados persistentes
- Criar uma interface amigável para o usuário

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fork o projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✨ Autor

Luis Andrei - [GitHub](https://github.com/Luis-Andrei)

---

Feito com ❤️ por Luis Andrei 👋

---

## 💡 Estrutura do Projeto

- `agenda.py`: Script principal que executa a aplicação.
- (Opcional) `contatos.json`: Arquivo de persistência para salvar os contatos, caso você evolua com leitura/escrita em arquivo JSON.

---

## 🧪 Tecnologias utilizadas

- Python 3
- (Opcional) Módulo `json` (para persistência dos dados)

---

## 🎮 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/agenda-python-terminal.git
   cd agenda-python-terminal
