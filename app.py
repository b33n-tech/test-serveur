import streamlit as st
from supabase import create_client, Client

# Debug des secrets
st.write("🔍 Debug des secrets")
st.write("Secrets disponibles:", list(st.secrets.keys()))
st.write("SUPABASE_URL présent?", "SUPABASE_URL" in st.secrets)
st.write("SUPABASE_KEY présent?", "SUPABASE_KEY" in st.secrets)

if "SUPABASE_URL" in st.secrets:
    st.write("URL value:", st.secrets["SUPABASE_URL"][:30] + "...")
if "SUPABASE_KEY" in st.secrets:
    st.write("KEY value:", st.secrets["SUPABASE_KEY"][:20] + "...")

# Connexion à Supabase
try:
    if "SUPABASE_URL" not in st.secrets or "SUPABASE_KEY" not in st.secrets:
        st.error("❌ Les secrets Supabase ne sont pas configurés")
        st.stop()
    
    url: str = st.secrets["SUPABASE_URL"]
    key: str = st.secrets["SUPABASE_KEY"]
    
    supabase: Client = create_client(url, key)
    
    st.success("✅ Connexion à Supabase réussie!")
    
except Exception as e:
    st.error(f"❌ Erreur: {str(e)}")
    st.stop()

# --- Ajout d'une entrée ---
st.write("## ➕ Ajouter une entrée à la table 'ma_table'")

# Saisie de l'entrée
nouvelle_valeur = st.text_input("Texte à ajouter")

if st.button("Ajouter"):
    if not nouvelle_valeur.strip():
        st.warning("⚠️ Veuillez entrer un texte valide.")
    else:
        try:
            # Remplace 'ma_table' par le nom réel de ta table
            response = supabase.table("ma_table").insert({"texte": nouvelle_valeur}).execute()
            
            if response.error:
                st.error(f"❌ Erreur lors de l'ajout: {response.error.message}")
            else:
                st.success("✅ Entrée ajoutée avec succès!")
                st.write("Détails:", response.data)
        except Exception as e:
            st.error(f"❌ Exception: {str(e)}")
