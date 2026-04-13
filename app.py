import streamlit as st

# Configuração inicial da página
st.set_page_config(
    page_title="Guia do Aprendiz - Lançamento SAP",
    page_icon="📘",
    layout="centered"
)

# --- MENU LATERAL ---
st.sidebar.title("📌 Navegação")
pagina = st.sidebar.radio(
    "Escolha a etapa:",
    ["1. O Kit de Sobrevivência", 
     "2. A Caça ao Pedido (ME2L)", 
     "3. O Lançamento Final (MIGO)"]
)

st.sidebar.markdown("---")
st.sidebar.info("Dica: Siga as etapas na ordem para não pular nenhuma validação importante.")

# --- PÁGINA 1: RECEBIMENTO ---
if pagina == "1. O Kit de Sobrevivência":
    st.title("📦 Etapa 1: O que você tem em mãos?")
    st.write("Você acabou de receber um Boleto e uma ou mais Notas Fiscais. O primeiro passo é organizar essa documentação.")
    
    st.warning("⚠️ **ALERTA:** Um único boleto pode servir para pagar VÁRIAS notas fiscais. Agrupe os documentos com atenção e valide os valores totais.")
    
    with st.expander("📸 Ver exemplo de Nota e Boleto"):
        # Substitua 'img_1.jpg' pelo caminho da sua imagem real no GitHub
        # st.image('img_1.jpg', caption='Atenção à relação Boleto x Notas')
        st.info("Aqui entrará a Imagem 1 (Ilustrativa de nota e boleto).")

    st.markdown("### Procurando o Pedido de Compras (PC)")
    st.write("Olhe atentamente para a Nota Fiscal impressa. Procure pelo número do **Pedido de Compras (PC)**.")
    
    with st.expander("📸 Onde encontro o PC na nota?"):
        # st.image('img_2.jpg', caption='Zoom na área de Dados Adicionais')
        st.info("Aqui entrará a Imagem 2 (Destaque na nota física).")

    st.success("👉 **Se você ACHOU o PC:** Vá direto para a etapa 3 (MIGO) no menu lateral.\n\n👉 **Se você NÃO ACHOU:** Vá para a etapa 2 (ME2L).")

# --- PÁGINA 2: ME2L ---
elif pagina == "2. A Caça ao Pedido (ME2L)":
    st.title("🔍 Etapa 2: Buscando o PC no SAP")
    st.write("Se o número do pedido não está na nota física, precisaremos investigar no sistema usando a transação **ME2L**.")

    st.markdown("""
    ### Passo a Passo:
    1. Digite **ME2L** na barra inicial do SAP.
    2. Em "Fornecedor", digite o código do fornecedor.
    3. Clique no **Relógio** (Executar).
    4. Encontre o PC mais atual.
    5. Compare os dados (Valor, placa, etc.) com a sua nota física. Bateu? **Copie o número do PC!**
    """)

    st.info("💡 **Dica:** Não sabe o código do fornecedor? Clique na barra branca do campo e pesquise pelo **CNPJ** que está na nota fiscal.")

    st.markdown("### Imagens de Apoio")
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("📸 Onde digitar ME2L e Fornecedor"):
            st.info("Aqui entrarão as Imagens 3 e 4 (Tela de pesquisa e matchcode).")
    
    with col2:
        with st.expander("📸 Botão Relógio e Lista de Pedidos"):
            st.info("Aqui entrarão as Imagens 5 e 6 (Botão executar e tabela de resultados).")

# --- PÁGINA 3: MIGO ---
elif pagina == "3. O Lançamento Final (MIGO)":
    st.title("⚙️ Etapa 3: Conferência e Registro")
    st.write("Agora que você tem o número do Pedido de Compras (PC), vamos fazer o lançamento usando a transação **MIGO**.")

    st.error("🛑 **REGRA DE OURO:** Sempre compare os preços do sistema com a NOTA, nunca com o boleto (pois o boleto já tem os impostos somados).")

    st.markdown("""
    ### Passo a Passo:
    1. Digite **MIGO** na barra inicial.
    2. Cole o número do PC ao lado de "Pedido".
    3. Compare os preços do Pedido (na tela) com os da Nota Fiscal (física). 
    4. Marque a caixinha **"OK"** na linha do item.
    5. Preencha a **Nota de Remessa** (NFS-e) e a **Data do Documento**.
    6. Clique no **Disquete** para salvar.
    """)

    st.markdown("### Imagens de Apoio")
    with st.expander("📸 Inserindo o Pedido na MIGO"):
        st.info("Aqui entrará a Imagem 7 (Tela MIGO e campo de colar o PC).")
    
    with st.expander("📸 Não esqueça da Caixinha OK!"):
        st.info("Aqui entrará a Imagem 8 (Close-up no checkbox OK).")
        
    with st.expander("📸 Dados da Nota e Disquete (Salvar)"):
        st.info("Aqui entrarão as Imagens 9 e 10 (Abas de remessa/data e botão salvar).")
