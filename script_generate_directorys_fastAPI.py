import os
project_name = "filipe"
# Define a estrutura de diretórios
directories = [
    f"{project_name}",
    f"{project_name}/app",
    f"{project_name}/app/services",
    f"{project_name}/app/repositories",
    f"{project_name}/app/routers",
    f"{project_name}/app/utils",
    f"{project_name}/app/external",
    f"{project_name}/tests"
]

# Define os arquivos a serem criados
files = {
    f"{project_name}/.env": "",
    f"{project_name}/requirements.txt": "",
    f"{project_name}/alembic.ini": "# Arquivo de configuração do Alembic para migrações de banco de dados\n",
    f"{project_name}/app/main.py": "# Ponto de entrada da aplicação\n",
    f"{project_name}/app/config.py": "# Configurações gerais da aplicação\n",
    f"{project_name}/app/database.py": "# Configurações de banco de dados\n",
    f"{project_name}/app/models.py": "# Definições de modelos do SQLAlchemy\n",
    f"{project_name}/app/schemas.py": "# Definições de esquemas Pydantic para validação\n",
    f"{project_name}/app/routers/__init__.py": "# Inicializador de rotas\n",
    f"{project_name}/app/routers/user_router.py": "# Rotas relacionadas a usuários\n",
    f"{project_name}/app/routers/item_router.py": "# Rotas relacionadas a itens\n",
    f"{project_name}/app/external/api_client.py": "# Cliente para consumir APIs externas\n",
    f"{project_name}/tests/__init__.py": "# Inicializador de testes\n",
    f"{project_name}/tests/test_main.py": "# Testes para o ponto de entrada\n",
    f"{project_name}/tests/test_user.py": "# Testes para rotas de usuário\n",
    f"{project_name}/tests/test_item.py": "# Testes para rotas de item\n"
}

# Cria os diretórios
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"Directory created: {directory}")

# Cria os arquivos com conteúdo padrão
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)
    print(f"File created: {file_path}")
