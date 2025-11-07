import streamlit as st
from supabase import create_client, Client

# ---- CONFIGURATION SUPABASE ----
SUPABASE_URL = "https://TON_PROJECT_URL.supabase.co"  # 🔁 remplace
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZHN5dHNzZGVpdHJycmtudmZiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI1NDA1NzQsImV4cCI6MjA3ODExNjU3NH0.Qtdebvn-e1m-r3SvOmzAzqKk3k2MHs_QFA-CEe9pKrY"  # 🔁 remplace
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("🚀 Proto minimal - Supabase + Streamlit")

# --- Ajout d'une entrée ---
st.header("Ajouter un nom")
texte = st.text_input("Nom de l'entrée")

if st.button("Ajouter"):
    if not texte.strip():
        st.error("Merci de saisir un texte")
    else:
        res = supabase.table("offres").insert({"name": texte.strip()}).execute()
        if res.data:
            st.success(f"✅ Entrée ajoutée : {texte.strip()}")
        else:
            st.error("❌ Erreur lors de l'ajout")
        st.experimental_rerun()  # rafraîchit la page pour voir l'entrée

# --- Affichage des entrées ---
st.header("Liste des entrées")
docs = supabase.table("offres").select("*").execute().data

if not docs:
    st.info("Aucune entrée pour le moment")
else:
    for d in docs:
        st.write(f"- {d['name']}")
