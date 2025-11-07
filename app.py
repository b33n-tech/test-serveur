import streamlit as st

st.write("🔍 Debug des secrets")
st.write("Secrets disponibles:", list(st.secrets.keys()))
st.write("SUPABASE_URL présent?", "SUPABASE_URL" in st.secrets)
st.write("SUPABASE_KEY présent?", "SUPABASE_KEY" in st.secrets)

if "SUPABASE_URL" in st.secrets:
    st.write("URL value:", st.secrets["SUPABASE_URL"][:30] + "...")
if "SUPABASE_KEY" in st.secrets:
    st.write("KEY value:", st.secrets["SUPABASE_KEY"][:20] + "...")

# Votre code original
from supabase import create_client, Client

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
