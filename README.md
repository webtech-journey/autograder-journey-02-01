
# Autograder para o Journey-02 (ASSPROM)

Este repositório contém um sistema de autograding projetado para avaliar projetos da primeira etapa do WebTech Journey da ASSPROM submetidos no GitHub Classroom. O autograder verifica uma série de condições no repositório do aluno e gera um relatório com a pontuação e feedback. A seguir, está uma explicação detalhada de como funciona o sistema.

## Funcionalidades

### 1. **Verificações de Repositório**

O autograder realiza as seguintes verificações no repositório do aluno:

- **Branch Principal**: Verifica se a branch principal (`main`) existe no repositório.
- **Commits**: Verifica se existe pelo menos um commit no repositório.
- **Arquivo `resumo.txt`**: Verifica se o arquivo `resumo.txt` existe no repositório.
- **Conteúdo do `resumo.txt`**: Verifica se o arquivo `resumo.txt` contém pelo menos três linhas de conteúdo relevante.

### 2. **Geração de Relatório**

O autograder gera um relatório em formato Markdown com as seguintes informações:

- **Pontuação Total**: A pontuação máxima é 100 pontos, dividida entre as verificações.
- **Detalhamento da Pontuação**: Para cada verificação, o sistema indica se foi aprovada ou reprovada e a pontuação correspondente.
- **Sugestões para Melhoria**: Sugestões específicas são fornecidas para as verificações que falharem.
- **Feedback Detalhado**: Um feedback geral é fornecido com base no desempenho do aluno.

O relatório gerado é salvo em um arquivo `relatorio.md` no repositório do aluno.

### 3. **Integração com GitHub Actions**

O autograder está integrado ao GitHub Actions para ser executado automaticamente sempre que um aluno submeter um novo commit. Ele utiliza um arquivo de configuração do GitHub Actions (`action.yml`) para definir como a ferramenta será executada. A ação pode ser personalizada para usar um token de acesso do GitHub para acessar e modificar o repositório.

### 4. **Fluxo de Trabalho**

- O aluno faz uma submissão para o GitHub Classroom.
- O GitHub Actions executa a ação definida em `action.yml`, que chama o script principal `main.py`.
- O script `main.py` realiza as verificações usando as funções de `tests.py`.
- O script `report_generator.py` gera o relatório com as pontuações e feedback.
- O script `commit_report.py` sobrescreve o relatório no repositório do aluno.

### 5. **Como Usar**

#### Requisitos

- Python 3.x
- Bibliotecas: `PyGithub`, `aiohttp`, `argparse` (definidas no arquivo `requirements.txt`)

#### Configuração

1. Instale as dependências executando o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```

2. Configure o GitHub Actions com o arquivo `action.yml`. Certifique-se de que o token do GitHub tenha permissões de escrita para o repositório.

#### Execução

Para executar o autograder manualmente, utilize o script `main.py` com o token do GitHub como argumento:

```bash
python main.py --token <seu_token_do_github>
```

O relatório será gerado e salvo no repositório do aluno como `relatorio.md`.

### 6. **Estrutura do Repositório**

```
/
├── action.yml               # Arquivo de configuração do GitHub Actions
├── commit_report.py         # Script para sobrescrever o relatório no repositório
├── entrypoint.sh            # Script de entrada para execução no Docker
├── export.py                # Script para notificar o GitHub Classroom com a nota final
├── main.py                  # Script principal para execução das verificações e geração do relatório
├── report_generator.py      # Script para gerar o relatório em Markdown
├── requirements.txt         # Arquivo de dependências do Python
├── tests.py                 # Scripts de testes para as verificações
```

