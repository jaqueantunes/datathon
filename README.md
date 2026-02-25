# datathon

# Datathon – Associação Passos Mágicos  
## Modelo Preditivo de Risco de Defasagem Educacional

Projeto desenvolvido no Datathon da Pós-Tech com o objetivo de identificar, de forma antecipada, alunos com risco de defasagem educacional, utilizando indicadores do PEDE (Pesquisa Extensiva do Desenvolvimento Educacional).

---

## Objetivo do Projeto

Construir um modelo de Machine Learning capaz de:

- Identificar padrões associados ao risco de defasagem
- Gerar probabilidade de risco
- Disponibilizar a previsão por meio de uma aplicação web (Streamlit)
- Apoiar decisões pedagógicas com base em dados

---

## Base de Dados

Dataset: PEDE 2022  
Indicadores utilizados:

- IDA – Indicador de Desempenho Acadêmico
- IEG – Indicador de Engajamento
- IAA – Indicador de Autoavaliação
- IPS – Indicador Psicossocial
- IPV – Indicador de Ponto de Virada

 # Insights para o Storytelling

💡 Principais Descobertas (EDA)

1. Sucesso na Retenção: A associação possui mais de 60% de Veteranos. Isso mostra que o projeto não é apenas assistencialista, mas gera um vínculo de longo prazo com o aluno.

2. Combate à Defasagem (IAN): Observamos uma tendência de queda na "Defasagem Severa" e um aumento no "Nível Ideal". O reforço escolar está colocando os alunos de volta no trilho certo para suas idades.

3. A "Alavanca" do Ponto de Virada: O Engajamento (IEG) e o Desempenho Acadêmico (IDA) são os fatores que mais influenciam o IPV.

4. Insight: O aluno não atinge o ponto de virada por "sorte", mas sim pela constância de presença e entrega de tarefas.

5. Impacto Real no Desempenho: Alunos que atingem o Ponto de Virada performam significativamente melhor. Existe um salto de qualidade visível no gráfico de barras entre quem "virou a chave" e quem ainda não.

6. Escalabilidade: Mesmo com a entrada de novos alunos a cada ano, as médias do INDE e dos indicadores psicossociais se mantêm estáveis ou em crescimento, indicando que a metodologia da Passos Mágicos suporta o crescimento da base de alunos.

Variável alvo (Target):
TARGET_RISCO = 1 se IAN < 5 (Defasagem)
TARGET_RISCO = 0 caso contrário


---

##  Modelagem

Modelos utilizados:

- Logistic Regression (Baseline)
- Random Forest (Modelo Principal)

### Métricas Avaliadas:
- Accuracy
- Precision
- Recall
- F1-score
- Curva ROC

O modelo Random Forest apresentou melhor desempenho comparado ao baseline.

---

## Principais Fatores de Risco

De acordo com o modelo treinado:

1. IDA (Desempenho Acadêmico)
2. IEG (Engajamento)
3. IAA (Autoavaliação)

Isso reforça a importância do desempenho e do engajamento como principais preditores de risco.

---

##  Aplicação Web

A solução foi disponibilizada em uma aplicação desenvolvida com Streamlit.

### Funcionalidades:
- Inserção manual dos indicadores
- Cálculo da probabilidade de risco
- Classificação automática (baixo, moderado ou alto risco)
- Visualização da importância das variáveis
- Interpretação pedagógica automatizada

🔗 **Link da aplicação:**  
(https://datathon-tiqsw6qn3rweuwauuuamzi.streamlit.app/)

---




---

## Conclusão

O projeto demonstra como a análise de dados e Machine Learning podem ser aplicados ao contexto educacional para:

- Antecipar riscos
- Apoiar decisões pedagógicas
- Gerar impacto social baseado em evidências

---

##  Tecnologias Utilizadas

- Python
- Pandas
- Scikit-learn
- Streamlit
- Matplotlib
- GitHub

---

Projeto desenvolvido para fins acadêmicos no Datathon Pós-Tech.
