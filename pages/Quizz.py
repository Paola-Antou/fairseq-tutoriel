import streamlit as st
import os

# Fonction pour afficher le quiz
def afficher_quiz():
    st.set_page_config(
        page_title="Quiz Fairseq",
        page_icon=":question:",
        layout="centered"
    )

    st.header(':blue[Quiz Fairseq]')
    st.write("Testez vos connaissances sur Fairseq après avoir suivi le tutoriel.😉")
    st.write("---")

    # Questions et options du quiz
    questions = {
        "1. Qu'est-ce que Fairseq ?": [
            "Une bibliothèque pour entraîner des modèles de séquences",
            "Un langage de programmation",
            "Un logiciel de traduction automatique",
            "Un modèle de réseau de neurones"
        ],
        "2. Quelle architecture n'est pas supportée par Fairseq ?": [
            "Transformer", 
            "BART", 
            "ResNet", 
            "RoBERTa"
        ],
        "3. Quelle est l'une des raisons principales d'utiliser Fairseq ?": [
            "Pour son support limité pour des petites bases de données",
            "Parce qu'il est compatible uniquement avec du matériel spécifique",
            "Pour sa flexibilité et ses performances de pointe",
            "Parce qu'il est utilisé uniquement dans le domaine de l'audio"
        ],
        "4. Quelle tâche n'est pas un cas d'usage de Fairseq ?": [
            "Traduction automatique",
            "Synthèse de texte",
            "Détection d'objets dans une image",
            "Classification de texte"
        ],
        "5. Quel modèle est utilisé pour la génération de texte dans Fairseq ?": [
            "Transformer",
            "BART",
            "ResNet",
            "RoBERTa"
        ]
    }

    # Bonnes réponses
    reponses_correctes = {
        "1. Qu'est-ce que Fairseq ?": "Une bibliothèque pour entraîner des modèles de séquences",
        "2. Quelle architecture n'est pas supportée par Fairseq ?": "ResNet",
        "3. Quelle est l'une des raisons principales d'utiliser Fairseq ?": "Pour sa flexibilité et ses performances de pointe",
        "4. Quelle tâche n'est pas un cas d'usage de Fairseq ?": "Détection d'objets dans une image",
        "5. Quel modèle est utilisé pour la génération de texte dans Fairseq ?": "BART"
    }

    # Stocker les réponses de l'utilisateur
    reponses_utilisateur = {}

    # Affichage des questions
    for question, options in questions.items():
        st.write(f"**{question}**")
        reponse = st.radio(f"Sélectionnez une réponse pour: {question}", options)
        reponses_utilisateur[question] = reponse
        st.write(" ")

    # Bouton de soumission
    if st.button("Soumettre"):
        st.write("### Résultats du quiz:")
        score = 0
        for question, bonne_reponse in reponses_correctes.items():
            if reponses_utilisateur[question] == bonne_reponse:
                st.success(f"{question} : Bonne réponse ! :white_check_mark:")
                score += 1
            else:
                st.error(f"{question} : Mauvaise réponse. La bonne réponse est : {bonne_reponse}")
        st.write(f"**Votre score : {score} / {len(questions)}**")

        # Bouton pour accéder à la deuxième page (second.py)
        if st.button("Passez à l'étape suivante "):
        # Utilisation de os.system pour lancer second.py
            os.system('streamlit run pages/💻Installation.py')

# Afficher le quiz
if __name__ == "__main__":
    afficher_quiz()
