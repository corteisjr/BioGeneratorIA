import streamlit as st
from decouple import config
import requests


# Config
API_KEY = st.secrets["OPENROUTER_API_KEY"] or config("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "X-Title": "BioGeneratorIA",  
}

# Função de geração de bio
def gerar_bio(nome, ocupacao, interesses, estilo):
    prompt = (
        f"Crie uma biografia curta e criativa para {nome}, "
        f"que é {ocupacao}, gosta de {interesses} e quer quea biografia seja num estilo {estilo}. "
        "Use até 150 caracteres. Seja original e atraente e use emojis."
    )
    
    data = {
       "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200,
    }

    response = requests.post(BASE_URL, headers=HEADERS, json=data)

    if response.status_code == 200:
        content = response.json()
        try:
            choices = content.get("choices", [])
            message = choices[0].get("message", {}) if choices else {}
            bio = message.get("content", "").strip()
            if not bio:
                st.error("A resposta da IA veio vazia ou incompleta. Veja detalhes abaixo.")
                return None
            return bio
        except Exception as e:
            st.error(f"Erro ao processar resposta: {e}")
            st.write(content)
            return None

# UI
st.set_page_config(page_title="Gerador de Bio com IA", page_icon="✨", layout="centered")
st.title("✨ Gerador de Biografia com IA")
st.markdown("Crie bios criativas para Instagram, LinkedIn ou outras redes sociais.")

nome = st.text_input("Seu nome ou apelido")
ocupacao = st.text_input("Sua profissão ou ocupação atual")
interesses = st.text_input("Seus interesses (ex: viagens, programação, arte)")
estilo = st.selectbox("Estilo da bio", ["Profissional", "Engraçado", "Inspirador", "Descontraído", "Minimalista"])

if st.button("Gerar Bio"):
    if nome and ocupacao:
        with st.spinner("Gerando sua bio com IA..."):
            bio = gerar_bio(nome, ocupacao, interesses, estilo)
            if bio:
                st.success("Aqui está sua bio:")
                st.code(bio, language="markdown",  height=150, wrap_lines=True)
    else:
        st.warning("Preencha pelo menos o nome e a ocupação.")

st.markdown("---")
st.caption("Feito com ❤️ por Corteis", unsafe_allow_html=True)
