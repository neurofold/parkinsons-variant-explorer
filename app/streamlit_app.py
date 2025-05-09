import streamlit as st
from src.ai_lit_agent import fetch_pubmed_abstracts, summarize_with_llm
from src.run_fold_prediction import simulate_structure_prediction
from src.compare_structures import calculate_rmsd
import streamlit.components.v1 as components
import py3Dmol

def render_pdb_structure(pdb_content, style="cartoon"):
    view = py3Dmol.view(width=800, height=500)
    view.addModel(pdb_content, "pdb")
    view.setStyle({style: {}})
    view.zoomTo()
    return view

st.title("🧬 Parkinson’s Variant Explorer")

# Sequence input & prediction
gene = st.text_input("Enter Gene (e.g., PINK1)", "PINK1")
if st.button("Fetch Variants"):
    st.write("🔍 Variants fetching not implemented in this version.")

sequence = st.text_area("Protein Sequence", "MKTAYIAKQRQISFVKSHFSRQ")
if st.button("Run Prediction"):
    pdb_path = simulate_structure_prediction(sequence)
    st.success(f"Predicted structure saved to: {pdb_path}")

# RMSD Comparison
st.header("🔬 Compare Protein Structures (RMSD)")
pdb1 = st.file_uploader("Upload Wild-Type Structure (.pdb)", type="pdb")
pdb2 = st.file_uploader("Upload Mutated Structure (.pdb)", type="pdb")

if st.button("Compare Structures") and pdb1 and pdb2:
    wt_path = f"data/processed/{pdb1.name}"
    mut_path = f"data/processed/{pdb2.name}"
    with open(wt_path, "wb") as f:
        f.write(pdb1.getvalue())
    with open(mut_path, "wb") as f:
        f.write(pdb2.getvalue())

    try:
        rmsd_value = calculate_rmsd(wt_path, mut_path)
        st.success(f"RMSD: {rmsd_value} Å")
    except Exception as e:
        st.error(f"Error comparing structures: {e}")

# 3D Visualization
st.header("🔬 Visualize 3D Structure")
pdb_file = st.file_uploader("Upload PDB file to visualize", type="pdb")
if pdb_file:
    pdb_content = pdb_file.read().decode("utf-8")
    st.text_area("📄 PDB Content Preview", pdb_content[:1000], height=150)
    view = render_pdb_structure(pdb_content)
    components.html(view._make_html(), height=500)

# Literature Mining
st.header("🔍 Literature Summary from PubMed")
query = st.text_input("Enter a gene/protein to search literature", "PINK1")
max_results = st.slider("Number of papers", 1, 10, 3)

if st.button("Get Summary"):
    with st.spinner("Searching PubMed and summarizing..."):
        abstracts = fetch_pubmed_abstracts(query, max_results)
        if abstracts:
            summary = summarize_with_llm(abstracts, query)
            st.subheader("📘 Summary")
            st.write(summary.content)
        else:
            st.warning("No abstracts found.")
