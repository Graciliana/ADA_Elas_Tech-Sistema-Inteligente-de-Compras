# 🛒 Sistema Inteligente de Compras
### ADA Tech · Elas Tech · Hackathon de Análise de Dados

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-1.57.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-3.0.2-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-%20Concluído-green?style=for-the-badge" />
</p>

---

## 📖 Nossa História — O Storytelling do Projeto

> *"Como consumidores, todos já nos perguntamos: estou pagando um preço justo por isso?"*

A ideia nasceu de uma dor real e cotidiana: a dificuldade de tomar decisões de compra inteligentes sem ter acesso a dados organizados e contextualizados. Em um cenário de alta inflação e tantas opções de produtos, o consumidor muitas vezes compra por impulso ou sem comparação de preços.

**Nossa missão foi clara desde o início:** transformar dados brutos de compras em inteligência acionável — uma ferramenta que não apenas informa, mas orienta.

Durante o hackathon, construímos uma jornada em três atos:

**Ato 1 — A Exploração:** mergulhamos nos dados, descobrindo padrões, anomalias e oportunidades escondidas nos registros de compras. Cada coluna do dataset contou uma história.

**Ato 2 — A Análise:** com Python e Pandas, transformamos observações em insights. Identificamos tendências de preço, categorias mais relevantes, comportamentos de compra e muito mais.

**Ato 3 — A Solução:** materializamos tudo isso em uma aplicação web interativa com Streamlit — acessível, visual e prática para qualquer pessoa, sem precisar ser especialista em dados.

O resultado é um **Sistema Inteligente de Compras**: uma plataforma que coloca o poder da análise de dados nas mãos do consumidor.

---

## 🎯 Sobre o Projeto

O **Sistema Inteligente de Compras** é uma solução desenvolvida durante o hackathon do programa **ADA Tech · Elas Tech**, voltado para o empoderamento de mulheres na tecnologia. O projeto combina análise exploratória de dados, visualizações interativas e uma interface amigável para auxiliar na tomada de decisão de compra.

### Principais objetivos:
- Analisar padrões e tendências em dados de compras
- Identificar oportunidades de economia para o consumidor
- Disponibilizar insights de forma visual e acessível via dashboard interativo
- Demonstrar a aplicação prática de ciência de dados no cotidiano

---

## 🗂️ Estrutura do Repositório

```
ADA_Elas_Tech-Sistema-Inteligente-de-Compras/
│
├── 📁 notebooks/                  # Análises e exploração de dados
│   └── (Jupyter Notebooks com EDA, limpeza de dados e modelagem)
│
├── 📁 app/                        # Aplicação web Streamlit
│   └── (Código da interface interativa e dashboard)
│
├── 📄 requirements.txt            # Dependências do projeto
├── 📄 .gitignore                  # Arquivos ignorados pelo Git
└── 📄 README.md                   # Documentação do projeto
```

---

## 🔬 Notebooks — A Jornada pelos Dados

A pasta `notebooks/` contém toda a análise desenvolvida ao longo do hackathon, organizada de forma progressiva:

### 📊 Análise Exploratória de Dados (EDA)
- Carregamento e inspeção inicial do dataset
- Tratamento de valores nulos e inconsistências
- Estatísticas descritivas (média, mediana, desvio padrão)
- Distribuição de variáveis numéricas e categóricas

### 📈 Visualizações e Insights
- Gráficos de distribuição de preços por categoria
- Análise de tendências temporais
- Identificação de produtos com maior variação de preço
- Correlações entre variáveis relevantes

### 🤖 Modelagem e Inteligência
- Segmentação e agrupamento de produtos/compras
- Identificação de padrões de comportamento de compra
- Geração de métricas de suporte à decisão

---

## 🖥️ Aplicação Web — O Dashboard Interativo

A pasta `app/` contém a aplicação construída com **Streamlit**, que transforma toda a análise em uma experiência interativa e intuitiva.

### Funcionalidades da aplicação:
- **Visão geral do painel:** resumo dos principais indicadores
- **Exploração de produtos:** filtros por categoria, preço e período
- **Comparação de preços:** análise comparativa entre itens e datas
- **Recomendações inteligentes:** insights de economia baseados nos dados
- **Visualizações dinâmicas:** gráficos interativos com Altair e Pydeck

Para executar a aplicação localmente:

```bash
# 1. Clone o repositório
git clone https://github.com/Graciliana/ADA_Elas_Tech-Sistema-Inteligente-de-Compras.git
cd ADA_Elas_Tech-Sistema-Inteligente-de-Compras

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute a aplicação
streamlit run app/app.py
```

A aplicação ficará disponível em `http://localhost:8501`.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|---|---|---|
| **Python** | 3.10+ | Linguagem principal |
| **Streamlit** | 1.57.0 | Interface web interativa |
| **Pandas** | 3.0.2 | Manipulação e análise de dados |
| **NumPy** | 2.4.4 | Operações numéricas |
| **Altair** | 6.1.0 | Visualizações declarativas |
| **Pydeck** | 0.9.2 | Visualizações geoespaciais |
| **Pillow** | 12.2.0 | Processamento de imagens |
| **PyArrow** | 24.0.0 | Processamento eficiente de dados |
| **Requests** | 2.33.1 | Requisições HTTP |
| **Uvicorn** | 0.46.0 | Servidor ASGI |

---

## ⚙️ Instalação e Configuração

### Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo a passo

```bash
# Clone o repositório
git clone https://github.com/Graciliana/ADA_Elas_Tech-Sistema-Inteligente-de-Compras.git

# Entre no diretório do projeto
cd ADA_Elas_Tech-Sistema-Inteligente-de-Compras

# (Recomendado) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale todas as dependências
pip install -r requirements.txt

# Para os notebooks, abra o Jupyter
jupyter notebook notebooks/

# Para rodar a aplicação
streamlit run app/app.py
```

---

## 👩‍💻 Time

Este projeto foi desenvolvido com muito carinho e dedicação por um grupo de mulheres participantes do programa **ADA Tech · Elas Tech** — uma iniciativa que acredita no poder da tecnologia como ferramenta de transformação e inclusão.

| Nome | GitHub |
|---|---|
| _Beatriz_ | — |
| _Carla Oliveira_ | [@Carla Oliveira](https://github.com/carlaoliveiraads) |— |
| _Franciele_ | — | [@Franciele Oliveira](https://github.com/Franciele01000110) |
| Graciliana | [@Graciliana](https://github.com/Graciliana) |
| _Nivea_ | — |

---

## 💡 Aprendizados 

Durante o hackathon, o time enfrentou e superou desafios reais de ciência de dados: desde a limpeza e tratamento de dados sujos até a construção de uma interface funcional e visualmente agradável em tempo limitado.

**O que aprendemos:**
- A importância de uma boa EDA antes de qualquer modelagem
- Como o Streamlit acelera a prototipagem de produtos de dados
- A força do trabalho colaborativo em ciência de dados


## 📜 Licença

Este projeto foi desenvolvido para fins educacionais no contexto do hackathon ADA Tech · Elas Tech.

---

<p align="center">
  Feito com 💜 pelo time <strong>Elas Tech</strong> · ADA Tech Hackathon
</p>
