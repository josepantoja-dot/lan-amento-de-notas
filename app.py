import streamlit as st

# Configuração Principal do App
st.set_page_config(
    page_title="Guia SAP - Aprendizes",
    page_icon="🧾",
    layout="centered"
)

# --- ESTILIZAÇÃO VISUAL ---
st.markdown("<h1 style='text-align: center; color: #004A99;'>Guia de Lançamento de Notas - SAP</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Treinamento para Novos Aprendizes</p>", unsafe_allow_html=True)
st.markdown("---")

# --- MENU LATERAL ---
st.sidebar.title("📌 Navegação")
etapa = st.sidebar.radio(
    "Selecione a Etapa:",
    [
        "1. Identificação (Nota Física)",
        "2. Busca de Pedido (ME2L)",
        "3. Lançamento (MIGO)",
        "4. Dicas e Cuidados"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Atenção:** Sempre use a Nota Fiscal como base, nunca o boleto para valores unitários.")

# --- ETAPA 1: IDENTIFICAÇÃO ---
if etapa == "1. Identificação (Nota Física)":
    st.header("📦 Etapa 1: Encontrando os dados na Nota")
    st.write("Analise a imagem abaixo. Ela é o seu ponto de partida.")

    # Carregamento da imagem que você subiu no GitHub
    try:
        st.image("Design sem nome.jpg", caption="Exemplo de NFS-e (Dados Borrados para Segurança)")
    except:
        st.error("⚠️ Erro: O arquivo 'Design sem nome.jpg' não foi encontrado. Verifique se o nome no GitHub está exatamente igual (incluindo maiúsculas).")

    st.markdown("""
    ### 📝 O que você deve anotar desta nota:
    * **Número da Nota:** Localizado no topo (Ex: **120**).
    * **Pedido de Compra (PC):** Nesta nota, ele está no texto da descrição: **4500468106**.
    * **Valor Líquido:** O valor total a ser conferido: **R$ 590,33**.
    * **Fornecedor:** Se precisar buscar na ME2L, use o CNPJ (Ex: **12.345.678/0001-90**).
    """)
    
    if st.button("Já encontrei os dados! Ir para o próximo passo"):
        st.success("Excelente! Use o menu lateral para ir à Etapa 3 (MIGO).")

# --- ETAPA 2: ME2L ---
elif etapa == "2. Busca de Pedido (ME2L)":
    st.header("🔍 Etapa 2: Quando o PC não está na nota")
    st.write("Se o número 4500... não estivesse escrito, você faria o seguinte:")
    
    st.markdown("""
    1.  No SAP, acesse a transação **ME2L**.
    2.  No campo **Fornecedor**, digite o CNPJ: `12.345.678/0001-90`.
    3.  Clique no ícone do **Relógio** (ou aperte F8).
    4.  Procure o pedido que tem o valor líquido de **R$ 590,33**.
    5.  Anote o número do Pedido de Compras.
    """)

# --- ETAPA 3: MIGO ---
elif etapa == "3. Lançamento (MIGO)":
    st.header("⚙️ Etapa 3: Lançamento no SAP")
    st.write("Com o número **4500468106** em mãos, siga estes passos:")
