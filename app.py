import streamlit as st

st.set_page_config(
    page_title="Tutorial SAP - Lançamento de Notas",
    page_icon="📑",
    layout="centered"
)

# --- ESTILIZAÇÃO DA NOTA FISCAL ---
# ATENÇÃO: As linhas abaixo estão sem espaço no começo de propósito 
# para o Streamlit não transformar em bloco de texto/código.
nota_fiscal_html = """
<div style="background-color: #ffffff; padding: 20px; border: 1px solid #cccccc; border-radius: 8px; color: #000000; font-family: Arial, sans-serif; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
<h3 style="text-align: center; margin-top: 0; color: #333333;">PREFEITURA DE MANAUS<br><span style="font-size: 16px; font-weight: normal;">Nota Fiscal de Serviço Eletrônica (NFS-e)</span></h3>
<hr style="border-top: 1px solid #eeeeee;">
<p><strong>Número da NFS-e:</strong> <span style="background-color: #e6f2ff; padding: 2px 6px; border: 1px solid #0066cc; font-weight: bold;">118</span> &nbsp;&nbsp;&nbsp; <strong>Data de Emissão:</strong> <span style="background-color: #e6f2ff; padding: 2px 6px; border: 1px solid #0066cc; font-weight: bold;">09/04/2026</span></p>
<hr style="border-top: 1px solid #eeeeee;">
<p><strong>PRESTADOR DO SERVIÇO (FORNECEDOR)</strong><br>
CNPJ: <span style="background-color: #ffff99; padding: 2px 6px; border: 1px solid #cccc00; font-weight: bold;">99.999.999/0001-99</span> <em>(Use este CNPJ na ME2L)</em><br>
Nome: EMPRESA FORNECEDORA DE EXEMPLO LTDA</p>
<hr style="border-top: 1px solid #eeeeee;">
<p><strong>TOMADOR DO SERVIÇO</strong><br>
CNPJ: 04.563.672/0001-66<br>
Nome: SOCIEDADE FOGAS LTDA</p>
<hr style="border-top: 1px solid #eeeeee;">
<p><strong>DESCRIÇÃO DO SERVIÇO</strong></p>
<div style="background-color: #f9f9f9; padding: 15px; border: 1px solid #dddddd; border-radius: 5px;">
14.01 SERVIÇO (ENSAIOS EM EPI/EPC...)<br><br>
<span style="background-color: #ffcccc; color: #cc0000; font-weight: bold; padding: 4px 8px; border: 1px dashed #cc0000;">CONFORME PEDIDO DE COMPRA 4500462144-VENCIMENTO: 29/04/2026.</span><br>
<br><em>(🚨 <strong>Atenção Aprendiz:</strong> O número do PC está escondido no meio do texto!)</em>
</div>
<hr style="border-top: 1px solid #eeeeee;">
<p style="text-align: right; font-size: 18px; margin-bottom: 0;"><strong>VALOR TOTAL DA NFS-e:</strong> <span style="background-color: #d9f2d9; padding: 4px 8px; border: 1px solid #339933; font-weight: bold;">R$ 7.280,00</span></p>
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
    st.write("O primeiro passo é identificar as informações cruciais na Nota Fiscal que você recebeu.")
    
    st.info("💡 **Dica:** Veja o exemplo abaixo para aprender onde cada informação fica na nota.")
    
    # Renderiza a nota fiscal (agora vai desenhar certo!)
    st.markdown(nota_fiscal_html, unsafe_allow_html=True)
    
    st.markdown("""
    ### 📝 O que conferir na imagem acima:
    * **Azul:** Número e Data da nota (Usaremos na MIGO).
    * **Amarelo:** CNPJ do fornecedor (Usaremos na ME2L caso não ache o pedido).
    * **Vermelho:** O Número do Pedido (PC). Note que nas notas de serviço, ele costuma ficar misturado na descrição!
    * **Verde:** O Valor Total que deve bater com o SAP.
    """)
    
    if st.button("Entendi! Vamos para o próximo passo"):
        st.success("Perfeito! Escolha o próximo passo no menu lateral.")

elif etapa == "2. Localizar PC (ME2L)":
    st.title("🔍 Etapa 2: Buscar Pedido no SAP (ME2L)")
    st.write("Se a nota física **não** trouxer o número do pedido impresso, faça o seguinte no SAP:")
    
    st.markdown("""
    1. Digite a transação **ME2L**.
    2. No campo **Fornecedor**, coloque o código dele.
       - *Sem código? Clique na busca e cole o **CNPJ** (destaque amarelo da etapa 1).*
    3. Clique no ícone do **Relógio** (Executar).
    4. Procure o pedido que bata com o valor da nota (ex: **R$ 7.280,00**).
    5. Copie o número do pedido.
    """)

elif etapa == "3. Lançamento (MIGO)":
    st.title("⚙️ Etapa 3: Lançamento MIGO")
    st.write("Com o número do PC em mãos, vamos registrar a nota.")
    
    st.error("⚠️ **Regra de Ouro:** Confira o valor da NOTA. O boleto pode ter um valor diferente por causa dos impostos, não o use para conferência.")
    
    st.markdown("""
    ### Passo a passo no SAP:
    1. Digite **MIGO**.
    2. Cole o número do PC no campo **Pedido**.
    3. Marque a caixa **OK** na linha do item.
    4. Preencha:
       - **Nota de Remessa:** O número da nota (ex: 118).
       - **Data do Doc:** A data de emissão (ex: 09/04/2026).
    5. Clique no ícone do **Disquete** (Salvar).
    """)
