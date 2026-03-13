# Telangana PDS Analytics

This project shows how to analyze and visualize data for Telangana Fair Price Shops using Python.

## What is included
- `app.py`: A Streamlit dashboard to view clustering of shops and see a map.
- `module.ipynb`: A Jupyter notebook with data loading, cleaning, clustering, and plots.
- CSV files with shop, transaction, and card data.

## How to set up (beginner friendly)
1. Make sure you have Python installed (version 3.8+).i]'[
2. eDX vbml,9ihjm z CVXU'=-[PIK,M 
3. Open a terminal (PowerShell) in this folder.
4. Install required packages:

<img src="Screenshot 2026-03-13 142936.png" alt="Description" width="600" height="400">
<img src="Screenshot 2026-03-13 142943.png" alt="Description" width="600" height="400">
<img src="Screenshot 2026-03-13 142951.png" alt="Description" width="600" height="400">

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## How to run the dashboard
In the same folder, run:

```powershell
streamlit run app.py
```

Then open the link shown in the terminal (usually http://localhost:8501).

## How to run the notebook
1. Install Jupyter if you don't have it:

```powershell
python -m pip install jupyter
```

2. Start Jupyter:

```powershell
jupyter notebook
```

3. Open `module.ipynb` in your browser.

## Notes
- If you add new data files, make sure they match the column names used in the code.
- If you see errors about missing packages, run the install command again.
