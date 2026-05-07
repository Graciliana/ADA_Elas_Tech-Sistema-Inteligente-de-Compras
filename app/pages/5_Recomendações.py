"""
— Recomendações
Objetivo

Sistema inteligente de decisão.

Conteúdo

✔️ Compra Urgente
✔️ Reposição Moderada
✔️ Reduzir Compras
✔️ Estoque Saudável

Responder:

o que comprar?
o que reduzir?
o que monitorar?
quais produtos exigem ação urgente?

"""
import streamlit as st
import pandas as pd
import plotly.express as px

from utils.load_data import load_inventory

PRIMARY_COLOR = "#50e550"

df = load_inventory()

st.title('🛒 Recomendações Inteligentes')

categories = sorted(
    df['product_category_name']
    .dropna()
    .unique()
)

selected_category = st.sidebar.selectbox(
    'Categoria',
    ['Todas'] + list(categories),
    key='recommendation_category'
)
# filtros
filtered_df = df.copy()

if selected_category != 'Todas':

    filtered_df = filtered_df[
        filtered_df[
            'product_category_name'
        ] == selected_category
    ]

# KPIs

urgent_count = (
    filtered_df[
        filtered_df[
            'recommendation'
        ] == 'Compra Urgente'
    ]
    .shape[0]
)

moderate_count = (
    filtered_df[
        filtered_df[
            'recommendation'
        ] == 'Reposição Moderada'
    ]\
    .shape[0]
)

reduce_count = (
    filtered_df[
        filtered_df[
            'recommendation'
        ] == 'Reduzir Compras'
    ]
    .shape[0]
)

healthy_count = (
    filtered_df[
        filtered_df[
            'recommendation'
        ] == 'Estoque Saudável'
    ]
    .shape[0]
)

# Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    'Compra Urgente',
    urgent_count
)

col2.metric(
    'Reposição Moderada',
    moderate_count
)

col3.metric(
    'Reduzir Compras',
    reduce_count
)

col4.metric(
    'Estoque Saudável',
    healthy_count
)

 # Distribuição Recomendações
recommendation_counts = (
    filtered_df['recommendation']
    .value_counts()
    .reset_index()
)

recommendation_counts.columns = [
    'Recomendação',
    'Quantidade'
]

fig = px.bar(
    recommendation_counts,

    x='Quantidade',
    y='Recomendação',

    orientation='h',

    title='Distribuição das Recomendações',

    color='Recomendação',

    color_discrete_map={
        'Compra Urgente': '#ff4d4d',
        'Reposição Moderada': '#fff176',
        'Reduzir Compras': '#64b5f6',
        'Estoque Saudável': '#ba68c8'
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)

## Produtos - Comprar Urgente
urgent_products = (
    filtered_df[
        filtered_df[
            'recommendation'
        ] == 'Compra Urgente'
    ]
)

# tabela 
urgent_table = urgent_products[
    [
        'product_id',
        'product_category_name',
        'prediction',
        'simulated_stock',
        'rupture_risk_pct'
    ]
].copy()

urgent_table = urgent_table.rename(
    columns={
        'product_id': 'ID Produto',
        'product_category_name': 'Categoria',
        'prediction': 'Demanda Prevista',
        'simulated_stock': 'Estoque',
        'rupture_risk_pct': 'Risco (%)'
    }
)

st.subheader(
    '🚨 Produtos com Compra Urgente'
)

urgent_table['Demanda Prevista'] = (
    urgent_table['Demanda Prevista']
    .round(0)
    .astype(int)
)

urgent_table['Estoque'] = (
    urgent_table['Estoque']
    .round(0)
    .astype(int)
)

st.dataframe(
    urgent_table
    .sort_values(
        'Risco (%)',
        ascending=False
    )
    .head(10),

    use_container_width=True
)

# produtos reduzir Compras


reduce_products = (
    filtered_df[
        filtered_df[
            'recommendation'
        ] == 'Reduzir Compras'
    ]
)

reduce_table = reduce_products[
    [
        'product_id',
        'product_category_name',
        'prediction',
        'simulated_stock',
        'overstock_pct'
    ]
].copy()

reduce_table = reduce_table.rename(
    columns={
        'product_id': 'ID Produto',
        'product_category_name': 'Categoria',
        'prediction': 'Demanda Prevista',
        'simulated_stock': 'Estoque',
        'overstock_pct': 'Overstock (%)'
    }
)

st.subheader(
    '📦 Produtos para Redução de Compras'
)
reduce_table['Demanda Prevista'] = (
    reduce_table['Demanda Prevista']
    .round(0)
    .astype(int)
)

reduce_table['Estoque'] = (
    reduce_table['Estoque']
    .round(0)
    .astype(int)
)
st.dataframe(
    reduce_table
    .sort_values(
        'Overstock (%)',
        ascending=False
    )
    .head(10),

    use_container_width=True
)

st.info(
    '''
    O sistema inteligente utiliza:
    
    - previsão de demanda
    - estoque simulado
    - risco de ruptura
    - overstock
    
    para recomendar ações operacionais.
    '''
)