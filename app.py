import streamlit as st
from supabase import create_client, Client

try:
    # Vérifier que les secrets existent
    if "SUPABASE_URL" not in st.secrets or "SUPABASE_KEY" not in st.secrets:
        st.error("❌ Les secrets Supabase ne sont pas configurés")
        st.stop()
    
    url: str = st.secrets["SUPABASE_URL"]
    key: str = st.secrets["SUPABASE_KEY"]
    
    # Créer le client
    supabase: Client = create_client(url, key)
    
    st.success("✅ Connexion à Supabase réussie!")
    
    # Test simple pour vérifier la connexion
    # Remplacez 'votre_table' par une vraie table de votre base
    # response = supabase.table('votre_table').select("*").limit(1).execute()
    # st.write("Données de test:", response.data)
    
except Exception as e:
    st.error(f"❌ Erreur de connexion: {str(e)}")
    st.write("Type d'erreur:", type(e).__name__)
