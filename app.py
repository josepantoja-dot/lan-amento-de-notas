import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Guia SAP - Lançamento de Notas",
    page_icon="📑",
    layout="centered"
)

# --- ESTILIZAÇÃO DO TÍTULO ---
st.markdown("<h1 style='text-align: center; color: #004A99;'>Guia de Lançamento de Notas - SAP</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Tutorial Passo a Passo para Aprendizes</p>", unsafe_allow_html=True)
st.markdown("---")

# --- MENU LATERAL ---
st.sidebar.title("📌 Navegação")
etapa = st.sidebar.radio(
    "Selecione a Etapa:",
    [
        "1. Identificação (Nota Física)",
        "2. Busca de Pedido (ME2L)",
        "3. Lançamento (MIGO)",
        "4. Resumo e Dicas"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Dica:** A informação mais importante é o número do Pedido de Compras (PC).")

# --- CONTEÚDO DAS ETAPAS ---

if etapa == "1. Identificação (Nota Física)":
    st.header("📦 Etapa 1: Encontrar os dados na Nota")
    st.write("Analise a nota fiscal abaixo. É nela que estão os dados necessários para o SAP.")

    # Tentativa de carregar a imagem renomeada
    try:
        st.image("nota.jpg", caption="Modelo de NFS-e (Dados Borrados para Segurança)")
    except:
        st.error("⚠️ Erro: O ficheiro 'nota.jpg' não foi encontrado no GitHub. Certifica-te de que o ficheiro foi renomeado e enviado corretamente.")

    st.markdown("""
    ### 📝 O que deves anotar desta nota:
    1. **Número da NFS-e:** Localizado no topo (Ex: **120**).
    2. **Pedido de Compra (PC):** Nesta nota, ele está no texto da descrição: **4500468106**.
    3. **Valor Líquido:** O valor total a ser conferido no sistema: **R$ 590,33**.
    """)
    
    if st.button("Já anotei os dados!"):
        st.balloons()
        st.success("Boa! Agora utiliza o menu lateral para ir à Etapa 3 (MIGO).")

elif etapa == "2. Busca de Pedido (ME2L)":
    st.header("🔍 Etapa 2: Se o PC não estiver na Nota")
    st.write("Se não encontrares o número 4500... escrito na descrição, segue estes passos no SAP:")
    
    st.markdown("""
    1.  No SAP, acede à transação **ME2L**.
    2.  No campo **Fornecedor**, digita o CNPJ do prestador (Ex: `12.345.678/0001-90`).
    3.  Clica no ícone do **Relógio** (Executar).
    4.  Procura na lista o pedido que tem o valor de **R$ 590,33**.
    5.  Copia o número do Pedido de Compras encontrado.
    """)

elif etapa == "3. Lançamento (MIGO)":
    st.header("⚙️ Et
