import streamlit as st
from utils.GoogleSheetManager import GoogleSheetManager
import pandas as pd

# Configure a página (chame isso apenas uma vez)
st.set_page_config(
    page_title="teste de galeria",
    page_icon=":material/table:",



)

# Inicializa o gerenciador de Google Sheets
gs_manager = GoogleSheetManager()
url = "https://docs.google.com/spreadsheets/d/1gq1sgOmUDyU5hn5P5BYWzqQ2I8RuB2Al-NzaMYIq-Jg/edit?usp=sharing"

if url:
    gs_manager.set_url(url)
    gs_manager.add_worksheet(url, "EDICOES")
    gs_manager.add_worksheet(url, "CONTROLES")
    gs_manager.add_worksheet(url, "CONSOLES")
    products = gs_manager.read_sheet(url, "EDICOES")
    controles = gs_manager.read_sheet(url, "CONTROLES")
    consoles = gs_manager.read_sheet(url, "CONSOLES")

data = pd.concat([controles, consoles], ignore_index=True)
# Exibição da galeria
cols_per_row = 7




tab1, tab2, tab3, tab5 = st.tabs(["CONSOLES", "CONTROLES", "EDICOES", "TABELAS"])

with tab1:
    # Galeria para "CONSOLES"
    rows = [consoles.iloc[i:i + cols_per_row] for i in range(0, len(consoles), cols_per_row)]
    for row in rows:
        cols = st.columns(cols_per_row)
        for col, (_, item) in zip(cols, row.iterrows()):
            with col:
                st.image(item["IMG"], caption=item["TITLE"], width=100)

with tab2:
    # Galeria para "CONTROLES"
    rows = [controles.iloc[i:i + cols_per_row] for i in range(0, len(controles), cols_per_row)]
    for row in rows:
        cols = st.columns(cols_per_row)
        for col, (_, item) in zip(cols, row.iterrows()):
            with col:
                st.image(item["IMG"], caption=item["TITLE"], width=100)

with tab3:
    # Galeria para "EDICOES"
    rows = [products.iloc[i:i + cols_per_row] for i in range(0, len(products), cols_per_row)]
    for row in rows:
        cols = st.columns(cols_per_row)
        for col, (_, item) in zip(cols, row.iterrows()):
            with col:
                st.image(item["IMG"], caption=item["TITLE"], width=100)

with tab5:
    st.dataframe(
        data,
        column_config={
            "IMG": st.column_config.ImageColumn(
                "Preview", help="Preview da imagem", width='small'
            )
        }, use_container_width=True)

with tab5:
    st.dataframe(
        products,
        column_config={
            "IMG": st.column_config.ImageColumn(
                "Preview", help="Preview da imagem", width='small'
            )
        }, use_container_width=True)
