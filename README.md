# Biblioteca API

API RESTful para gerenciamento de uma biblioteca (autores e livros), construída com Django e Django REST Framework.

## Requisitos

- Python 3.13 (testado com 3.13.14; compatível com Python 3.10+)

## Instalação

### 1. Criar e ativar o ambiente virtual

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar as variáveis de ambiente

Copie o arquivo de exemplo:

```powershell
# Windows (PowerShell)
Copy-Item .env.example .env
```

```bash
# Linux / macOS
cp .env.example .env
```

Gere uma `SECRET_KEY` e cole o valor em `SECRET_KEY=` no arquivo `.env`:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

| Variável        | Descrição                                   | Padrão                |
|-----------------|---------------------------------------------|-----------------------|
| `SECRET_KEY`    | Chave secreta do Django (obrigatória)       | —                     |
| `DEBUG`         | Modo de depuração (`True` ou `False`)       | `False`               |
| `ALLOWED_HOSTS` | Hosts permitidos, separados por vírgula     | `localhost,127.0.0.1` |

### 4. Aplicar as migrações

```bash
python manage.py migrate
```

### 5. Criar um superusuário (opcional)

Necessário apenas para acessar o painel administrativo em `/admin/`.

```bash
python manage.py createsuperuser
```

### 6. Executar o servidor

```bash
python manage.py runserver
```

A API fica disponível em `http://127.0.0.1:8000/api/`.

## Endpoints

### Autores

| Método   | Rota                  | Descrição                      |
|----------|-----------------------|--------------------------------|
| `GET`    | `/api/autores/`       | Lista os autores (paginado)    |
| `POST`   | `/api/autores/`       | Cria um autor                  |
| `GET`    | `/api/autores/<id>/`  | Detalha um autor e seus livros |
| `PUT`    | `/api/autores/<id>/`  | Atualiza um autor (completo)   |
| `PATCH`  | `/api/autores/<id>/`  | Atualiza um autor (parcial)    |
| `DELETE` | `/api/autores/<id>/`  | Remove um autor                |

### Livros

| Método   | Rota                 | Descrição                    |
|----------|----------------------|------------------------------|
| `GET`    | `/api/livros/`       | Lista os livros (paginado)   |
| `POST`   | `/api/livros/`       | Cria um livro                |
| `GET`    | `/api/livros/<id>/`  | Detalha um livro             |
| `PUT`    | `/api/livros/<id>/`  | Atualiza um livro (completo) |
| `PATCH`  | `/api/livros/<id>/`  | Atualiza um livro (parcial)  |
| `DELETE` | `/api/livros/<id>/`  | Remove um livro              |

Ao criar ou atualizar um livro, o autor é informado pelo campo `autor_id`:

```json
{
  "titulo": "Dom Casmurro",
  "isbn": "9788535910663",
  "ano_publicacao": 1899,
  "genero": "ROMANCE",
  "autor_id": 1
}
```

Gêneros aceitos: `FICCAO`, `ROMANCE`, `TECNICO`, `BIOGRAFIA`, `FANTASIA`.

### Filtros

| Recurso   | Parâmetro          | Exemplo                            |
|-----------|--------------------|------------------------------------|
| Autores   | `?nacionalidade=`  | `/api/autores/?nacionalidade=Brasileira` |
| Livros    | `?genero=`         | `/api/livros/?genero=ROMANCE`      |
| Livros    | `?autor=`          | `/api/livros/?autor=1`             |
| Livros    | `?ano_publicacao=` | `/api/livros/?ano_publicacao=1899` |

### Paginação

As listagens retornam 10 itens por página. Use `?page=` para navegar:

```
/api/livros/?page=2
```

## Regras de negócio

- O `isbn` de um livro é único; cadastrar um ISBN repetido retorna `400 Bad Request`.
- O `ano_publicacao` não pode ser maior que o ano atual; caso contrário, retorna `400 Bad Request`.
- Um autor que possui livros vinculados não pode ser removido: o `DELETE` retorna `400 Bad Request`.
