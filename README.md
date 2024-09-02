# SCRIPT_directory_generator_fastAPI
Script em Python para gerar estrutura comum para RestAPI com FastAPI

my_fastapi_project/
│
├── .env
├── requirements.txt
├── alembic.ini  # Arquivo de configuração do Alembic para migrações de banco de dados
│
├───app/
│   ├── main.py  # Ponto de entrada da aplicação
│   ├── config.py  # Configurações gerais da aplicação
│   ├── database.py  # Configurações de banco de dados
│   ├── models.py  # Definições de modelos do SQLAlchemy
│   ├── schemas.py  # Definições de esquemas Pydantic para validação
│   ├── services/  # Lógica de negócios e serviços
│   ├── repositories/  # Repositórios para interagir com o banco de dados
│   ├── routers/  # Rotas da aplicação
│   │   ├── __init__.py
│   │   ├── user_router.py  # Rotas relacionadas a usuários
│   │   └── item_router.py  # Rotas relacionadas a itens
│   ├── utils/  # Utilitários e funções auxiliares
│   └── external/  # Consumo de APIs externas
│       └── api_client.py  # Cliente para consumir APIs externas
│
└───tests/
    ├── __init__.py
    ├── test_main.py  # Testes para o ponto de entrada
    ├── test_user.py  # Testes para rotas de usuário
    └── test_item.py  # Testes para rotas de item
