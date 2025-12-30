# Projeto Diário Pessoal Fullstack

Este é um projeto fullstack para um diário pessoal, que permite aos usuários registrar seus pensamentos e momentos diários, associá-los a pessoas e tags, além de visualizar suas entradas de forma organizada.

## Funcionalidades

### Registro de Diário
- **Criação de Anotações:** Os usuários podem adicionar novas entradas no diário com título, texto, tags e pessoas associadas.
- **Tags Personalizadas:** As anotações podem ser marcadas com múltiplas tags (Viagem, Trabalho, Outro) para fácil categorização.
- **Associação de Pessoas:** As anotações podem ser relacionadas a pessoas previamente cadastradas, permitindo registrar com quem os momentos foram compartilhados.
- **Visualização por Data:** As anotações podem ser filtradas e visualizadas por data.
- **Exclusão:** Os usuários podem excluir anotações individualmente ou todas as anotações de um dia específico.

### Gerenciamento de Pessoas
- **Cadastro de Pessoas:** Os usuários podem cadastrar pessoas, incluindo seus nomes e fotos (opcional).
- **Exclusão de Pessoas:** Os usuários podem excluir pessoas cadastradas.
- **Listagem de Pessoas:** É possível visualizar todas as pessoas cadastradas.

### Visualização de Dados
- **Gráfico de Barras:** Exibe a quantidade de anotações associadas a cada pessoa cadastrada.
- **Visualização de Anotações:** As anotações são exibidas na página inicial com resumo e tags.

### Interface de Usuário
- **Noções de Design UI/UX:** Interface com arredondamento das bordas de botões interativos. Além de emojis, barra de navegação e logo.
- **Alertas e Notificações:** Exibe mensagens de sucesso e erro para as operações de cadastro, edição e exclusão.

## Tecnologias Utilizadas

### Frontend
- **HTMl:** Para a estrutura da página.
- **Tailwind CSS:** Para estilos e layout responsivo.
- **JavaScript:** Para interação e funcionalidades adicionais.
- **Chart.js:** Para exibição de gráficos de dados.

### Backend
- **Python:** Linguagem de programação principal.
- **Django:** Framework web para o desenvolvimento do backend.
- **Pyllow:** Biblioteca de processamento de imagens para a linguagem de programação Python.
- **Django Templates:** Para renderização dinâmica de páginas HTML.
- **SQLite:** Banco de dados para armazenar informações.
- **Emoji:** Biblioteca de emojis em python.

## Como Executar o Projeto

1.  **Clone o Repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <DIRETORIO_DO_PROJETO>
    ```
2.  **Crie um ambiente virtual:**
    ```bash
    python -m venv venv
    ```
    - Para ativar o ambiente virtual no Linux/macOS:
        ```bash
        source venv/bin/activate
        ```
    - Para ativar o ambiente virtual no Windows:
        ```bash
        venv\Scripts\activate
        ```
3.  **Instale o django, pillow e emoji:**
    ```bash
    pip install django
    pip install pillow
    pip install emoji
    ```
4.  **Crie as classes do arquivo Models.py e Aplique as migrações:**
    ```bash
    python manage.py makemigrations diario
    python manage.py migrate
    ```
5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
6.  **Acesse o sistema no seu navegador:**
    Abra seu navegador e vá para `http://127.0.0.1:8000/diario/`.

## Telas do Projeto

<img width="1349" height="639" alt="image" src="https://github.com/user-attachments/assets/cf8a6607-01d6-4255-ac02-4120ba09c69d" />
Essa tela é a home do site.

#

<img width="1344" height="591" alt="image" src="https://github.com/user-attachments/assets/fcf1ea43-5b71-41f5-bfd6-15176bd9f60e" />
Essa tela faz parte da home, onde mostra as anotações recentes e quantidade de anotações de cada pessoa.

#

<img width="1348" height="635" alt="image" src="https://github.com/user-attachments/assets/d5add269-6b07-4fa2-ac4e-2b64b22474b6" />
Essa é a tela'Pessoas'.

#

<img width="1342" height="628" alt="image" src="https://github.com/user-attachments/assets/74baba43-1758-4c05-99e3-30ec6b40027e" />
Essa é a tela 'Escrever'.

#

<img width="1344" height="627" alt="image" src="https://github.com/user-attachments/assets/61bc2f0c-12e0-424a-98d4-3fd2b6fa931c" />
Essa é a tela 'Anotações Diárias', onde mostra as anotações realizadas naquele dia selecionado.
