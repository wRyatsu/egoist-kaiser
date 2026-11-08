# Como rodar o Sazonalizei (Django) na sua máquina

Este pacote já vem com o projeto Django completo ligado ao seu backend
(`InventoryManager` / `PaymentManager`) e ao visual "Sistema Moderno".

> ⚠️ Este código foi escrito e validado sintaticamente aqui, mas **não pôde
> ser executado de fato** neste ambiente (sem acesso à internet para instalar
> o Django). Rode os passos abaixo na sua máquina para testar.

## 1. Criar e ativar um ambiente virtual (recomendado)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

## 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 3. Rodar o servidor

Rode a partir da **pasta raiz do projeto** (onde está o `manage.py` e o
`databaseSazonalizei.db`):

```bash
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000/**

## 4. Login

- **Usuário:** `admin`
- **Senha:** `admin123`

(Configurável em `config/settings.py`, variáveis `APP_USUARIO` / `APP_SENHA`.)

## O que já está ligado ao backend real

- **Dashboard, Financeiro:** `PaymentManager.get_resumo_financeiro_global()`
- **Clientes, Fornecedores, Cadastro (entidades):** `PaymentManager.obter_entidades_detalhadas()` +
  `get_extrato_entidade()`
- **Produtos, Estoque:** `InventoryManager.get_produtos_lista()` + tabela `produto` do banco
- **Relatórios:** notas reais (`fluxosNotasEstoque`) + `gerar_relatorio_markdown_global()`
- **Formulários (Produtos, PDV, Cadastro, Financeiro):** já enviam para as
  APIs reais em `core/views.py` (`/api/cadastrar-produto/`, `/api/comprar/`,
  `/api/vender/`, `/api/cadastrar-entidade/`, `/api/registrar-pagamento/`)

Se o banco ainda estiver vazio (sem produtos/clientes cadastrados), cada
página cai automaticamente em dados de demonstração (ver `core/helpers.py`)
só para a interface não ficar vazia — assim que você cadastrar dados reais,
eles passam a aparecer sozinhos.

## Próximos passos sugeridos

1. Revisar os templates `estoque.html`, `pdv.html`, `financeiro.html` e
   `entidades.html` linha a linha — o JavaScript deles já foi escrito para
   as APIs corretas, mas eu não tive tempo de testar cada payload manualmente.
2. Trocar `SECRET_KEY` e as credenciais de login antes de qualquer uso real.
3. Trocar os emojis do menu por ícones SVG, se quiser um acabamento ainda
   mais "profissional" (hoje eles usam emoji para não depender de nenhuma
   biblioteca de ícones paga/externa).
