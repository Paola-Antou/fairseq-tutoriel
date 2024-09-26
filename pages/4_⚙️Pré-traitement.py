import streamlit as st

def afficher_architecture_concepts():
    # Configuration de la page
    st.set_page_config(
        page_title="Architecture et Concepts Clés de Fairseq",
        page_icon=":brain:",
        layout="centered"
    )

    # Titre et introduction
    st.header(":brain: Architecture et Concepts Clés de Fairseq")
    st.write("""
    Fairseq est une bibliothèque puissante et flexible pour le traitement de séquences. Elle prend en charge divers modèles de pointe pour des tâches telles que la traduction automatique, le résumé de texte, et la reconnaissance vocale.
    
    Ce tutoriel explore en profondeur les concepts clés de Fairseq, les modèles supportés, et la manière de pré-traiter les datasets pour l'entraînement des modèles. Chaque commande sera expliquée en détail pour vous aider à mieux comprendre les étapes de prétraitement.
    """)

    # Section: Modèles Supportés
    st.header(":gear: Modèles Supportés")
    st.write("""
    Fairseq prend en charge plusieurs modèles populaires pour des tâches de traitement du langage naturel (NLP) et autres. Voici les principaux modèles supportés :
    
    - **Transformer** : Modèle performant basé sur l'attention, souvent utilisé pour la traduction automatique et la génération de séquences.
    - **RoBERTa** : Amélioration de BERT, utilisé pour l'apprentissage de représentations de langage non supervisé.
    - **BART** : Auto-encodeur séquentiel, efficace pour la génération de texte, comme le résumé ou la réponse à des questions.
    - **Wav2Vec** : Conçu pour la reconnaissance vocale à partir de données audio.
    - **M2M-100** : Modèle multilingue capable de traduire entre 100 langues sans langue pivot.
    """)

    # Section: Datasets et Pré-traitement
    st.header(":open_file_folder: Datasets et Pré-traitement")
    st.write("""
    Fairseq propose plusieurs commandes pour préparer et prétraiter les datasets avant l'entraînement. Le prétraitement est une étape cruciale pour garantir que les données sont prêtes à être utilisées efficacement par les modèles.
    """)

    st.markdown("""
    ### Commandes de prétraitement dans Fairseq :
    
    - **fairseq-preprocess** : La commande la plus courante pour binariser et préparer les données textuelles brutes pour l'entraînement. Elle est utilisée pour transformer les fichiers sources et cibles en un format binaire optimisé.
    
    ```bash
    fairseq-preprocess \
        --source-lang en --target-lang fr \
        --trainpref train --validpref valid --testpref test \
        --destdir data-bin/wmt17_en_fr \
        --workers 20
    ```

    **Explications des paramètres** :
    - `--source-lang` : Spécifie la langue source (ici l'anglais, `en`).
    - `--target-lang` : Spécifie la langue cible (ici le français, `fr`).
    - `--trainpref` : Fichier de données d'entraînement sans extension (Fairseq utilise les fichiers `train.en` et `train.fr`).
    - `--validpref` : Fichier de validation.
    - `--testpref` : Fichier de test.
    - `--destdir` : Dossier où les fichiers binarisés seront stockés.
    - `--workers` : Nombre de threads utilisés pour accélérer le prétraitement.

    - **fairseq-generate** : Cette commande génère des traductions à partir d'un modèle entraîné.
    
    ```bash
    fairseq-generate data-bin/wmt17_en_fr \
        --path checkpoints/checkpoint_best.pt \
        --beam 5 --remove-bpe
    ```

    **Explications des paramètres** :
    - `--path` : Chemin vers le modèle sauvegardé (fichier `.pt`).
    - `--beam` : Définit la taille du faisceau pour la recherche (généralement entre 5 et 10).
    - `--remove-bpe` : Retire les sous-unités de BPE (Byte Pair Encoding) pour reconstituer les mots complets.

    - **fairseq-train** : Cette commande est utilisée pour entraîner un modèle sur un dataset pré-traité.
    
    ```bash
    fairseq-train data-bin/wmt17_en_fr \
        --arch transformer \
        --optimizer adam --lr 0.0005 \
        --batch-size 128 \
        --max-epoch 10
    ```

    **Explications des paramètres** :
    - `--arch transformer` : Architecture du modèle (ici, Transformer).
    - `--optimizer adam` : Utilisation de l'algorithme Adam pour l'optimisation.
    - `--lr` : Définition du taux d'apprentissage.
    - `--batch-size` : Taille des mini-lots pour chaque étape d'entraînement.
    - `--max-epoch` : Nombre maximum d'époques d'entraînement.

    D'autres commandes pour le prétraitement incluent :
    - **fairseq-eval-lm** : Pour évaluer les modèles de langage.
    - **fairseq-interactive** : Pour interagir directement avec un modèle en temps réel.
    """)

    st.write("""
    ### Gestion des Datasets
    Fairseq permet de gérer des datasets volumineux à travers la **binarisation**, ce qui accélère le chargement des données pendant l'entraînement. Cette méthode optimise la mémoire et permet de traiter de grandes quantités de données.
    
    - **Tokenisation** : Processus de découpe du texte en tokens (mots ou sous-mots) afin de le rendre compatible avec les modèles.
    - **Normalisation** : Élimine les variations inutiles dans les données (comme les accents) pour faciliter l'entraînement.
    """)

    # Section: Exemples d'utilisation
    st.header("Exemples d'utilisation")
    st.write("""
    Voici des exemples concrets de la manière dont Fairseq peut être utilisé pour différentes tâches de traitement du langage naturel et d'audio.
    """)

    # Exemple 1: Traduction automatique avec Transformer
    st.subheader("1. Traduction automatique avec Transformer")
    st.write("""
    Après avoir pré-traité les données avec `fairseq-preprocess`, vous pouvez entraîner un modèle Transformer pour la traduction.
    
    ```bash
    fairseq-preprocess \
        --source-lang en --target-lang fr \
        --trainpref train --validpref valid --testpref test \
        --destdir data-bin/wmt17_en_fr \
        --workers 20
    ```
    
    Puis entraînez le modèle :
    
    ```bash
    fairseq-train data-bin/wmt17_en_fr \
        --arch transformer \
        --optimizer adam --lr 0.0005 \
        --batch-size 128 \
        --max-epoch 10
    ```
    """)

    # Exemple 2: Synthèse de texte avec BART
    st.subheader("2. Synthèse de texte avec BART")
    st.write("""
    BART est un modèle puissant pour la génération de texte, tel que le résumé de documents longs.
    
    ```bash
    fairseq-preprocess \
        --source-lang en --target-lang summary \
        --trainpref train --validpref valid --testpref test \
        --destdir data-bin/document_summarization \
        --workers 20
    ```

    Ensuite, entraînez BART pour la synthèse de texte :

    ```bash
    fairseq-train data-bin/document_summarization \
        --arch bart_base \
        --task translation \
        --criterion label_smoothed_cross_entropy \
        --label-smoothing 0.1 \
        --optimizer adam --lr 0.0003 --warmup-updates 500 --max-update 20000
    ```
    """)

    # Exemple 3: Reconnaissance vocale avec Wav2Vec
    st.subheader("3. Reconnaissance vocale avec Wav2Vec")
    st.write("""
    Pour transcrire des fichiers audio en texte, vous pouvez utiliser Wav2Vec :
    
    ```bash
    fairseq-hydra-train task=audio_pretraining \
        dataset.num_workers=8 \
        optimization.max_update=400000
    ```
    """)

    # Ajout de la section sur les erreurs fréquentes
    st.header(":warning: Erreurs Fréquentes et Solutions")
    st.write("""
    Voici quelques erreurs courantes lors de l'utilisation de Fairseq, ainsi que des suggestions pour les résoudre :
    
    - **Erreur : File not found error**  
      Cette erreur se produit souvent lorsque les chemins de fichier spécifiés dans les commandes `--trainpref`, `--validpref`, ou `--testpref` sont incorrects. Vérifiez que les fichiers existent dans le répertoire indiqué et que vous utilisez les bonnes extensions.

    - **Erreur : CUDA out of memory**  
      Si vous utilisez un GPU et que cette erreur survient, c'est probablement parce que votre modèle ou la taille de batch est trop grande pour la mémoire de la carte. Solution : diminuez la taille de `--batch-size` ou utilisez un modèle plus petit.

    - **Erreur : KeyError: 'source'**  
      Cela survient généralement lorsque les fichiers de données sont mal formatés ou que les fichiers sources/langues ne correspondent pas aux paramètres de pré-traitement. Assurez-vous que les fichiers sources et cibles correspondent aux langues spécifiées avec `--source-lang` et `--target-lang`.

    - **Erreur : ValueError: too many dimensions**  
      Cette erreur peut survenir lors du chargement de données lorsque les dimensions ne correspondent pas. Il se peut que les données aient été mal pré-traitées ou que les dimensions des entrées ne correspondent pas à celles attendues par le modèle. Solution : vérifiez vos données d'entrée et assurez-vous qu'elles sont bien formatées.
      
    - **Erreur : Validation loss doesn't decrease**  
      Si la perte de validation ne diminue pas après plusieurs époques, il est possible que votre modèle surapprenne les données d'entraînement. Essayez de régulariser davantage votre modèle en utilisant des techniques comme le `dropout` ou en réduisant le taux d'apprentissage.
    """)
    
    st.header("📘 Liens utiles")
    st.markdown("""
    - [Documentation officielle de Fairseq](https://fairseq.readthedocs.io/)
    - [Dépôt GitHub de Fairseq](https://github.com/facebookresearch/fairseq)
    """)

    # Affichage de la notification à la fin
    if st.button("Commencer l'exercice"):
        st.success("Bonne chance pour l'exercice !")
        st.switch_page('pages/Evaluation.py')
    if st.button("Pas maintenant"):
        st.switch_page('pages/5_Evaluation.py')

    
if __name__ == "__main__":
    afficher_architecture_concepts()
