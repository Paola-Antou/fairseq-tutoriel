import streamlit as st

def afficher_exercices_fine_tuning_optimisation():
    # Configuration de la page
    st.set_page_config(
        page_title="Exercices Fine-tuning et Optimisation",
        page_icon=":zap:",
        layout="centered"
    )

    # Titre de la page
    st.header(":zap: Exercices sur le Fine-tuning et l'Optimisation")
    st.write("""
    Bienvenue dans cette section d'exercice ! Vous allez pouvoir ajuster les paramètres de fine-tuning et d'optimisation, et voir comment cela affecte l'entraînement des modèles. Vous pourrez également explorer les effets du multi-GPU et de la précision réduite (FP16).
    """)

    # Explication de l'exercice
    st.subheader(":book: Introduction à l'exercice")
    st.write("""
    Dans cet exercice, vous allez fine-tuner un modèle fictif basé sur un modèle pré-entraîné, et ajuster des paramètres tels que la taille du batch, le nombre d'époques, et l'utilisation de GPU.
    """)

    # Paramètres du modèle (utilisation de sliders pour que l'utilisateur ajuste les valeurs)
    st.subheader(":gear: Paramètres de Fine-tuning")
    
    # Nombre d'époques
    num_epochs = st.slider("Nombre d'époques d'entraînement", 1, 10, value=3, step=1)
    
    # Taille du batch pour l'entraînement
    batch_size = st.slider("Taille de batch pour l'entraînement", 4, 32, value=8, step=4)
    
    # Taille du batch pour l'évaluation
    eval_batch_size = st.slider("Taille de batch pour l'évaluation", 4, 32, value=8, step=4)
    
    # Décroissance du poids
    weight_decay = st.slider("Weight Decay (Régularisation)", 0.0, 0.1, value=0.01, step=0.01)
    
    # Choix de l'entraînement multi-GPU
    use_multi_gpu = st.checkbox("Utiliser plusieurs GPUs", value=False)
    
    # Utilisation de la précision mixte (FP16)
    use_fp16 = st.checkbox("Activer FP16 (Précision Mixte)", value=False)

    # Bouton pour valider les paramètres
    if st.button("Lancer l'entraînement"):
        st.write(f"""
        ### Paramètres sélectionnés :
        - Nombre d'époques : {num_epochs}
        - Taille du batch (entraînement) : {batch_size}
        - Taille du batch (évaluation) : {eval_batch_size}
        - Weight Decay : {weight_decay}
        - Multi-GPU : {"Activé" if use_multi_gpu else "Désactivé"}
        - FP16 : {"Activé" if use_fp16 else "Désactivé"}
        """)
        
        # Simulation de l'entraînement
        st.success("Entraînement simulé avec succès !")
        st.write("Le modèle a été entraîné avec les paramètres sélectionnés.")

        # Résultats de l'entraînement
        st.write("""
        ### Résultats simulés de l'entraînement :
        - Précision d'entraînement : 92%
        - Précision d'évaluation : 89%
        - Perte : 0.35
        """)
    
    # Section sur l'optimisation
    st.header(":rocket: Optimisation des Modèles")
    st.write("""
    Ici, vous pouvez tester des techniques d'optimisation comme le multi-GPU et la précision mixte pour améliorer la vitesse d'entraînement de vos modèles.
    """)

    # Explication des techniques d'optimisation
    st.write("""
    - **Multi-GPU** : Utiliser plusieurs GPUs permet de répartir le calcul sur plusieurs cartes graphiques, réduisant ainsi le temps d'entraînement.
    - **Précision mixte (FP16)** : L'utilisation de flottants 16 bits permet d'accélérer l'entraînement tout en réduisant la consommation de mémoire GPU.
    """)

    # Section sur les erreurs fréquentes
    st.header(":warning: Erreurs Fréquentes à Éviter")
    st.write("""
    Pendant l'entraînement et l'optimisation des modèles, il est courant de rencontrer des erreurs. Voici quelques-unes des erreurs les plus fréquentes et comment les résoudre :
    
    - **'CUDA out of memory'** : Diminuer la taille du batch ou activer la précision mixte (FP16) pour économiser la mémoire GPU.
    - **'RuntimeError: all distributed processes must have the same model and input shapes'** : Assurez-vous que toutes les machines participant à l'entraînement multi-GPU utilisent les mêmes paramètres de modèle.
    """)

    # Section de quiz pour tester la compréhension
    st.header(":pencil: Quiz : Testez vos connaissances")
    st.write("Répondez à ces questions pour valider votre compréhension des concepts de fine-tuning et d'optimisation.")

    # Questions du quiz
    question_1 = st.radio("1. Quel est l'avantage principal du fine-tuning par rapport à l'entraînement d'un modèle depuis zéro ?", 
                          ("A. Réduit le temps d'entraînement", "B. Améliore la précision", "C. Utilise un modèle pré-entraîné sur une grande quantité de données", "D. Toutes les réponses"))
    
    if question_1 == "D. Toutes les réponses":
        st.success("Bonne réponse !")
    else:
        st.error("Mauvaise réponse. La bonne réponse est D. Toutes les réponses.")

    question_2 = st.radio("2. Quel est l'effet de l'utilisation de FP16 pendant l'entraînement ?", 
                          ("A. Augmente la précision", "B. Accélère l'entraînement et économise de la mémoire", "C. Ralentit l'entraînement", "D. Réduit la consommation d'énergie"))
    
    if question_2 == "B. Accélère l'entraînement et économise de la mémoire":
        st.success("Bonne réponse !")
    else:
        st.error("Mauvaise réponse. La bonne réponse est B. Accélère l'entraînement et économise de la mémoire.")

# Afficher la page
if __name__ == "__main__":
    afficher_exercices_fine_tuning_optimisation()
