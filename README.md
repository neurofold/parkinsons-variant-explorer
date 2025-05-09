```markdown
# 🧠 Parkinson’s Variant Explorer

**An AI-powered open-source platform to explore the impact of Parkinson’s disease-associated genetic mutations on protein structures using AlphaFold and LLM-driven literature synthesis.**

---

## 🧬 Overview

Parkinson’s disease (PD) is a progressive neurodegenerative disorder characterized by motor dysfunction and cognitive decline. A major hallmark of PD is the **misfolding and aggregation of proteins**—especially **alpha-synuclein**—driven by genetic mutations in key proteins like **SNCA, LRRK2, PINK1**, and **PARK7**.

Understanding how these mutations impact protein **structure and function** is essential for:
- Identifying drug targets
- Understanding molecular pathology
- Designing disease-modifying therapies

This project bridges **genomics**, **AI-based protein folding**, and **LLM-powered biomedical literature mining** to create an interactive tool for researchers and students.

---

## 💡 Key Features

| Feature                       | Description |
|------------------------------|-------------|
| 🔬 **Protein Structure Prediction** | Predict structures using AlphaFold via ColabFold |
| 🧠 **RMSD Comparison**        | Compare wild-type and mutant proteins to quantify structural deviation |
| 📘 **LLM-powered Literature Agent** | Summarize key scientific findings from PubMed |
| 🧪 **3D Structure Viewer**    | Visualize .pdb files interactively using py3Dmol |
| 📦 **Dockerized App**        | Easily deployable on any Docker-compatible host |

---

## 📚 Scientific Concepts

### 🔁 AlphaFold & Protein Folding
[AlphaFold](https://www.deepmind.com/research/highlighted-research/alphafold) is a deep learning system that predicts a protein’s 3D structure from its amino acid sequence. Structural prediction helps:
- Understand folding errors caused by mutations
- Identify functional domains
- Predict stability and binding regions

### ⚠️ Parkinson’s Disease & Mutations
Mutations in genes like:
- `SNCA` → produces alpha-synuclein, which forms toxic aggregates
- `PINK1` → involved in mitochondrial quality control
- `LRRK2` → linked to familial PD with kinase activity

Understanding the structure of these mutant proteins can lead to:
- Early diagnostics
- Drug screening
- Biomarker discovery

### 📚 PubMed & LLMs
We use [NCBI Entrez](https://www.ncbi.nlm.nih.gov/books/NBK25500/) to fetch abstracts and summarize them using **LangChain + OpenAI**, allowing users to extract insights from the latest research efficiently.

---

## 🖼️ Architecture Diagram

```

User Input
↓
+------------+        +----------------+       +----------------------+
\| Protein Seq| -----> |  AlphaFold via | --->  |  Predicted Structure |
\| or Variant |        |   ColabFold    |       |     (.pdb file)      |
+------------+        +----------------+       +----------------------+
↓                              ↓
↓                        +-------------------+
↓                        | RMSD Comparison   |
+-------------+               |  (WT vs Mutant)   |
\| PubMed Query| ------------> +-------------------+
↓
+---------------------+
\| LangChain + OpenAI  |
\| Research Summary     |
+---------------------+

````

---

## 🚀 Getting Started

### 🔧 Installation

#### Option A: Local Development
```bash
git clone https://github.com/yourname/parkinsons-variant-explorer.git
cd parkinsons-variant-explorer
python -m venv env
source env/bin/activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
````

#### Option B: Docker (Recommended)

```bash
docker build -t pd-explorer .
docker run -p 8501:8501 pd-explorer
```

---

## 📂 Directory Structure

```
parkinsons-variant-explorer/
├── app/
│   └── streamlit_app.py         # Streamlit UI
├── src/
│   ├── ai_lit_agent.py          # PubMed + LangChain summarizer
│   ├── compare_structures.py    # RMSD calculation
│   └── run_fold_prediction.py   # AlphaFold/ColabFold integration
├── data/                        # Upload your .pdb files here
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🧪 Example Use Cases

* Upload a wild-type and mutant `.pdb` of **PINK1** → compute RMSD
* Paste a sequence from `UniProt` → simulate AlphaFold prediction
* Enter query: `"LRRK2 Parkinson"` → get AI summary of latest research

---

## 🔐 Environment Variables

To use OpenAI with LangChain:

```bash
export OPENAI_API_KEY=your_openai_key
```

---

## 🌐 Suggested Datasets

* [UniProt PD-Related Proteins](https://www.uniprot.org/)
* [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) – mutation records
* [PDGene/DisGeNET](https://www.disgenet.org/)

---

## 🙌 Contributing

We welcome issues, PRs, and feature suggestions.

```bash
# Fork + PR
git checkout -b feature/my-awesome-feature
```

Areas for contribution:

* Real-time variant fetch from ClinVar
* Integrate PyMOL viewer
* Use Hugging Face `BioBERT` for local summarization

---

## 🧠 References

* DeepMind: [AlphaFold](https://deepmind.com/research/highlighted-research/alphafold)
* NIH: [Parkinson’s Disease Overview](https://www.ninds.nih.gov/parkinsons-disease)
* LangChain: [LangChain for Biomedical NLP](https://www.langchain.com/)
* py3Dmol: [Protein 3D Viewer](https://pypi.org/project/py3Dmol/)

---

## 📄 License

MIT License

---

## 👩‍🔬 Built for BioHackathons, Researchers, and Open Science Enthusiasts.

```
