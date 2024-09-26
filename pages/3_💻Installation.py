import streamlit as st
import os

def afficher_installation():
    # Configuration de la page
    st.set_page_config(
        page_title="Installation Fairseq - Page 2",
        page_icon=":computer:",
        layout="centered"
    )

    # Titre et description
    st.title(":blue[:wrench: Installation et Configuration de Fairseq ]")

    st.write("""
    Cette section vous guide pas à pas dans l'installation de Fairseq et la configuration de votre environnement de développement. 
    Assurez-vous de suivre chaque étape pour garantir un environnement stable et fonctionnel.
    """)

    # Pré-requis
    st.subheader("1. Pré-requis")
    st.write("""
    Avant d'installer Fairseq, assurez-vous d'avoir :
    - Python 3.6 ou une version supérieure installé sur votre machine.
    - **PyTorch** : Fairseq est construit sur PyTorch, donc vous devez l'installer en premier.
    """)

    # Installation de PyTorch
    st.subheader("2. Installation de PyTorch")
    st.write("""
    Installez PyTorch en utilisant la commande suivante :
    """)
    st.code("pip install torch", language="bash")
    st.write("""
    Vous pouvez également utiliser [le site officiel de PyTorch](https://pytorch.org/get-started/locally/) pour sélectionner les options spécifiques à votre système d'exploitation et matériel (GPU/CPU).
    """)

    # Installation de Fairseq
    st.subheader("3. Installation de Fairseq")
    st.write("""
    Une fois PyTorch installé, vous pouvez installer Fairseq avec la commande suivante :
    """)
    st.code("pip install fairseq", language="bash")
    st.write("""
    Alternativement, vous pouvez cloner directement le dépôt GitHub et l'installer depuis la source :
    """)
    st.code("""
    git clone https://github.com/pytorch/fairseq
    cd fairseq
    pip install --editable ./
    """, language="bash")

    # Environnement virtuel
    st.subheader("4. Configuration de l'environnement virtuel")
    st.write("""
    Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances de votre projet. Voici comment créer et activer un environnement virtuel :
    """)
    st.code("""
    # Créer un environnement virtuel
    python -m venv fairseq-env

    # Activer l'environnement (sur macOS/Linux)
    source fairseq-env/bin/activate

    # Activer l'environnement (sur Windows)
    fairseq-env\\Scripts\\activate
    """, language="bash")
    st.write("""
    Une fois activé, vous pouvez installer PyTorch et Fairseq à l'intérieur de cet environnement.
    """)

    # Vérification de l'installation
    st.subheader("5. Vérification de l'installation")
    st.write("""
    Pour vérifier que Fairseq a été installé correctement, exécutez la commande suivante :
    """)
    st.code("python -m fairseq_cli.train --help", language="bash")
    st.write("""
    Si l'installation est réussie, cette commande affichera l'aide de la commande `train` de Fairseq, ce qui confirme que tout fonctionne correctement.
    """)

    # Liens utiles
    st.header("📘 Liens utiles")
    st.markdown("""
    - [Documentation officielle de Fairseq](https://fairseq.readthedocs.io/)
    - [Dépôt GitHub de Fairseq](https://github.com/facebookresearch/fairseq)
    """)

    # Conclusion
    st.success("Installation terminée avec succès ! Vous êtes maintenant prêt à utiliser Fairseq dans votre projet.")
        # Bouton pour accéder à la deuxième page (second.py)
    if st.button("Suivant"):
        # Utilisation de os.system pour lancer second.py
        st.switch_page('pages/4_⚙️Pré-traitement.py')
if __name__ == "__main__":
    afficher_installation()
