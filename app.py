import streamlit as st
from supabase import create_client, Client

# Connexion à Supabase avec service role key
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]  # <-- service role key
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
            # Nouvelle syntaxe supabase-py
            response = supabase.table("test-base").insert({"name": nouvelle_valeur}).execute()
            
            if response.status_code >= 400:
                st.error(f"❌ Erreur lors de l'ajout: {response.data}")
            else:
                st.success("✅ Nom ajouté avec succès!")
                st.write("Détails:", response.data)
        except Exception as e:
            st.error(f"❌ Exception: {str(e)}")
