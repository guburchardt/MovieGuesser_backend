# MovieGuesser Backend

Backend para o jogo MovieGuesser, onde os usuários tentam adivinhar filmes baseados em imagens borradas.

## Requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd MovieGuesser_backend
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do TMDB:
```
TMDB_API_KEY=sua_chave_api_aqui
```

## Estrutura do Projeto

O projeto segue os princípios do Domain-Driven Design (DDD):

```
src/
├── application/
│   └── use_cases/
│       ├── get_game_use_case.py
│       ├── update_blur_use_case.py
│       └── reveal_movie_use_case.py
├── domain/
│   ├── entities/
│   │   └── movie.py
│   ├── repositories/
│   │   └── movie_repository.py
│   └── services/
│       └── movie_service.py
├── infrastructure/
│   ├── config/
│   │   └── settings.py
│   └── external/
│       └── tmdb_client.py
└── interfaces/
    ├── api/
    │   └── routes.py
    └── utils/
        └── image_utils.py
```

## Executando o Servidor

Para iniciar o servidor de desenvolvimento:

```bash
python main.py
```

O servidor estará disponível em `http://localhost:5000`

## Endpoints

### GET /api/game
Retorna um jogo com:
- Uma imagem de filme em base64 com blur aplicado
- 4 opções de títulos de filmes
- O ID do filme correto

Parâmetros:
- `blur_level` (opcional): Nível de blur da imagem (1-4, padrão: 1)

### GET /api/update_blur/<movie_id>
Atualiza o nível de blur de uma imagem de filme específica.

Parâmetros:
- `blur_level` (opcional): Nível de blur da imagem (1-4, padrão: 1)

Retorna:
- Imagem atualizada em base64
- ID do filme
- Título do filme

### GET /api/reveal/<movie_id>
Revela a imagem original e o título do filme.

Retorna:
- Imagem original em base64
- Título do filme

## Tecnologias Utilizadas

- Flask
- TMDB API
- Python
- Pillow (para processamento de imagens)
- pytest (para testes)

## Desenvolvimento

### Testes
Para executar os testes:
```bash
pytest
```

### Estrutura DDD

O projeto segue uma arquitetura em camadas:

1. **Domain**: Contém as entidades e regras de negócio
   - `entities`: Classes que representam os objetos do domínio
   - `repositories`: Interfaces para acesso a dados
   - `services`: Lógica de negócio

2. **Application**: Contém os casos de uso
   - `use_cases`: Implementações das operações do sistema

3. **Infrastructure**: Implementações concretas
   - `config`: Configurações do sistema
   - `external`: Integrações com serviços externos

4. **Interfaces**: Camada de apresentação
   - `api`: Rotas e controladores
   - `utils`: Utilitários diversos

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

Projeto jogo de adivinhação
Este projeto será o desenvolvimento de um jogo interativo de adivinhação de filmes. O jogo apresentará uma imagem de um filme ao usuário, que deverá responder a uma pergunta relacionada a esse filme através de um formulário. O sistema será composto por um front-end construído com React com typescript e um back-end, atuando como um proxy para a API pública The Movie Database (TMDb) link da documentação.

O back-end deve ser capaz de:
Comunicar-se com a TMDb API para buscar dados de filmes (imagens, títulos, atores, etc.).
Expor uma API própria para o front-end consumir.

O front-end em React capaz de:
Comunicar-se com a API do back-end para obter dados do jogo (imagem e informações do filme).
Exibir a imagem do filme para o usuário.
Apresentar um formulário para o usuário inserir sua resposta.
Exibir feedback ao usuário (correto/incorreto).

O que esperamos:
frontend responsivo
páginas dinâmicas e intuitivas 

Sugestão de framework css:
Material ui

Tecnologias que nos surpreenderia(opcional):
Docker: dockerizar as aplicações tanto do frontend quando no backend
Testes unitários/componente
https://developer.themoviedb.org/reference/discover-movie
HEADER: eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZGJlODA2ZGU5NDhlYjNlYmIxMzhmMTY4YmZkNTEwYiIsIm5iZiI6MTc0NjgwMTkyMy43NzMsInN1YiI6IjY4MWUxNTAzZWQ1YzY5ZGIzZjg4YzhlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7HtJl3EjRHwKpndZFf3q7WJ3SB9J1liokbwJXmoFnBQ