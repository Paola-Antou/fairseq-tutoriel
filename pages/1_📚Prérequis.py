import streamlit as st
import os

def afficher_tutoriel():
    # Configuration de la page
    st.set_page_config(
        page_title="Comprendre Fairseq - Page 1 ",
        page_icon=":books:",
        layout="centered"
    )

    # Titre principal
    st.header(':blue[ Comprendre Fairseq ]')
    st.write(" ")

    # Section 1 : Qu'est-ce que Fairseq ?
    st.subheader(":books: Qu'est-ce que Fairseq ?")
    st.write("""
    Fairseq est une bibliothèque open-source développée par Facebook AI Research (FAIR). Elle est spécialement conçue pour 
    construire et entraîner des modèles de séquences, notamment pour des tâches comme la traduction automatique, le résumé de texte, et d'autres tâches 
    de traitement du langage naturel (NLP).
    """)

    st.write("""
    Fairseq supporte plusieurs architectures de modèles performants telles que :
    - **Transformer** : Une architecture largement utilisée pour la traduction automatique.
    - **BART** : Un modèle pour la génération de texte, utilisé pour des tâches comme le résumé de texte et la génération de réponses.
    - **RoBERTa** : Une version optimisée de BERT, populaire pour diverses tâches de NLP.
    """)

    st.info("👉 Fairseq est populaire pour son efficacité et ses performances de pointe dans les tâches de traitement de séquences.")

    st.write(" ")
    
    # Section 2 : Pourquoi utiliser Fairseq ?
    st.subheader(":bulb: Pourquoi utiliser Fairseq ?")
    st.write("""
    Il y a plusieurs raisons d'utiliser Fairseq :
    - **Flexibilité** : Fairseq permet de personnaliser les modèles et les tâches, ce qui le rend adapté à divers cas d'usage dans le traitement des séquences.
    - **Performances de pointe** : Grâce à son support des dernières architectures de modèles, Fairseq a montré des performances de pointe dans de nombreuses tâches.
    - **Parallélisme** : Fairseq peut traiter efficacement de grandes quantités de données en parallèle, ce qui en fait un excellent choix pour les chercheurs et les ingénieurs travaillant avec de grandes bases de données.
    - **Support multi-GPU** : L'entraînement des modèles peut être facilement distribué sur plusieurs GPU pour une accélération considérable des temps d'entraînement.
    """)

    st.info("🚀 En résumé, Fairseq est un outil puissant pour les chercheurs et développeurs souhaitant travailler sur des modèles de séquences à grande échelle.")

    st.write(" ")
    
    # Section 3 : Cas d'usage courants
    st.subheader(":hammer_and_wrench: Cas d'usage courants")
    st.write("""
    Fairseq est principalement utilisé dans le domaine du traitement du langage naturel (NLP). Voici quelques-uns des cas d'usage courants :
    - **Traduction automatique** : Construire des systèmes de traduction de haute qualité entre différentes langues.
    - **Synthèse de texte** : Générer du texte à partir de données non structurées ou résumer de longs articles en phrases concises.
    - **Question-Réponse** : Utiliser Fairseq pour des tâches de génération de réponses à partir de questions données.
    - **Classification de texte** : Entraîner des modèles pour classer automatiquement des documents ou des phrases selon leur contenu.
    """)

    st.info("🌍 Fairseq est un atout majeur pour les chercheurs travaillant sur des applications NLP à l'échelle industrielle.")
    st.write(" ")
    st.header("📘 Liens utiles")
    st.markdown("""
    - [Documentation officielle de Fairseq](https://fairseq.readthedocs.io/)
    - [Dépôt GitHub de Fairseq](https://github.com/facebookresearch/fairseq)
    """)
    st.success("Passez un petit quizz pour évaluer ce que vous venez d'apprendre")
    # Bouton pour accéder à la deuxième page (second.py)
    if st.button("Commencer l'exercice🏆 "):
        st.success("Bonne chance pour l'exercice !")
        # Utilisation de os.system pour lancer second.py
        st.switch_page('2_Quizz.py')

if __name__ == "__main__":
    afficher_tutoriel()
