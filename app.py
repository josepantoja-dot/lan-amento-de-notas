import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Tutorial SAP - Lançamento de Notas",
    page_icon="📑",
    layout="centered"
)

# --- ESTILIZAÇÃO DA NOTA FISCAL (HTML/CSS) ---
nota_fiscal_html = """
<div style="background-color: white; padding: 20px; border: 2px solid #333; border-radius: 10px; color: #333; font-family: 'Courier New', Courier, monospace; line-height: 1.2; box-shadow: 5px 5px 15px rgba(0,0,0,0.2);">
    <div style="text-align: center; border-bottom: 2px solid #333; margin-bottom: 10px;">
        <h2 style="margin: 0; font-size: 1.2em;">PREFEITURA DE MANAUS</h2>
        <h3 style="margin: 0; font-size: 1em;">NOTA FISCAL DE SERVIÇO ELETRÔNICA (NFS-e)</h3>
    </div>
    
    <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
        <div><strong>Número da NFS-e:</strong> <span style="background-color: #e6f2ff; padding: 2px 5px; border: 1px solid #0066cc; font-weight: bold;">999</span></div>
        <div><strong>Data de Emissão:</strong> <span style="background-color: #e6f2ff; padding: 2px 5px; border: 1px solid #0066cc; font-weight: bold;">13/04/2026</span></div>
    </div>

    <div style="border: 1px solid #666; padding: 10px; margin-bottom: 10px; background-color: #fcfcfc;">
        <strong>PRESTADOR DO SERVIÇO (FORNECEDOR)</strong><br>
        Nome: EMPRESA DE MANUTENÇÃO EXEMPLO LTDA<br>
        CNPJ: <span style="background-color: #ffff99; padding: 2px 5px; font-weight: bold; border: 1px solid #999;">99.999.999/0001-99</span> <em>(CÓDIGO P/ ME2L)</em>
    </div>

    <div style="border: 1px solid #666; padding: 10px; margin-bottom: 10px;">
        <strong>TOMADOR DO SERVIÇO</strong><br>
        Nome: SUA EMPRESA LTDA<br>
        Endereço: Rua de Exemplo, Manaus - AM
    </div>

    <div style="border: 1px solid #666; padding: 10px; height: 120px; background-color: #fff;">
        <strong>DESCRIÇÃO DOS SERVIÇOS</strong><br><br>
        SERVIÇO DE MANUTENÇÃO ELÉTRICA EM GRUPO GERADOR.<br>
        <div style="margin-top: 10px; color: #cc0000; font-weight: bold; border: 2px dashed #cc0000; padding: 5px; background-color: #ffeeee; text-align: center;">
            CONFORME PEDIDO DE COMPRA 4500001234 - VENCIMENTO: 29/04/2026.
        </div>
        <small style="color: #666;">(🚨 Aprendiz: O número do PC para a MIGO está no quadro acima!)</small>
    </div>

    <div style="margin-top: 10px; text-align: right;">
        <span style="font-size: 1.2em; font-weight: bold;">VALOR TOTAL DA NOTA: </span>
        <span style="background-color: #ccffcc; padding: 5px 10px; border: 1px solid #009900; font-size: 1.2em;">R$ 5.000,00</span>
    </div>
</div>
"""

# --- BARRA LATERAL (MENU) ---
st.sidebar.title("Navegação")
etapa = st.sidebar.radio(
    "Selecione a Etapa:",
    ["1. Início e Exemplo de Nota", "2. Localizar PC (ME2L)", "3. Lançamento (MIGO)"]
)

# --- CONTEÚDO PRINCIPAL ---

if etapa == "1. Início e Exemplo de Nota":
    st.title("📦 Etapa 1: Recebimento do Documento")
    st.write("Bem-vindo! O primeiro passo é identificar as informações chave na Nota Fiscal que você recebeu.")
    
    st.info("💡 **Dica:** Use o exemplo interativo abaixo para aprender onde cada informação fica na nota padrão de Manaus.")
    
    # Exibe a Nota Fiscal "Visual"
    st.markdown(nota_fiscal_html, unsafe_allow_html=True)
    
    st.markdown("""
    ### 📝 O que conferir agora:
    1. **Número da NFS-e:** Destaque em Azul (Topo).
    2. **CNPJ do Fornecedor:** Destaque em Amarelo (Se precisar buscar o PC no SAP).
    3. **Número do Pedido (PC):** Destaque em Vermelho (Dentro da Descrição do Serviço).
    4. **Valor Total:** Destaque em Verde.
    """)
    
    if st.button("Já achei o número do PC na minha nota"):
        st.balloons()
        st.success("Ótimo! Agora pule para a etapa **3. Lançamento (MIGO)** no menu lateral.")

elif etapa == "2. Localizar PC (ME2L)":
    st.title("🔍 Etapa 2: Buscar Pedido no SAP (ME2L)")
    st.write("Se a nota física **não** trouxer o número do pedido impresso, siga estes passos:")
    
    st.markdown("""
    1. No SAP, digite a transação **ME2L**.
    2. No campo **Fornecedor**, digite o código dele.
       - *Dica: Se não souber o código, clique na busca e coloque o **CNPJ** que você viu na nota (destaque amarelo).*
    3. Clique no ícone do **Relógio** (Executar).
    4. Procure o pedido mais recente que tenha o valor de **R$ 5.000,00** (ou o valor da sua nota).
    5. Copie o número do pedido (ex: 4500001234).
    """)

elif etapa == "3. Lançamento (MIGO)":
    st.title("⚙️ Etapa 3: Lançamento MIGO")
    st.write("Com o número do PC em mãos, vamos finalizar o processo.")
    
    st.error("⚠️ **Atenção:** Confira o valor da NOTA. Não use o valor do boleto para bater com o SAP.")
    
    st.markdown("""
    ### No SAP (MIGO):
    1. Digite **MIGO** na barra de pesquisa.
    2. Cole o número do Pedido no campo **Pedido**.
    3. Na lista que aparecer, marque a coluna **OK**.
    4. Preencha os campos:
       - **Nota de Remessa:** Coloque o número da nota (ex: 999).
       - **Data do Doc:** Coloque a data da nota (ex: 13/04/2026).
    5. Clique no ícone do **Disquete** (Salvar) na barra superior.
    """)
    st.success("✅ Processo concluído! O sistema gerará um número de documento contábil.")
