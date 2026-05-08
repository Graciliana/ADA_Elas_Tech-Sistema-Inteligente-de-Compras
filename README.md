<h1 align="center">
Sistema Inteligente de Compras com Machine Learning
</h1>

<p align="center">
Machine Learning • Forecasting • Supply Chain • Analytics
</p>

> Um sistema inteligente para previsão de demanda, monitoramento de ruptura de estoque e identificação de overstock utilizando Ciência de Dados, Machine Learning e Streamlit.

<h3 align="center"> 
ADA Tech · Elas Tech · Hackathon de Análise de Dados
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-1.57.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-3.0.2-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-%20Concluído-green?style=for-the-badge" />
</p>

---

## Objetivo do Projeto

> Este projeto foi desenvolvido com o objetivo de construir um sistema inteligente capaz de apoiar decisões operacionais relacionadas a:

- previsão de demanda
- gestão de estoque
- prevenção de ruptura
- redução de overstock
- recomendação inteligente de compras

O sistema utiliza técnicas de:

- análise de dados
- feature engineering
- machine learning
- forecasting
- visualização de dados

para transformar dados históricos em decisões operacionais inteligentes.

---

## Problema de Negócio

Empresas que trabalham com estoque enfrentam desafios como:

- falta de produtos (ruptura)
- excesso de estoque (overstock)
- capital parado
- desperdício operacional
- baixa previsibilidade de demanda

Este projeto busca minimizar esses problemas através de modelos preditivos e analytics.

---

## Solução Desenvolvida

O sistema realiza:

✅ previsão de demanda por produto
✅ monitoramento de risco de ruptura
✅ identificação de excesso de estoque
✅ recomendações inteligentes de compra
✅ dashboard interativo para tomada de decisão

---

## Funcionalidades

### Previsão de Demanda

- previsão de vendas futuras
- análise temporal
- comparação real vs previsto

### Monitoramento de Ruptura

- identificação de produtos críticos
- risco percentual de ruptura
- priorização operacional

### Overstock

- detecção de excesso de estoque
- produtos com baixo giro
- redução de compras

### Recomendações Inteligentes

- Compra Urgente
- Reposição Moderada
- Reduzir Compras
- Estoque Saudável

---

## Arquitetura do Projeto

```
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── 01_business_understanding.ipynb
│   ├── 02_data_understanding.ipynb
│   ├── 03_data_preparation.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_modeling_baseline.ipynb
│   ├── 06_modeling_previsao.ipynb
│   ├── 07_modeling_previsao_por_produto.ipynb
│   ├── 08_modeling_estoque.ipynb
│
├── app
│   ├── Home.py
│   ├── pages
│   │   ├── 2_previsao.py
│   │   ├── 3_ruptura.py
│   │   ├── 4_overstock.py
│   │   └── 5_recomendacoes.py
│   │
│   └── utils
│       └── load_data.py
│
├── requirements.txt
└── README.md

```

---

## Pipeline do Projeto

1️⃣ Business Understanding

Definição do problema de negócio e objetivos estratégicos.

2️⃣ Data Understanding

Análise exploratória dos dados (EDA).

3️⃣ Data Preparation

Tratamento de:

- dados faltantes
- outliers
- normalização
- criação da base de demanda

4️⃣ Feature Engineering

Criação de variáveis:

- lags temporais
- médias móveis
- features sazonais
- rolling windows

5️⃣ Modelagem

Benchmark de modelos:

- Linear Regression
- Random Forest
- XGBoost

6️⃣ Forecasting

Previsão de demanda por produto e categoria.

7️⃣ Previsão por Produtos e Categoria

Cálculo de:

- ruptura
- overstock
- estoque de segurança
- recomendações automáticas

8️⃣ Previsões para o estoque

- ruptura
- overstock
- estoque de segurança
- recomendações automáticas

9️⃣ app- Dashboard Streamlit

Visualização interativa dos indicadores operacionais.

---

## Modelos Utilizados

| Modelo            | Objetivo                                 |
| ----------------- | ---------------------------------------- |
| Linear Regression | Baseline de previsão de demanda          |
| Random Forest     | Modelo de previsão baseado em ensemble   |
| XGBoost           | Modelo avançado para previsão de demanda |

---

## Métricas Avaliadas

- MAE
- MSE
- RMSE
- R²
- MAPE

---

## Tecnologias Utilizadas

### Linguagens

- Python

### Bibliotecas

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- plotly
- streamlit

---

## Impacto do Projeto

### Impacto Financeiro

- redução de desperdício
- diminuição de capital parado
- otimização de compras
- maior eficiência operacional

### Impacto Ecológico

- redução de desperdício
- menor descarte de produtos
- logística mais eficiente
- consumo mais inteligente

---

## Como Executar o Projeto

## 1️⃣ Download da Base de Dados

O projeto utiliza o dataset público da Olist disponibilizado no Kaggle.

Faça o download da base:

Dataset Olist no Kaggle [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database)

---

### Estrutura esperada

Após o download:

- extraia o arquivo .zip
- mova o arquivo .sqlite para:

```bash
data/raw/
```

---

### Estrutura final

data/
└── raw/
└── olist.sqlite
└── processed/

> ⚠️ O dataset não está versionado no repositório devido ao tamanho do arquivo.

---

## 2️⃣ Clonar o repositório

```bash
# 1. Clone o repositório
git clone https://github.com/Graciliana/ADA_Elas_Tech-Sistema-Inteligente-de-Compras.git
```

Ou acesse diretamente:

[Repositório no GitHub](https://github.com/Graciliana/ADA_Elas_Tech-Sistema-Inteligente-de-Compras.git)

---

## 3️⃣ Criar ambiente virtual

```bash
python -m venv .venv

```

## 4️⃣ Ativar ambiente virtual

### Windows

```bash
.venv\Scripts\activate

```

### Linux/Mac

```bash
source .venv/bin/activate

```

---

## 5️⃣ Instalar dependências

```bash
pip install -r requirements.txt

```

---

## 6️⃣ Executar os notebooks

```
├── notebooks
│   ├── 01_business_understanding.ipynb
│   ├── 02_data_understanding.ipynb
│   ├── 03_data_preparation.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_modeling_baseline.ipynb
│   ├── 06_modeling_previsao.ipynb
│   ├── 07_modeling_previsao_por_produto.ipynb
│   ├── 08_modeling_estoque.ipynb

```

## 7️⃣ Executar o dashboard

```
streamlit run app/Home.py
```

---

## Resultados Obtidos

O sistema foi capaz de:

✅ prever demanda futura
✅ identificar produtos críticos
✅ detectar excesso de estoque
✅ gerar recomendações inteligentes
✅ apoiar decisões operacionais

---

## Aprendizados

Durante o desenvolvimento foram aplicados conhecimentos em:

- ciência de dados
- engenharia de dados
- machine learning
- forecasting
- supply chain analytics
- visualização de dados
- engenharia de features

Durante o hackathon, o time enfrentou e superou desafios reais de ciência de dados: desde a limpeza e tratamento de dados sujos até a construção de uma interface funcional e visualmente agradável em tempo limitado.

> **O que aprendemos:**

- A importância de uma boa EDA antes de qualquer modelagem
- Como o Streamlit acelera a prototipagem de produtos de dados
- A força do trabalho colaborativo em ciência de dados

---

## Time

Este projeto foi desenvolvido com muito carinho e dedicação por um grupo de mulheres participantes do programa **ADA Tech · Elas Tech** — uma iniciativa que acredita no poder da tecnologia como ferramenta de transformação e inclusão.

| Nome               | GitHub                                                     | Linkedin                                                 |
| ------------------ | ---------------------------------------------------------- | -------------------------------------------------------- |
| Beatriz Porto      | [@mpbeatriz](https://github.com/mpbeatriz)                 | https://www.linkedin.com/in/beatriz-de-m-porto/          |
| Carla Oliveira     | [@Carla Oliveira](https://github.com/carlaoliveiraads)     | https://www.linkedin.com/in/carla-oliveira-ads/          |
| Franciele Oliveira | [@Franciele01000110](https://github.com/Franciele01000110) | https://www.linkedin.com/in/franciele-oliveira-b02296211 |
| Graciliana Kascher | [@Graciliana](https://github.com/Graciliana)               | https://www.linkedin.com/in/gracilianakascher/           |
| Nivea Oliveira     | [@niveaaoliveira](https://github.com/niveaaoliveira)       | https://www.linkedin.com/in/niveaaoliveira               |

---

## 📜 Licença

Este projeto foi desenvolvido para fins educacionais no contexto do hackathon ADA Tech · Elas Tech.

---

## Próximos Passos

- deploy em nuvem
- integração em tempo real
- APIs de recomendação
- alertas automáticos
- integração com ERP
- modelos deep learning

<p align="center">
  Feito com 💜 pelo time <strong>Elas Tech</strong> · ADA Tech Hackathon
</p>
