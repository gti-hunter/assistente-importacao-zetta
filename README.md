# assistente-importacao-zetta

# 🤖 Assistente de Inteligência de Importação (AII)
**Projeto Zetta Tecnologia e Soluções**

Este projeto foi desenvolvido como entrega para o Lab "Construa Seu Assistente Virtual Com Inteligência Artificial" da DIO, estruturado nos 6 passos metodológicos da criação de agentes.

## 1. Documentação do Agente
- **Nome:** Assistente de Inteligência de Importação (AII)
- **Objetivo:** Auxiliar a área de Comex na consulta rápida e precisa de tributos de importação, cruzando descrições de produtos com a base aduaneira.
- **Público-Alvo:** Analistas de Importação e Despachantes.
- **Restrições Éticas e Técnicas:** O agente é estritamente proibido de calcular impostos com base em estimativas de internet. Ele deve consultar exclusivamente a base de dados em CSV fornecida. Se o produto não constar na base, ele deve obrigatoriamente informar a ausência de dados, evitando alucinações.

## 2. Base de Conhecimento (RAG)
Foi construída uma base de dados local (`data/base_ncm.csv`) simulando uma tabela aduaneira simplificada.
Ela contém os campos: `NCM`, `Descricao`, `II_Porcentagem` e `IPI_Porcentagem`. Esta base atua como a única fonte de verdade do agente.

## 3. Prompts do Agente
O comportamento da IA foi desenhado com o seguinte System Prompt (Instrução de Sistema):
> "Você é um assistente especialista em comércio exterior da Zetta Tecnologia e Soluções. Sua função é responder dúvidas sobre tributação.
> REGRAS:
> 1. Use APENAS a base de dados fornecida.
> 2. O rigor matemático é essencial. Não arredonde ou deduza valores.
> 3. Se o produto não constar na base, responda EXATAMENTE: 'Desculpe, não tenho informações sobre este item na minha base de dados atual.'"

## 4. Aplicação Funcional
O projeto foi desenvolvido em **Python** (`src/assistente.py`). O script carrega o arquivo `.csv`, lê a entrada do usuário via terminal e simula a engine de inferência baseada nas regras do System Prompt e nos dados estruturados. O laço de repetição (`while True`) mantém a conversa ativa até o usuário digitar "sair".

## 5. Avaliação e Métricas
O assistente foi avaliado com testes de mesa para validar a segurança das informações:
- **Cenário de Sucesso:** - *Input:* "Qual o imposto de um videogame?" 
  - *Output:* Retornou corretamente 16% de II e 30% de IPI. (✅ Aprovado)
- **Cenário de Segurança (Anti-Alucinação):** - *Input:* "Qual a taxa para importar camisetas?" 
  - *Output:* "Desculpe, não tenho informações sobre este item na minha base de dados atual." (✅ Aprovado - O agente não inventou uma NCM falsa).

## 6. Pitch Final
**O Problema:** A classificação fiscal e consulta de tributos em planilhas gigantescas geram gargalos e erros operacionais na cotação de mercadorias importadas.
**A Solução:** O AII (Assistente de Inteligência de Importação) automatiza essa busca através de linguagem natural, utilizando uma base de dados controlada (RAG) para garantir 100% de precisão.
**O Valor para a Empresa:** A **Zetta Tecnologia e Soluções** ganha escalabilidade e segurança. Tarefas de consulta que levavam minutos em busca de linhas no Excel agora são respondidas instantaneamente, sem risco de alucinações fiscais.
