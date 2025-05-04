# 🛡️ Data Anonymization Tool for Privacy Protection

This Python-based tool anonymizes sensitive data in a CSV file using **Differential Privacy** and **K-Anonymity** techniques. It’s ideal for researchers, data scientists, and developers who need to protect personal information in datasets while preserving analytical value.

## 🔍 Features

- ✅ **Differential Privacy** for numerical data
- ✅ **K-Anonymity Techniques** for categorical data:
  - Suppression
  - Generalization
  - Synthetic Replacement
- 📁 Reads input from `data.csv`
- 💾 Outputs anonymized data as `anonymized_pakistan_housing.csv`

---

## 📂 How It Works

1. **Checks** for the existence of `data.csv`.
2. **Prompts** the user to input privacy settings:
   - Epsilon value for numerical columns.
   - Anonymization method for each categorical column.
3. **Applies** the selected privacy-preserving transformations.
4. **Saves** the anonymized dataset for further use.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed with the following libraries:

```bash
pip install pandas numpy
```

### Usage

1. Place your original dataset as `data.csv` in the same directory.
2. Run the script:

```bash
python Assignment.py
```

3. Follow the interactive prompts to configure privacy settings.
4. An anonymized version will be saved as `anonymized_pakistan_housing.csv`.

---

## 📘 Example

If your dataset has:

- Numerical columns like `Age`, `Income`
- Categorical columns like `City`, `Occupation`

You will be prompted to enter:
- A privacy level (epsilon) for each numerical column.
- An anonymization method (1-3) for each categorical column.

Example prompt:
```
Enter epsilon (privacy level) for numerical column 'Income': 0.5
Choose anonymization method used for 'City':
1) Suppression
2) Generalization
3) Synthetic Replacement
```

---

## ⚠️ Important Notes

- Ensure `data.csv` is in the **same folder** as `Assignment.py`.
- Epsilon values must be **greater than 0**. Lower values mean higher privacy.
- Choose appropriate anonymization techniques depending on the nature of the data and use case.

---

## 📄 Output

The processed data will be saved as:

```
anonymized_pakistan_housing.csv
```

This file contains the privacy-preserving version of your original dataset.

---

## 🧠 Concepts Used

- **Differential Privacy**: Adds statistical noise to protect individual data points.
- **Suppression**: Replaces values with asterisks.
- **Generalization**: Masks values partially (e.g., only keeps the first few characters).
- **Synthetic Replacement**: Replaces categories with generated labels.

---

## 🤝 Contributing

Feel free to fork, improve, or adapt this script to suit your needs. Pull requests are welcome!

---

## 📧 Contact

For questions or suggestions, open an issue or contact the repository maintainer.
