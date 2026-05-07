"""
3 — Risco de Ruptura
Objetivo

Monitorar falta de estoque.

Conteúdo

✔️ top categorias críticas
✔️ top produtos críticos
✔️ tabela operacional
✔️ risco médio (%)

✔️ produtos críticos
✔️ categorias com maior risco
✔️ risco operacional
✔️ recomendações urgentes

Responder:

quais produtos podem faltar?
quais categorias estão críticas?
onde priorizar reposição?
quais produtos exigem compra urgente?

"""

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.load_data import load_inventory

PRIMARY_COLOR = "#50e550"

df = load_inventory()

st.title('🚨 Risco de Ruptura')

st.sidebar.header('Filtros')

categories = sorted(
    df['product_category_name']
    .dropna()
    .unique()
)

selected_category = st.sidebar.selectbox(
    'Categoria',
    ['Todas'] + list(categories),
    key='ruptura_category'
)
# filtros
filtered_df = df.copy()

if selected_category != 'Todas':

    filtered_df = filtered_df[
        filtered_df[
            'product_category_name'
        ] == selected_category
    ]
## pontos criticos

critical_df = filtered_df[
    filtered_df['rupture_risk_pct'] > 50
]

## KPIS
critical_products = (
    critical_df['product_id']
    .nunique()
)

average_risk = (
    filtered_df['rupture_risk_pct']
    .mean()
)

max_risk = (
    filtered_df['rupture_risk_pct']
    .max()
)

# CARDS
col1, col2, col3 = st.columns(3)

col1.metric(
    'Produtos Críticos',
    critical_products
)

col2.metric(
    'Risco Médio (%)',
    round(average_risk, 2)
)

col3.metric(
    'Maior Risco (%)',
    round(max_risk, 2)
)

# CATEGORIAS COM MAIOR RISCO
risk_by_category = (
    filtered_df.groupby(
        'product_category_name'
    )['rupture_risk_pct']
    .mean()
    .sort_values(ascending=True)
    .head(10)
    .reset_index()
)

fig = px.bar(
    risk_by_category,

    x='rupture_risk_pct',
    y='product_category_name',

    orientation='h',

    title='Categorias com Maior Risco de Ruptura',

    labels={
        'rupture_risk_pct': 'Risco Médio (%)',
        'product_category_name': 'Categoria do Produto'
    },

    color_discrete_sequence=[PRIMARY_COLOR]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Produtos com Maior Risco

top_products = (
    critical_df.groupby(
        [
            'product_id',
            'product_category_name'
        ]
    )['rupture_risk_pct']
    .mean()
    .sort_values(ascending=True)
    .head(10)
    .reset_index()
)

top_products['Produto'] = (
    top_products[
        'product_category_name'
    ]
    +
    ' | '
    +
    top_products[
        'product_id'
    ].str[:8]
)

fig = px.bar(
    top_products,

    x='rupture_risk_pct',
    y='Produto',

    orientation='h',

    title='Produtos com Maior Risco',

    labels={
        'rupture_risk_pct': 'Risco de Ruptura (%)',
        'Produto': 'Produto'
    },

    color_discrete_sequence=['#ff4d4d']
)

st.plotly_chart(
    fig,
    use_container_width=True
)

## Tabela Operacional
table_df = critical_df[
    [
        'product_id',
        'product_category_name',
        'prediction',
        'simulated_stock',
        'rupture_risk_pct',
        'recommendation'
    ]
].copy()

table_df = table_df.rename(
    columns={
        'product_id': 'ID Produto',
        'product_category_name': 'Categoria',
        'prediction': 'Demanda Prevista',
        'simulated_stock': 'Estoque Simulado',
        'rupture_risk_pct': 'Risco (%)',
        'recommendation': 'Recomendação'
    }
)

def highlight_risk(row):

    risk = row['Risco (%)']

    if risk > 80:
        return ['background-color: #ff4d4d'] * len(row)

    elif risk > 50:
        return ['background-color: #fff176'] * len(row)

    else:
        return ['background-color: #ba68c8'] * len(row)
    
# MOSTRAR A TABELA 
st.subheader(
    '📋 Produtos Críticos'
)

st.dataframe(
    table_df
    .sort_values(
        'Risco (%)',
        ascending=False
    )
    .style
    .apply(
        highlight_risk,
        axis=1
    ),

    use_container_width=True
)

st.info(
    '''
    Produtos com alto risco de ruptura
    apresentam demanda prevista acima
    do estoque disponível.

    Recomenda-se:
    - reposição prioritária
    - revisão do estoque de segurança
    - monitoramento contínuo
    '''
)