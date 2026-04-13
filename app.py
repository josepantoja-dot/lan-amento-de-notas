import streamlit as st

st.set_page_config(
    page_title="Tutorial SAP - Lançamento de Notas",
    page_icon="📑",
    layout="centered"
)

# --- ESTILIZAÇÃO DA NOTA FISCAL (COM BARRAS PRETAS E NOVO LAYOUT) ---
nota_fiscal_html = """
<div style="background-color:#fff;padding:10px;border:2px solid #000;color:#000;font-family:'Arial',sans-serif;font-size:11px;line-height:1.2;">
<div style="display:flex;border-bottom:2px solid #000;padding-bottom:5px;">
<div style="flex:1;text-align:center;border-right:1px solid #000;padding:5px;">
<strong style="font-size:12px;">Prefeitura de Manaus</strong><br>Secretaria Municipal de Finanças,<br>Planejamento e Tecnologia da Informação
</div>
<div style="flex:1;text-align:center;border-right:1px solid #000;padding:5px;">
<strong style="font-size:14px;">NFS-e</strong><br>Nota Fiscal de Serviço eletrônica
</div>
<div style="flex:1;text-align:center;padding:5px;">
<strong>Número da NFS-e</strong><br>
<span style="background-color:#e6f2ff;padding:2px 10px;border:1px solid #0066cc;font-weight:bold;font-size:16px;">120</span>
</div>
</div>
<div style="border-bottom:1px solid #000;padding:5px;font-size:9px;">
<strong>Chave de Acesso da NFS-e</strong><br>13026032204412953000118000000000012026049321784731
</div>
<div style="border-bottom:1px solid #000;padding:5px;background-color:#f9f9f9;">
<strong>EMITENTE DA NFS-e (Prestador do Serviço)</strong><br>
Nome / Nome Empresarial: <span style="background-color:#000;color:#000;">██████████████████████████████████</span><br>
CNPJ/CPF: <span style="background-color:#ffff99;padding:1px 4px;border:1px solid #999;font-weight:bold;">12.345.678/0001-90</span> <small>(Use para ME2L)</small><br>
Endereço: <span style="background-color:#000;color:#000;">████████████████████████████████████████████████████</span>
</div>
<div style="border-bottom:1px solid #000;padding:5px;">
<strong>TOMADOR DO SERVIÇO</strong><br>
Nome / Nome Empresarial: <span style="background-color:#000;color:#000;">██████████████████████████████████</span><br>
CNPJ/CPF: 10.987.654/0001-21<br>
Endereço: <span style="background-color:#000;color:#000;">████████████████████████████████████████████████████</span>
</div>
<div style="border-bottom:1px solid #000;padding:5px;min-height:100px;">
<strong>SERVIÇO PRESTADO</strong><br>
<p>1 SERVICO USINAGEM. 650,00 Desconto: 32,50<br><br>
01-POLIA FERRO FUNDIDO 100MM SOLICITANTE: ALDAIR 
<span style="background-color:#ffcccc;color:#cc0000;border:3px solid #cc0000;padding:2px 6px;font-weight:bold;font-size:14px;">PC 4500468106</span>
</p>
<p style="font-size:10px;color:#666;text-align:center;margin-top:15px;">(🚨 Aprendiz: O número do PC está destacado em vermelho no meio do texto!)</p>
</div>
<div style="display:flex;justify-content:flex-end;padding:10px;">
<div style="text-align:right;">
<strong>Valor Líquido da NFS-e:</strong><br>
<span style="font-size:20px;font-weight:bold;color:#008000;background-color:#d9f2d9;padding:2px 12px;border:1px solid #008000;">R$ 590,33</span>
</div>
</div>
</div>
<br>
"""

# --- BARRA LATERAL ---
st.sidebar.title("📌 Navegação")
etapa = st.sidebar.radio(
    "Selecione a Etapa:", 
    ["1. Identificação (Nota)", "2. Busca no SAP (ME2L)", "3. Lançamento (MIGO)"]
)

# --- CONTEÚDO ---
if etapa == "1. Identificação (Nota)":
    st.title("📦 Etapa 1: Analisando o Documento")
    st.write("Abaixo está uma nota real anonimizada. Identifique os dados destacados para iniciar o processo.")
    
    st.markdown(nota_fiscal_html, unsafe_allow_html=True)
    
    st.markdown("""
    ### 📝 O que você precisa extrair:
    1. **Número da NFS-e:** 120 (Destaque Azul).
    2. **Pedido de Compra (PC):** 4500468106 (Destaque Vermelho).
    3. **Valor Líquido:** R$ 590,33 (Destaque Verde).
    4. **CNPJ do Fornecedor:** 12.345.678/0001-90 (Destaque Amarelo - *Apenas se precisar da ME2L*).
    """)

elif etapa == "2. Busca no SAP (ME2L)":
    st.title("🔍 Etapa 2: Localizar PC (ME2L)")
    st.write("Se o PC não estivesse escrito na nota, você precisaria buscar no SAP.")
    st.markdown("""
    1. Digite a transação **ME2L**.
    2. No campo fornecedor, digite o CNPJ da nota: **12.345.678/0001-90**.
    3. Clique no **Relógio** (Executar).
    4. Busque na lista um pedido com o valor exato de **R$ 590,33**.
    """)

elif etapa == "3. Lançamento (MIGO)":
    st.title("⚙️ Etapa 3: Registro (MIGO)")
    st.write("Com os dados da Etapa 1 em mãos, faça o lançamento final:")
    st.markdown("""
    1. Acesse a transação **MIGO**.
    2. Insira o Pedido: **4500468106**.
    3. Marque a caixa **OK** na linha do material.
    4. Preencha a Nota de Remessa: **120**.
    5. Preencha a Data do Documento (ver topo da nota).
    6. Clique no **Disquete** para salvar.
    """)
