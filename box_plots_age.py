import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Box Plot Viewer", layout="wide")

# Título do aplicativo
st.title("Visualizador de Box Plot")

# Carregar arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Ler dados do CSV
    df = pd.read_csv(uploaded_file)

    # Verificar se o arquivo tem pelo menos 4 colunas
    if df.shape[1] >= 3:
        # Ajuste do eixo
        y_axis_scale = st.selectbox("Escala do eixo Y", ["linear", "log"])

        # Criar box plot para todas as colunas
        c1, c2, c3 = st.columns([0.5, 1, 0.5])
        with c2:
            fig, ax = plt.subplots()
            
            # Definir paleta de cores
            palette = ["#808080", "#33FF57", "#FF3333", "#FFFF33"]  # Cinza, Verde, Vermelho, Amarelo
            
            sns.boxplot(data=df, ax=ax, palette=palette)
            ax.set_yscale(y_axis_scale)
            ax.set_xlabel('Age groups')
            ax.set_ylim(0,80)
            ax.set_ylabel('Luminance contrast (%)')
            plt.xticks(rotation=0)
            st.pyplot(fig)
    else:
        st.error("O arquivo CSV deve conter pelo menos 3 colunas.")
else:
    st.info("Por favor, carregue um arquivo CSV para começar.")
