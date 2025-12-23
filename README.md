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
- **Design Responsivo:** A interface é adaptável a diferentes tamanhos de tela, proporcionando uma boa experiência em dispositivos móveis e desktops.
- **Alertas e Notificações:** Exibe mensagens de sucesso e erro para as operações de cadastro, edição e exclusão.

## Tecnologias Utilizadas

### Frontend
- **HTML5:** Para a estrutura da página.
- **Tailwind CSS:** Para estilos e layout responsivo.
- **JavaScript:** Para interação e funcionalidades adicionais.
- **Chart.js:** Para exibição de gráficos de dados.

### Backend
- **Python:** Linguagem de programação principal.
- **Django:** Framework web para o desenvolvimento do backend.
- **Pyllow:** Biblioteca de processamento de imagens para a linguagem de programação Python.
- **Django Templates:** Para renderização dinâmica de páginas HTML.
- **SQLite:** Banco de dados para armazenar informações.

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
3.  **Instale o django e pillow:**
    ```bash
    pip install django
    pip install pillow
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
