import streamlit as st
import pandas as pd
import subprocess


# Titre de la page
st.title("Évaluation des commandes de prétraitement et d'entraînement - Fairseq")

# Section 1: Présentation du dataset
st.header("Section 1: Exploration du Dataset")

# Charger et afficher le dataset
dataset_path = 'pages/French_to_fongbe.csv'
df = pd.read_csv(dataset_path)

# Montrer les premières lignes
st.write("Voici les premières lignes du dataset de phrases en français et fon :")
st.write(df.head())

# Expliquer le dataset
st.markdown("""
Ce dataset contient des phrases en **français** et leurs traductions en **fon**. 
L'objectif est d'utiliser ce corpus pour entraîner un modèle de traduction automatique.
**Colonne source** : Phrases en français.  
**Colonne cible** : Phrases en fon.
""")

# Section 2: Prétraitement avec `fairseq-preprocess`
st.header("Section 2: Prétraitement des données avec `fairseq-preprocess`")

st.markdown("""
Vous allez maintenant configurer et lancer le prétraitement des données. 
Veuillez remplir les champs ci-dessous pour configurer la commande `fairseq-preprocess`.
""")

# Inputs pour le prétraitement
source_lang = st.text_input("Langue source ", "")
target_lang = st.text_input("Langue cible ", "")
train_path = st.text_input("Chemin du fichier d'entraînement", "/pages/train")
valid_path = st.text_input("Chemin du fichier de validation", "/pages/valid")
test_path = st.text_input("Chemin du fichier de test", "/pages/test")
output_dir = st.text_input("Dossier de sortie des fichiers binaires", "/pages/data-bin")

# Bouton pour prétraiter
if st.button("Lancer le prétraitement"):
    preprocess_cmd = (
        f"fairseq-preprocess --source-lang {source_lang} --target-lang {target_lang} "
        f"--trainpref {train_path} --validpref {valid_path} --testpref {test_path} "
        f"--destdir {output_dir} --workers 4"
    )
    try:
        # Lancer la commande
        subprocess.run(preprocess_cmd, shell=True, check=True)
        st.success("Prétraitement terminé avec succès.")
    except subprocess.CalledProcessError as e:
        st.error(f"Erreur lors du prétraitement : {str(e)}")

# Section 3: Entraînement avec `fairseq-train`
st.header("Section 3: Entraînement du modèle avec `fairseq-train`")

st.markdown("""
Configurez et lancez l'entraînement du modèle avec `fairseq-train`.
Remplissez les champs ci-dessous pour ajuster la commande d'entraînement.
""")

# Inputs pour l'entraînement
arch = st.text_input("Architecture du modèle (ex: transformer)", "")
max_tokens = st.number_input("Nombre maximum de tokens", value=4000)
save_dir = st.text_input("Dossier de sauvegarde des checkpoints", "/pages/checkpoints")
learning_rate = st.number_input("Taux d'apprentissage", value=0.0005)
max_epoch = st.number_input("Nombre maximum d'époques", value=10)

# Bouton pour entraîner
if st.button("Lancer l'entraînement"):
    train_cmd = (
        f"fairseq-train {output_dir} --source-lang {source_lang} --target-lang {target_lang} "
        f"--arch {arch} --max-tokens {max_tokens} --save-dir {save_dir} --optimizer adam "
        f"--lr {learning_rate} --clip-norm 0.1 --dropout 0.3 --max-epoch {max_epoch}"
    )
    try:
        # Lancer la commande
        subprocess.run(train_cmd, shell=True, check=True)
        st.success("Entraînement terminé avec succès.")
    except subprocess.CalledProcessError as e:
        st.error(f"Erreur lors de l'entraînement : {str(e)}")

# Section 4: Évaluation du modèle avec `fairseq-generate`
st.header("Section 4: Évaluation du modèle avec `fairseq-generate`")

st.markdown("""
Lancez l'évaluation du modèle sur le jeu de test avec `fairseq-generate`.
""")

# Inputs pour l'évaluation
checkpoint_path = st.text_input("Chemin du checkpoint du modèle", "/pages/checkpoints/checkpoint_best.pt")

# Bouton pour évaluer
if st.button("Lancer l'évaluation"):
    eval_cmd = (
        f"fairseq-generate {output_dir} --path {checkpoint_path} --batch-size 64 --beam 5"
    )
    try:
        # Lancer la commande d'évaluation
        subprocess.run(eval_cmd, shell=True, check=True)
        st.success("Évaluation terminée avec succès.")
    except subprocess.CalledProcessError as e:
        st.error(f"Erreur lors de l'évaluation : {str(e)}")
