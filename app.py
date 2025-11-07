import streamlit as st
from supabase import create_client, Client

# Connexion à Supabase avec service role key
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]  # service role key
supabase: Client = create_client(url, key)

st.success("✅ Connexion à Supabase réussie!")

# --- Ajout d'une entrée ---
st.write("## ➕ Ajouter une entrée à la table 'test-base'")

nouvelle_valeur = st.text_input("Nom à ajouter")

if st.button("Ajouter"):
    if not nouvelle_valeur.strip():
        st.warning("⚠️ Veuillez entrer un nom valide.")
    else:
        try:
            # Insert avec la v2 de supabase-py
            response = supabase.table("test-base").insert({"name": nouvelle_valeur}).execute()
            # Si on arrive ici, c'est que l'insertion a fonctionné
            st.success("✅ Nom ajouté avec succès!")
            st.write("Détails:", response.data)
        except Exception as e:
            # Toute erreur renvoyée par Supabase sera attrapée ici
            st.error(f"❌ Exception: {e}")
