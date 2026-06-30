import csv
import os

def carregar_base_conhecimento(caminho_arquivo):
    """Lê o arquivo CSV e transforma em um texto para a IA entender (RAG)."""
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Erro: Arquivo base_ncm.csv não encontrado."

def simular_agente_ia(pergunta, contexto_dados):
    """Simula o comportamento de uma LLM com regras estritas (System Prompt)."""
    
    pergunta_lower = pergunta.lower()
    
    # Regra 3: Se não estiver na base, não alucinar.
    if "smartphones" not in pergunta_lower and "notebooks" not in pergunta_lower and "videogame" not in pergunta_lower:
        return "Desculpe, não tenho informações sobre este item na minha base de dados atual."
    
    # Simulando a extração de dados da base baseada na pergunta
    if "smartphones" in pergunta_lower:
        return "Com base na NCM 8517.13.00 (Smartphones), a alíquota de II é 16% e IPI é 15%."
    elif "notebooks" in pergunta_lower:
        return "Com base na NCM 8471.30.12 (Notebooks), a alíquota de II é 16% e IPI é 0%."
    elif "videogame" in pergunta_lower:
        return "Com base na NCM 9504.50.00 (Consoles de Videogame), a alíquota de II é 16% e IPI é 30%."

def iniciar_chat():
    print("="*50)
    print("🤖 Assistente de Importação Zetta (AII) Iniciado")
    print("="*50)
    
    # Ajustando o caminho para rodar corretamente independentemente de onde o terminal for aberto
    caminho_csv = os.path.join(os.path.dirname(__file__), '..', 'data', 'base_ncm.csv')
    base_dados = carregar_base_conhecimento(caminho_csv)
    
    while True:
        usuario = input("\nVocê (Digite 'sair' para encerrar): ")
        if usuario.lower() == 'sair':
            print("Encerrando assistente...")
            break
            
        print("AII processando dados da base NCM...")
        resposta = simular_agente_ia(usuario, base_dados)
        print(f"🤖 AII Zetta: {resposta}")

if __name__ == "__main__":
    iniciar_chat()
