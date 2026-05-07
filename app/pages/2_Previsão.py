"""
2 — Previsão de Demanda
Objetivo

Visualizar forecasting.

Conteúdo

✔️ séries temporais
✔️ real vs previsto
✔️ filtros por categoria
✔️ filtros por produto

quais categorias possuem maior demanda?
como a previsão evolui?
o modelo acompanha a realidade?
quais produtos possuem maior crescimento?

"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.load_data import load_inventory

PRIMARY_COLOR = "#50e550"

df = load_inventory()

st.title('📈 Previsão de Demanda')

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
    key='previsao_category'
)


# filtros
filtered_df = df.copy()

if selected_category != 'Todas':

    filtered_df = filtered_df[
        filtered_df[
            'product_category_name'
        ] == selected_category
    ]
# kpis

total_prediction = (
    filtered_df['prediction']
    .sum()
)

average_prediction = (
    filtered_df['prediction']
    .mean()
)

total_products = (
    filtered_df['product_id']
    .nunique()
)

# Cards

col1, col2, col3 = st.columns(3)

col1.metric(
    'Demanda Prevista',
    round(total_prediction)
)

col2.metric(
    'Previsão Média',
    round(average_prediction, 2)
)

col3.metric(
    'Produtos',
    total_products
)

# Agregação temporal

time_series = (
    filtered_df.groupby('date')
    [
        ['sales', 'prediction']
    ]
    .sum()
    .reset_index()
)

# grafico

fig = go.Figure()

# Real
fig.add_trace(
    go.Scatter(
        x=time_series['date'],
        y=time_series['sales'],
        mode='lines',
        name='Real'
    )
)

# Previsto

fig.add_trace(
    go.Scatter(
        x=time_series['date'],
        y=time_series['prediction'],
        mode='lines',
        name='Previsto'
    )
)

# 
fig.update_layout(
title='Demanda Real vs Prevista',

xaxis_title='Data',

yaxis_title='Quantidade',

template='plotly_white'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# top categoriaas por previsao
top_categories = (
    filtered_df.groupby(
        'product_category_name'
    )['prediction']
    .sum()
    .sort_values(ascending=True)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_categories,

    x='prediction',
    y='product_category_name',

    orientation='h',

    title='Top Categorias por Previsão',

    labels={
        'prediction': 'Previsão',
        'product_category_name': 'Categoria do Produto'
    },

    color_discrete_sequence=[PRIMARY_COLOR]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# produtos com maior previsao

top_products = (
    filtered_df.groupby(
        [
            'product_id',
            'product_category_name'
        ]
    )['prediction']
    .sum()
    .sort_values(ascending=True)
    .reset_index()
    .head(10)
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

    x='prediction',
    y='Produto',

    orientation='h',

    title='Produtos com Maior Previsão',

    labels={
        'prediction': 'Previsão',
        'Produto': 'Produto'
    },

    color_discrete_sequence=[PRIMARY_COLOR]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# tabela operacional
table_df = filtered_df[
    [
        'product_id',
        'product_category_name',
        'sales',
        'prediction'
    ]
].copy()

table_df = table_df.rename(
    columns={
        'product_id': 'ID Produto',
        'product_category_name': 'Categoria',
        'sales': 'Demanda Real',
        'prediction': 'Previsão'
    }
)

st.subheader(
    '📋 Produtos Monitorados'
)

st.dataframe(
    table_df.head(20),
    use_container_width=True
)