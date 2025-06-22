# BioGeneratorIA ✨

Um gerador de biografias criativas para redes sociais usando IA!

## Descrição

O **BioGeneratorIA** é uma aplicação web feita com [Streamlit](https://streamlit.io/) que utiliza modelos de linguagem avançados para criar bios originais e personalizadas para Instagram, LinkedIn, Twitter e outras redes sociais. Basta informar seu nome, profissão, interesses e escolher um estilo — a IA faz o resto!

## Funcionalidades

- Geração automática de biografias curtas e criativas
- Vários estilos: Profissional, Engraçado, Inspirador, Descontraído e Minimalista
- Uso de emojis e linguagem envolvente
- Interface simples e intuitiva

## Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/BioGeneratorIA.git
   cd BioGeneratorIA
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure sua chave de API:**
   - Crie um arquivo `.env` ou `.streamlit/secrets.toml` e adicione sua chave da OpenRouter:
     ```
     OPENROUTER_API_KEY="sua-chave-aqui"
     ```

4. **Execute o app:**
   ```bash
   streamlit run app.py
   ```

5. **Acesse no navegador:**  
   Normalmente em [http://localhost:8501](http://localhost:8501)

## Exemplo de uso

Preencha os campos com seu nome, profissão, interesses e escolha um estilo. Clique em "Gerar Bio" e copie sua nova biografia!

## Tecnologias

- Python 3.12+
- Streamlit
- OpenRouter API (ou OpenAI API)
- Requests


Feito com ❤️ por Corteis Jr.