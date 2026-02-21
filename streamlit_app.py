if st.button("Prever"):
    dados = np.array([[ida, ieg, iaa, ips, ipv]])
    
    prob = modelo.predict_proba(dados)[0][1]
    
    st.markdown("## 🎯 Resultado da Análise")
    st.metric("Probabilidade de Risco", f"{prob:.2%}")
    
    if prob > 0.7:
        st.error("⚠️ RISCO ALTO: intervenção imediata recomendada.")
    elif prob > 0.4:
        st.warning("🟡 Risco moderado: monitoramento recomendado.")
    else:
        st.success("🟢 Baixo risco.")
    
    st.markdown("---")
    
    # 📊 IMPORTÂNCIA DAS VARIÁVEIS
    st.markdown("## 📊 O que mais influencia o risco?")
    
    features = ['IDA', 'IEG', 'IAA', 'IPS', 'IPV']
    importancias = modelo.feature_importances_

    df_importancia = pd.DataFrame({
        'Indicador': features,
        'Importância': importancias
    }).sort_values(by='Importância', ascending=False)

    # 🎨 Gráfico colorido
    fig, ax = plt.subplots()
    cores = ['#d62728', '#ff7f0e', '#1f77b4', '#2ca02c', '#9467bd']
    ax.bar(df_importancia['Indicador'], df_importancia['Importância'], color=cores)
    ax.set_ylabel("Importância")
    ax.set_title("Ranking de Impacto no Risco")
    st.pyplot(fig)

    # 🏆 Ranking dinâmico
    st.markdown("### 🏆 Ranking das Variáveis")
    for i, row in df_importancia.iterrows():
        st.write(f"{row['Indicador']} → {row['Importância']:.2%}")

    st.markdown("---")

    # 🧠 Explicação automática baseada no input
    st.markdown("## 🧠 Interpretação Inteligente")

    explicacao = []

    if ida < 6:
        explicacao.append("• IDA abaixo do ideal pode indicar fragilidade acadêmica.")
    if ieg < 6:
        explicacao.append("• IEG baixo sugere pouco engajamento nas atividades.")
    if iaa < 6:
        explicacao.append("• IAA reduzido pode indicar baixa autoconfiança.")
    if ips < 6:
        explicacao.append("• IPS baixo pode sinalizar vulnerabilidade emocional.")
    if ipv < 6:
        explicacao.append("• IPV baixo pode indicar ausência de progresso consistente.")

    if explicacao:
        for item in explicacao:
            st.write(item)
    else:
        st.success("Os indicadores mostram um perfil educacional consistente.")