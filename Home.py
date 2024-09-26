import streamlit as st
import os

def afficher_tutoriel():
    # Configuration de la page
    st.set_page_config(
        page_title="Tutoriel fairseq - Page 1",
        page_icon=":rocket:",
        layout="centered"
    )

    # Titre et introduction
    st.title(":blue[Tutoriel d'utilisation de Fairseq]")
    
    st.image("https://pbs.twimg.com/profile_images/1257734697540554752/E-ME_L_q_400x400.jpg", width=200)

    st.write("""
    Bienvenue dans ce tutoriel interactif sur Fairseq, une bibliothèque de référence pour le traitement des modèles de séquence.
    Que vous soyez débutant ou expérimenté en traitement du langage naturel, ce tutoriel vous guidera dans la mise en place et l'entraînement
    de modèles performants pour des tâches comme la traduction automatique ou la synthèse de texte.
    """)

    # Objectifs
    st.header(":dart: Objectifs")

    st.write("""
    Voici les objectifs principaux de ce tutoriel :
    """)

    st.markdown("""
    - :books: **Comprendre Fairseq** : Découvrir la bibliothèque Fairseq, son utilité et ses applications courantes.
    - :computer: **Installation et configuration** : Apprendre à installer Fairseq et configurer l'environnement de travail.
    - :gear: **Préparation des données** : Apprendre à pré-traiter et préparer des datasets pour l'entraînement.
    - :rocket: **Entraînement de modèles** : Comprendre comment entraîner des modèles comme Transformer avec Fairseq.
    - :mag: **Fine-tuning** : Découvrir comment ajuster des modèles pré-entraînés pour des tâches spécifiques.
    - :zap: **Optimisation** : Maîtriser les techniques d'optimisation pour accélérer l'entraînement avec du multi-GPU et FP16.
    - :trophy: **Démo pratique** : Participer à une démo en temps réel pour mieux saisir les concepts abordés.
    """)

    # Section interactivité
    st.write(" ")
    st.success("Prêt à plonger dans le tutoriel ? Aller à la page suivante pour démarrer la première étape !")

    # Bouton pour accéder à la deuxième page (second.py)
    if st.button("Commencer "):
        # Utilisation de os.system pour lancer second.py
        st.switch_page('pages/1_📚Prérequis.py')



if __name__ == "__main__":
    afficher_tutoriel()
