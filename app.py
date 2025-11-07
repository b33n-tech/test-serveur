import streamlit as st
import pandas as pd
from supabase import create_client

# Connexion Supabase (service role key)
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("📋 Gestion des appels à projets ESS")

# --- Ajouter une entrée ---
st.subheader("➕ Ajouter un nom")
nouveau_nom = st.text_input("Nom à ajouter")

if st.button("Ajouter"):
    if nouveau_nom.strip():
        try:
            supabase.table("test-base").insert({"name": nouveau_nom}).execute()
            st.success("✅ Nom ajouté !")
        except Exception as e:
            st.error(f"❌ Erreur : {e}")
    else:
        st.warning("⚠️ Veuillez entrer un nom valide.")

# --- Récupérer et afficher les données ---
try:
    response = supabase.table("test-base").select("*").execute()
    data = response.data  # liste de dicts
    df = pd.DataFrame(data)

    if not df.empty:
        st.subheader("📊 Liste des noms")
        st.dataframe(df.sort_values(by="name"))

        # --- Télécharger CSV ---
        csv = df.to_csv(index=False)
        st.download_button(
            label="⬇️ Télécharger CSV",
            data=csv,
            file_name="test-base.csv",
            mime="text/csv"
        )
    else:
        st.info("La table est vide.")
except Exception as e:
    st.error(f"❌ Impossible de récupérer les données : {e}")
