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
- **Django Templates:** Para renderização dinâmica de páginas HTML.
- **SQLite:** Banco de dados para armazenar informações.

## Como Executar o Projeto

1.  **Clone o Repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <DIRETORIO_DO_PROJETO>
    ```
2.  **Crie um ambiente virtual (opcional, mas recomendado):**
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
3.  **Instale o django:**
    ```bash
    pip install django
    ```
4.  **Aplique as migrações:**
    ```bash
    python manage.py migrate
    ```
5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
6.  **Acesse o aplicativo no navegador:**
    Abra seu navegador e vá para `http://127.0.0.1:8000/diario/`.

## Contribuições

Contribuições são bem-vindas! Se você encontrar bugs ou tiver sugestões de melhorias, por favor, abra uma issue ou envie um pull request.
