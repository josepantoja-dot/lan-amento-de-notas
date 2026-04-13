import streamlit as st

st.set_page_config(
    page_title="Tutorial SAP - Lançamento de Notas",
    page_icon="📑",
    layout="centered"
)

# --- ESTILIZAÇÃO DA NOTA FISCAL (LAYOUT FIEL AO PDF) ---
nota_fiscal_html = """
<div style="background-color: #fff; padding: 15px; border: 2px solid #000; color: #000; font-family: 'Arial', sans-serif; font-size: 12px; line-height: 1.2;">
    
    <div style="display: flex; border-bottom: 2px solid #000; padding-bottom: 5px;">
        <div style="flex: 1; text-align: center; border-right: 1px solid #000; padding: 5px;">
            <strong style="font-size: 14px;">Prefeitura de Manaus</strong><br>
            Secretaria Municipal de Finanças,<br>Planejamento e Tecnologia da Informação
        </div>
        <div style="flex: 1; text-align: center; border-right: 1px solid #000; padding: 5px;">
            <strong style="font-size: 14px;">NFS-e</strong><br>
            Nota Fiscal de Serviço eletrônica
        </div>
        <div style="flex: 1; text-align: center; padding: 5px;">
            <strong>Número da NFS-e</strong><br>
            <span style="background-color: #e6f2ff; padding: 2px 10px; border: 1px solid #0066cc; font-weight: bold; font-size: 16px;">118</span>
        </div>
    </div>

    <div style="border-bottom: 1px solid #000; padding: 5px; font-size: 10px;">
        <strong>Chave de Acesso da NFS-e</strong><br>
        13026032229631434000171000000000011826043341345615
    </div>

    <div style="border-bottom: 1px solid #000; padding: 5px; background-color: #f2f2f2;">
        <strong>EMITENTE DA NFS-e (Prestador do Serviço)</strong><br>
        Nome / Nome Empresarial: <strong>NOVA ENERGIA SERVICOS E COMERCIO LTDA</strong><br>
        CNPJ/CPF: <span style="background-color: #ffff99; padding: 1px 4px; border: 1px solid #999; font-weight: bold;">29.631.434/0001-71</span> <small>(Use para ME2L)</small>
    </div>

    <div style="border-bottom: 1px solid #000; padding: 5px;">
        <strong>TOMADOR DO SERVIÇO</strong><br>
        Nome / Nome Empresarial: <strong>SOCIEDADE FOGAS LTDA</strong><br>
        CNPJ/CPF: 04.563.672/0001-66
    </div>

    <div style="border-bottom: 1px solid #000; padding: 5px; min-height: 100px;">
        <strong>SERVIÇO PRESTADO</strong><br>
        <p>14.01 - SERVIÇOS DE ENSAIOS EM EPI/EPC E FERRAMENTAS PARA LINHA VIVA.</p>
        <div style="margin-top: 15px; padding: 8px; border: 2px dashed #cc0000; background-color: #ffeeee; color: #cc0000; font-weight: bold; text-align: center;">
            CONFORME PEDIDO DE COMPRA 4500462144 - VENCIMENTO: 29/04/2026.
        </div>
        <p style="font-size: 10px; color: #666; text-align: center;">(🚨 Aprendiz: O número do PC está neste quadro vermelho acima!)</p>
    </div>

    <div style="display: flex; justify-content: flex-end; padding: 10px;">
        <div style="text-align: right;">
            <strong>Valor Líquido da NFS-e:</strong><br>
            <span style="font-size: 18px; font-weight: bold; color: #008000; background-color: #d9f2d9; padding: 2px 10px; border: 1px solid #008000;">R$ 7.280,00</span>
        </div>
    </div>
</div>
<br>
"""

# --- BARRA LATERAL (MENU) ---
st.sidebar.title("📌 Navegação")
etapa = st.sidebar.radio(
    "Selecione a Etapa:",
    ["1. Início e Exemplo de Nota", "2. Localizar PC (ME2L)", "3. Lançamento (MIGO)"]
)

# --- CONTEÚDO PRINCIPAL ---
if etapa == "1. Início e Exemplo de Nota":
    st.title("📦 Etapa 1: Recebimento do Documento")
    st.write("Identifique os dados abaixo na sua nota física para iniciar o processo no SAP.")
    
    # Renderiza a nota técnica igual ao PDF
    st.markdown(nota_fiscal_html, unsafe_allow_html=True)
    
    st.markdown("""
    ### 📝 Pontos de Atenção:
    * **Número da Nota (118):** Fica no topo à direita.
    * **CNPJ Fornecedor:** Use para pesquisar o pedido se ele não estiver impresso.
    * **Descrição do Serviço:** O número do **Pedido (PC)** no padrão da Fogás vem escrito no corpo do texto.
    """)
    
    if st.button("Tudo certo, vamos prosseguir!"):
        st.success("Use o menu lateral para ir à Etapa 2 ou 3.")

elif etapa == "2. Localizar PC (ME2L)":
    st.title("🔍 Etapa 2: Buscar Pedido (ME2L)")
    st.markdown("""
    1. Entre na **ME2L**.
    2. No fornecedor, use o CNPJ: **29.631.434/0001-71**.
    3. Clique no **Relógio**.
    4. O valor do pedido deve ser **R$ 7.280,00**.
    """)

elif etapa == "3. Lançamento (MIGO)":
    st.title("⚙️ Etapa 3: Lançamento (MIGO)")
    st.markdown("""
    1. Digite **MIGO**.
    2. Cole o pedido: **4500462144**.
    3. Nota de Remessa: **118**.
    4. Data: **09/04/2026**.
    5. Clique no **Disquete** para salvar.
    """)
