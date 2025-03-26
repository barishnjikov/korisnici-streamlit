import streamlit as st
import gspread
import pandas as pd

spajanje = gspread.service_account('credentials.json')
list = spajanje.open('korisnici').sheet1

st.title("Aplikacija za evidenciju korisnika")

ime = st.text_input("Ime korisnika:")
email = st.text_input("E-mail korisnika:")
godine = st.number_input("Godine:", 1, 100)

if st.button("Dodaj korisnika"):
    list.append_row([ime, email, godine])
    st.success(f"Korisnik uspješno dodan!")

def prikaži_korisnike():
    korisnici = list.get_all_records()
    df = pd.DataFrame(korisnici)

    if df.empty:
        st.info("Nema korisnika u tablici.")
        return None
    else:
        df.index = df.index + 2
        st.dataframe(df)
        return df

st.subheader("Svi korisnici:")
df = prikaži_korisnike()

if df is not None:
    st.subheader("Brisanje korisnika")

    redak_za_brisanje = st.number_input("Unesi redni broj korisnika za brisanje:", 
                                        min_value=int(df.index.min()), 
                                        max_value=int(df.index.max()))

    if st.button("Obriši korisnika"):
        list.delete_rows(redak_za_brisanje)
        st.success("Korisnik uspješno obrisan!")

        prikaži_korisnike()

