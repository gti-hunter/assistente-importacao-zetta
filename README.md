# 🤖 AII - Assistente de Inteligência de Importação
**Projeto Avançado - Zetta**

Este repositório contém a entrega final para o Lab *"Construa Seu Assistente Virtual Com Inteligência Artificial"* da DIO. O projeto foi estruturado seguindo rigorosamente os 6 passos metodológicos exigidos, evoluindo de uma base estática para um agente dinâmico com capacidade de **Tool Calling (Uso de Ferramentas / Web Scraping)**.

---

## 📝 1. Documentação do Agente
- **Nome do Agente:** AII (Assistente de Inteligência de Importação)
- **Objetivo Principal:** Automatizar e acelerar a consulta de alíquotas fiscais aduaneiras (II e IPI) através da NCM (Nomenclatura Comum do Mercosul), eliminando a digitação manual e a busca lenta em planilhas.
- **Público-Atvo:** Analistas de Comércio Exterior (Comex), Despachantes Aduaneiros e Gestores de Supply Chain.
- **Diretrizes de Comportamento:** Rigoroso, técnico e analítico. O agente adota uma postura de conformidade contábil estrita.
- **Restrições de Segurança (Anti-Alucinação):** A IA é expressamente proibida de deduzir, aproximar ou inventar alíquotas fiscais. Caso encontre inconsistências ou ausência de dados na consulta à ferramenta, deve reportar o erro técnico imediatamente, blindando a operação contra autuações ou erros de cálculo de margem.

---

## 🧠 2. Base de Conhecimento & Ferramentas (Tool Use)
Em vez de depender de um arquivo `.csv` estático que ficaria desatualizado rapidamente devido às constantes mudanças na legislação tributária brasileira, o agente foi dotado de uma ferramenta de **Web Scraping em tempo real**.

- **Alvo de Conexão:** Portal Fazcomex (Engine de Busca Aduaneira).
- **Mapeamento de Rota Fidedigno:** O agente foi calibrado para ignorar rotas estáticas inválidas (como `/ncm/`) e realizar requisições via parâmetros de consulta dinâmicos diretamente na URL de busca homologada do portal:
  `https://ncm.fazcomex.com.br/s/?term={NCM_LIMPO}`
- **Bibliotecas Utilizadas:** `requests` (para tráfego HTTP/HTTPS emulando um navegador real) e `BeautifulSoup4` (para parsing estruturado do DOM HTML).

---

## ⚙️ 3. Prompts do Agente (System Prompt)
O comportamento operacional da inteligência é blindado pelo seguinte *System Prompt* mestre:

> "Você é o Assistente de Inteligência de Importação (AII), um agente especialista em comércio exterior integrado ao ecossistema da Zetta Tecnologia e Soluções. Sua única e exclusiva função é identificar o NCM solicitado pelo usuário, acionar a ferramenta de varredura web no portal Fazcomex e extrair as alíquotas de II e IPI.
> 
> REGRAS CRÍTICAS:
> 1. Você deve isolar o código numérico do NCM da entrada do usuário, eliminando textos adicionais, pontos ou traços antes de chamar a ferramenta de busca.
> 2. O retorno final para o usuário deve seguir estritamente o formato estruturado padrão CSV (Comma-Separated Values). Não adicione textos explicativos longos fora deste formato, pois os dados serão consumidos por sistemas de ERP.
> 3. O formato de saída obrigatório é:
>    NCM,Descricao,II_Porcentagem,IPI_Porcentagem
>    {NCM_FORMATADO},{DESCRICAO},{II},{IPI}
> 4. Se a ferramenta retornar um erro de conexão ou código HTTP impeditivo (como 404 ou 403), repasse a mensagem de segurança: 'Desculpe, não tenho informações sobre este item na minha base de dados atual.' e nunca invente os dados."

---

## 💻 4. Aplicação Funcional
O protótipo funcional completo está localizado em `src/assistente.py`. O script executa um loop interativo em terminal (`while True`), captura inputs complexos em linguagem natural (ex: *"Busque o NCM 85171300"*), filtra o ruído de texto via Expressões Regulares (`re`), dispara a requisição HTTP com `User-Agent` simulado para evitar bloqueios, e processa o retorno estruturado.

O código foi projetado para rodar em ambientes virtuais (`venv`) isolados, garantindo a portabilidade do projeto.

---

## 📈 5. Avaliação e Métricas
O agente foi submetido a uma esteira de testes práticos de homologação (Testes de Mesa e Estresse de Rotas) para avaliar sua resiliência:

1. **Teste de Validação de Rota Dinâmica (Sucesso):**
   - *Input do Usuário:* `Busque o NCM 85171300`
   - *Comportamento do Agente:* Identificou o NCM `85171300`, ignorou a rota antiga `/ncm/85171300/` (que gerava erro 404), acionou com sucesso a rota correta `/s/?term=85171300`, obteve o Status Code 200 (OK) e formatou os dados perfeitamente.
   - *Output gerado:*
     ```text
     NCM,Descricao,II_Porcentagem,IPI_Porcentagem
     8517.13.00,Smartphones,16,15
     ```
   - *Status:* **✅ APROVADO**

2. **Teste de Resiliência a Inputs Parciais:**
   - *Input do Usuário:* `27` ou `2502`
   - *Comportamento do Agente:* Tratou o input parcial, efetuou a busca na URL parametrizada e retornou a estrutura de cabeçalho correta sem quebrar a execução do código.
   - *Status:* **✅ APROVADO**

3. **Teste de Proteção Fiscais (Anti-Alucinação):**
   - *Input do Usuário:* `Qual a taxa para importar sapatos de couro exótico?`
   - *Comportamento do Agente:* Ao não identificar um código numérico de NCM válido para consulta imediata na ferramenta, recusou o processamento preditivo genérico e solicitou o código correto do produto, evitando a geração de alíquotas falsas.
   - *Status:* **✅ APROVADO**

---

## 🎥 6. Pitch Final
- **O Problema:** O ecossistema tributário aduaneiro no Brasil é um dos mais complexos do mundo. Analistas de Comex perdem horas cruzando dados de tabelas TIPI e NCMs extensas no Excel para calcular o custo estimado de uma importação, gerando lentidão comercial e alta incidência de erros de digitação que custam multas pesadas.
- **A Solução:** O **AII** elimina a fricção operacional. Ele transforma uma dúvida em linguagem natural em uma consulta automatizada de Web Scraping, extraindo as informações direto da fonte governamental/aduaneira em milissegundos.
- **O Valor Gerado:** Escalar a capacidade operacional da **Zetta Tecnologia e Soluções**. Consultas fiscais aduaneiras que antes travavam fluxos de cotação agora são resolvidas instantaneamente, entregando saídas limpas em formato CSV prontas para alimentar sistemas automáticos de precificação ou Dashboards de Power BI, unindo automação inteligente com precisão contábil inabalável.
