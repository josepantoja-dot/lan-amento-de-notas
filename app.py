import streamlit as st

st.set_page_config(
    page_title="Tutorial SAP - Lançamento de Notas",
    page_icon="📑",
    layout="centered"
)

# Estilo para a tarja preta
tarja = '<span style="background-color:black; color:black; border-radius:2px;">CENSURADO_DADO_CONFIDENCIAL</span>'

# --- ESTILIZAÇÃO DA NOTA FISCAL (LAYOUT FIEL AO PDF COM TARJAS) ---
nota_fiscal_html = f"""
<div style="background-color:#fff;padding:10px;border:2px solid #000;color:#000;font-family:'Arial',sans-serif;font-size:11px;line-height:1.2;">
<div style="display:flex;border-bottom:2px solid #000;">
<div style="flex:1;text-align:center;border-right:1px solid #000;padding:5px;">
<strong style="font-size:12px;">Prefeitura de Manaus</strong><br>Secretaria Municipal de Finanças,<br>Planejamento e Tecnologia da Informação
</div>
<div style="flex:1;text-align:center;border-right:1px solid #000;padding:5px;">
<strong style="font-size:14px;">NFS-e</strong><br>Nota Fiscal de Serviço eletrônica
</div>
<div style="flex:1;text-align:center;padding:5px;">
<strong>Número da NFS-e</strong><br>
<span style="background-color:#e6f2ff;padding:2px 10px;border:1px solid #0066cc;font-weight:bold;font-size:16px;">118</span>
</div>
</div>
<div style="border-bottom:1px solid #000;padding:5px;font-size:9px;">
<strong>Chave de Acesso da NFS-e</strong><br>13026032229631434000171000000000011826043341345615
</div>
<div style="border-bottom:1px solid #000;padding:5px;background-color:#f9f9f9;">
<strong>EMITENTE DA NFS-e (Prestador do Serviço)</strong><br>
Nome/Razão Social: {tarja}<br>
CNPJ/CPF: {tarja}<br>
Endereço: {tarja}
</div>
<div style="border-bottom:1px solid #000;padding:5px;">
<strong>TOMADOR DO SERVIÇO</strong><br>
Nome/Razão Social: {tarja}<br>
CNPJ/CPF: {tarja}<br>
Endereço: {tarja}
</div>
<div style="border-bottom:1px solid #000;padding:5px;min-height:120px;">
<strong>SERVIÇO PRESTADO</strong><br>
<p>14.01 - SERVIÇOS DE ENSAIOS EM EPI/EPC E FERRAMENTAS PARA LINHA VIVA.</p>
<div style="margin-top:20px;padding:10px;border:2px dashed #cc0000;background-color:#ffeeee;color:#cc0000;font-weight:bold;text-align:center;font-size:14px;">
CONFORME PEDIDO DE COMPRA 4500462144 - VENCIMENTO: 29/04/2026.
</div>
<p style="font-size:10px;color:#666;text-align:center;margin-top:5px;">(🚨 Aprendiz: O número do PC está neste quadro vermelho acima!)</p>
</div>
<div style="display:flex;justify-content:space-between;border-bottom:1px solid #000;padding:5px;">
<div><strong>Município de Incidência:</strong> Manaus - AM</div>
<div><strong>Alíquota:</strong> 5,00%</div>
</div>
<div style="display:flex;justify-content:flex-end;padding:10px;">
<div style="text-align:right;">
<strong>Valor Líquido da NFS-e:</strong><br>
<span style="font-size:20px;font-weight:bold;color:#008000;background-color:#d9f2d9;padding:2px 12px;border:1px solid #008000;">R$ 7.280,00</span>
</div>
</div>
</div>
<br>
"""

# --- BARRA LATERAL ---
st.sidebar.title("📌 Navegação")
etapa = st.sidebar.radio("Selecione a Etapa:", ["1. Identificação (Nota)", "2. Busca no SAP (ME2L)", "3. Lançamento (MIGO)"])

# --- CONTEÚDO ---
if etapa == "1. Identificação (Nota)":
    st.title("📦 Etapa 1: Analisando o Documento")
    st.write("Abaixo está o modelo da nota que você recebeu, com as informações sensíveis ocultadas:")
    st.markdown(nota_fiscal_html, unsafe_allow_html=True)
    st.markdown("""
    ### 📝 O que você precisa extrair:
    1. **Número da NFS-e:** 118 (Topo direito).
    2. **Pedido de Compra (PC):** 4500462144 (Dentro da descrição do serviço).
    3. **Valor Líquido:** R$ 7.280,00.
    """)

elif etapa == "2. Busca no SAP (ME2L)":
    st.title("🔍 Etapa 2: Localizar PC")
    st.write("Caso o PC não estivesse na descrição, você usaria o CNPJ do fornecedor (que está sob a tarja amarela na nota real) para buscar na transação **ME2L**.")

elif etapa == "3. Lançamento (MIGO)":
    st.title("⚙️ Etapa 3: Registro")
    st.write("Use os dados identificados na Etapa 1 para preencher os campos de Pedido, Nota de Remessa e Data no SAP.")
    
