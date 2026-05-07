"""
1 — Overview
Objetivo

Mostrar visão executiva.

KPIs

✔️ total produtos
✔️ total categorias
✔️ demanda prevista total
✔️ produtos críticos
✔️ produtos overstock
✔️ MAE modelo

Gráficos

✔️ demanda por categoria
✔️ distribuição recomendações
✔️ top categorias críticas

"""

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.load_data import load_inventory

PRIMARY_COLOR = "#50e550"

df = load_inventory()

# titulo
st.title('📊 Overview')

# kpis
total_products = df['product_id'].nunique()

total_categories = (
    df['product_category_name']
    .nunique()
)

total_prediction = (
    df['prediction']
    .sum()
)

critical_products = (
    df[df['rupture_risk_pct'] > 50]
    .shape[0]
)

overstock_products = (
    df[df['overstock_pct'] > 50]
    .shape[0]
)

# Cards
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    'Produtos',
    total_products
)

col2.metric(
    'Categorias',
    total_categories
)

col3.metric(
    'Demanda Prevista',
    round(total_prediction)
)

col4.metric(
    'Risco de Ruptura',
    critical_products
)

col5.metric(
    'Overstock',
    overstock_products
)

# Demanda por Categoria
category_sales = (
    df.groupby(
        'product_category_name'
    )['prediction']
    .sum()
    .sort_values(ascending=True)
    .head(10)
    .reset_index()
)

fig = px.bar(
    category_sales,

    x='prediction',
    y='product_category_name',

    orientation='h',

    title='Top Categorias por Demanda',

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

## Distribuição Recomendações

# Produtos aleatórios
sample_products = (
    df[
        [
            'product_id',
            'product_category_name',
            'recommendation'
        ]
    ]
    .sample(10)
)

# Renomeando colunas
sample_products = sample_products.rename(
    columns={
        'product_id': 'ID Produto',
        'product_category_name': 'Categoria do Produto',
        'recommendation': 'Recomendação'
    }
)

st.subheader(
    '📦 Recomendações Operacionais'
)

# cores
def highlight_recommendation(row):

    recommendation = row['Recomendação']

    if recommendation == 'Compra Urgente':
        return ['background-color: #ff4d4d'] * len(row)

    elif recommendation == 'Reposição Moderada':
        return ['background-color: #fff176'] * len(row)

    elif recommendation == 'Reduzir Compras':
        return ['background-color: #64b5f6'] * len(row)

    else:
        return ['background-color: #ba68c8'] * len(row)

# tabela estilizada
st.dataframe(
    sample_products
    .style
    .apply(
        highlight_recommendation,
        axis=1
    ),
    use_container_width=True
)

