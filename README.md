# Backend do Conversor de PDF para CSV

Este é o backend para a aplicação de conversão de PDF para CSV. É uma API construída com FastAPI que gerencia o upload de arquivos PDF, extrai o texto, o processa e o converte para o formato CSV.

## Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- Uvicorn
- Google Gemini API (para correção e formatação do texto)
- PyMuPDF (para extração de texto de PDFs)

## Estrutura do Projeto

```
api/
├── main.py             # Ponto de entrada da aplicação FastAPI
├── requirements.txt    # Dependências do projeto
└── README.md           # Este arquivo
```

## Endpoints da API

### Processar PDF

- **URL:** `/api/process-pdf/`
- **Método:** `POST`
- **Descrição:** Recebe um arquivo PDF, extrai o texto, utiliza a API do Gemini para formatá-lo como uma tabela e retorna os dados em formato CSV.
- **Corpo da Requisição:** `multipart/form-data`
  - `file`: O arquivo PDF a ser processado.

## Configuração e Instalação

1.  **Navegue até o diretório da API:**
    ```bash
    cd api
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure sua chave da API do Google:**
    Crie um arquivo `.env` na raiz do diretório `api` e adicione sua chave:
    ```
    GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"
    ```
    O aplicativo carregará essa variável de ambiente.

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    uvicorn main:app --reload
    ```

O servidor estará disponível em `http://127.0.0.1:8000`.
