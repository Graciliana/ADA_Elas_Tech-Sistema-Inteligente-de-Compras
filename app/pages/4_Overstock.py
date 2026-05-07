"""
4 — Overstock
Objetivo

Monitorar excesso de estoque.

Conteúdo
✔️ capital parado
✔️ produtos com excesso
✔️ categorias com excesso
✔️ overstock médio (%)
✔️ tabelas operacionais

Responder:

quais produtos possuem excesso?
quais categorias estão superestocadas?
onde reduzir compras?
quais produtos possuem baixo giro?
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.load_data import load_inventory

PRIMARY_COLOR = "#50e550"

df = load_inventory()

st.title('📦 Overstock')

st.sidebar.header('Filtros')

# categorias

categories = sorted(
    df['product_category_name']
    .dropna()
    .unique()
)


selected_category = st.sidebar.selectbox(
    'Categoria',
    ['Todas'] + list(categories),
    key = 'overstock_category'

)

filtered_df = df.copy()

if selected_category != 'Todas':

    filtered_df = filtered_df[
        filtered_df[
            'product_category_name'
        ] == selected_category
    ]

# produtos com Overstock
overstock_df = filtered_df[
    filtered_df['overstock_pct'] > 50
]

# KPIS
overstock_products = (
    overstock_df['product_id']
    .nunique()
)

average_overstock = (
    filtered_df['overstock_pct']
    .mean()
)

max_overstock = (
    filtered_df['overstock_pct']
    .max()
)

# CARDS
col1, col2, col3 = st.columns(3)

col1.metric(
    'Produtos Overstock',
    overstock_products
)

col2.metric(
    'Overstock Médio (%)',
    round(average_overstock, 2)
)

col3.metric(
    'Maior Overstock (%)',
    round(max_overstock, 2)
)

# Categorias com Maior Overstock
overstock_by_category = (
    filtered_df.groupby(
        'product_category_name'
    )['overstock_pct']
    .mean()
    .sort_values(ascending=True)
    .head(10)
    .reset_index()
)

fig = px.bar(
    overstock_by_category,

    x='overstock_pct',
    y='product_category_name',

    orientation='h',

    title='Categorias com Maior Overstock',

    labels={
        'overstock_pct': 'Overstock Médio (%)',
        'product_category_name': 'Categoria do Produto'
    },

    color_discrete_sequence=['#64b5f6']
)

st.plotly_chart(
    fig,
    use_container_width=True
)
# Produtos com Maior Overstock
top_products = (
    overstock_df.groupby(
        [
            'product_id',
            'product_category_name'
        ]
    )['overstock_pct']
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

    x='overstock_pct',
    y='Produto',

    orientation='h',

    title='Produtos com Maior Overstock',

    labels={
        'overstock_pct': 'Overstock (%)',
        'Produto': 'Produto'
    },

    color_discrete_sequence=['#64b5f6']
)

st.plotly_chart(
    fig,
    use_container_width=True
)

    
# MOSTRAR A TABELA 
st.subheader(
    '📋 Produtos em Excesso no Estoque'
)

## Tabela Operacional
table_df = overstock_df[
    [
        'product_id',
        'product_category_name',
        'prediction',
        'simulated_stock',
        'overstock_pct',
        'recommendation'
    ]
].copy()

## RENOMEAR
table_df = table_df.rename(
    columns={
        'product_id': 'ID Produto',
        'product_category_name': 'Categoria',
        'prediction': 'Demanda Prevista',
        'simulated_stock': 'Estoque Simulado',
        'overstock_pct': 'Overstock (%)',
        'recommendation': 'Recomendação'
    }
)

# CORES DA TABELA 
def highlight_overstock(row):

    overstock = row['Overstock (%)']

    if overstock > 100:
        return ['background-color: #1e88e5'] * len(row)

    elif overstock > 50:
        return ['background-color: #90caf9'] * len(row)

    else:
        return ['background-color: #ba68c8'] * len(row)
    
    st.subheader(
    '📋 Produtos com Overstock'
)

st.dataframe(
    table_df
    .sort_values(
        'Overstock (%)',
        ascending=False
    )
    .style
    .apply(
        highlight_overstock,
        axis=1
    ),

    use_container_width=True
)

st.info(
    '''
    Produtos com overstock apresentam
    estoque acima da demanda prevista,
    indicando possível excesso operacional.

    Recomenda-se:
    - reduzir compras
    - realizar promoções
    - redistribuir estoque
    - revisar política de reposição
    '''
)