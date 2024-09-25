import streamlit as st
import os

def afficher_fine_tuning_optimisation():
    # Configuration de la page
    st.set_page_config(
        page_title="Fine-tuning et Optimisation",
        page_icon=":zap:",
        layout="centered"
    )

    # Titre et introduction
    st.header(":zap: Fine-tuning et Optimisation")
    st.write("""
    Dans cette section, nous allons explorer comment ajuster des modèles pré-entraînés pour des tâches spécifiques à l'aide du fine-tuning, ainsi que les techniques d'optimisation pour accélérer l'entraînement des modèles.
    """)

    # Section: Fine-tuning des modèles pré-entraînés
    st.header(":mag: Fine-tuning")
    st.write("""
    Le fine-tuning est une technique qui consiste à ajuster un modèle pré-entraîné pour qu'il puisse mieux accomplir une tâche spécifique. Au lieu de former un modèle à partir de zéro, on tire parti d'un modèle déjà entraîné sur une grande quantité de données, comme BERT ou GPT, pour une tâche précise. Cela permet de réutiliser les connaissances déjà acquises par le modèle.
    """)

    # Exemples de Fine-tuning
    st.subheader("Exemple de Fine-tuning avec Transformers")
    st.write("""
    Pour fine-tuner un modèle Transformer, vous pouvez suivre ces étapes :
    
    ```python
    from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification

    # Chargement du modèle pré-entraîné
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

    # Définir les arguments d'entraînement
    training_args = TrainingArguments(
        output_dir='./results',  # Répertoire où les résultats seront sauvegardés
        evaluation_strategy="epoch",  # Évalue le modèle après chaque époque
        per_device_train_batch_size=8,  # Taille du lot pour l'entraînement par GPU
        per_device_eval_batch_size=8,  # Taille du lot pour l'évaluation
        num_train_epochs=3,  # Nombre total d'époques d'entraînement
        weight_decay=0.01,  # Paramètre de régularisation pour éviter l'overfitting
        logging_dir='./logs',  # Répertoire où les logs seront enregistrés
        logging_steps=10,  # Nombre de pas entre chaque log
    )

    # Utilisation de Trainer pour le fine-tuning
    trainer = Trainer(
        model=model,  # Le modèle que nous souhaitons entraîner
        args=training_args,  # Les paramètres d'entraînement
        train_dataset=train_dataset,  # Les données d'entraînement
        eval_dataset=eval_dataset  # Les données de validation
    )

    trainer.train()
    ```

    **Explication des paramètres dans `Trainer`** :
    - `model` : Le modèle pré-entraîné que vous souhaitez ajuster.
    - `args` : Les paramètres d'entraînement, comme définis dans `TrainingArguments`.
    - `train_dataset` : Le jeu de données utilisé pour l'entraînement.
    - `eval_dataset` : Le jeu de données utilisé pour l'évaluation pendant l'entraînement.
    """)

    # Section: Optimisation de l'entraînement
    st.header(":rocket: Optimisation")
    st.write("""
    L'optimisation permet d'accélérer l'entraînement des modèles, surtout pour les architectures complexes, en utilisant des techniques comme le multi-GPU et la précision réduite (FP16). Ces techniques sont particulièrement utiles pour des tâches computationnellement lourdes.
    """)

    # Techniques d'optimisation
    st.subheader("1. Entraînement avec multi-GPU")
    st.write("""
    Utiliser plusieurs GPU permet de diviser le travail d'entraînement sur plusieurs cartes graphiques, accélérant ainsi le processus.

    ```bash
    torchrun --nproc_per_node=4 train.py --distributed
    ```

    **Explication** :  
    - `--nproc_per_node=4` : Utilise 4 GPUs pour l'entraînement.
    - `--distributed` : Active l'entraînement distribué, ce qui permet de diviser le travail d'entraînement sur plusieurs GPUs.
    """)

    st.subheader("2. Précision Mixte (FP16)")
    st.write("""
    La précision réduite (FP16) est une méthode qui utilise des flottants de 16 bits au lieu de 32 bits, ce qui accélère l'entraînement tout en économisant de la mémoire GPU. Cela est particulièrement utile pour les modèles complexes ou lorsque vous travaillez avec des données volumineuses.

    ```python
    from transformers import Trainer, TrainingArguments

    # Définir les arguments d'entraînement avec FP16
    training_args = TrainingArguments(
        output_dir='./results',  # Répertoire de sortie
        per_device_train_batch_size=16,  # Taille du batch par appareil
        num_train_epochs=3,  # Nombre d'époques d'entraînement
        fp16=True,  # Active l'entraînement en précision mixte (FP16)
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset
    )

    trainer.train()
    ```

    **Paramètres supplémentaires** :
    - `fp16=True` : Active l'entraînement avec précision mixte (FP16), ce qui réduit l'utilisation de mémoire GPU et accélère le processus d'entraînement tout en maintenant une précision acceptable.
    """)

    # Ajout de la section sur les erreurs fréquentes
    st.header(":warning: Erreurs Fréquentes et Solutions")
    st.write("""
    Voici quelques erreurs courantes liées au fine-tuning et à l'optimisation, ainsi que leurs solutions :

    - **Erreur : 'CUDA out of memory'**  
      Solution : Diminuez la taille du batch ou activez FP16 pour économiser de la mémoire GPU.

    - **Erreur : 'RuntimeError: all distributed processes must have the same model and input shapes'**  
      Solution : Vérifiez que toutes les machines utilisant du multi-GPU ont la même configuration de modèle.
    """)

    st.header("📘 Liens utiles")
    st.markdown("""
    - [Documentation officielle de Fairseq](https://fairseq.readthedocs.io/)
    - [Dépôt GitHub de Fairseq](https://github.com/facebookresearch/fairseq)
    """) 
    if st.button("Commencer l'exercice"):
        st.success("Bonne chance pour l'exercice !")
        os.system('streamlit run pages\Exercice.py')
# Afficher la page
if __name__ == "__main__":
    afficher_fine_tuning_optimisation()
