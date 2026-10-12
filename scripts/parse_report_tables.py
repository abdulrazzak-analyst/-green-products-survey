"""
Turns the 26 result tables in Chapter 4 of the report into one tidy CSV.
Source: report/04_Data_Analysis_and_Interpretation.pdf (needs `pdftotext` from poppler).
Run:  python scripts/parse_report_tables.py
"""
import csv, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "report", "04_Data_Analysis_and_Interpretation.pdf")
OUT = os.path.join(ROOT, "data", "survey_results_tidy.csv")

# table no -> (questionnaire question no, section, short question)
META = {
    "4.1": (2, "Demographics", "Gender"),
    "4.2": (3, "Demographics", "Age group"),
    "4.3": (4, "Demographics", "Educational qualification"),
    "4.4": (5, "Demographics", "Marital status"),
    "4.5": (6, "Demographics", "Occupation"),
    "4.6": (7, "Demographics", "Area of residence"),
    "4.7": (8, "Demographics", "Monthly income"),
    "4.8": (9, "Awareness", "How respondents came to know about green products"),
    "4.9": (10, "Usage behaviour", "Product used before green products"),
    "4.10": (11, "Usage behaviour", "Reason for choosing green products"),
    "4.11": (12, "Usage behaviour", "Amount spent on green products"),
    "4.12": (13, "Usage behaviour", "How often green products are purchased"),
    "4.13": (14, "Usage behaviour", "Frequency of using green products"),
    "4.14": (15, "Usage behaviour", "Green product used most frequently"),
    "4.15": (16, "Usage behaviour", "Reason for purchasing green products"),
    "4.16": (17, "Usage behaviour", "Place of purchase"),
    "4.17": (18, "Usage behaviour", "Green product currently used"),
    "4.18": (19, "Barriers", "Reason for not purchasing green products"),
    "4.19": (20, "Usage behaviour", "Most popular green product category"),
    "4.20": (21, "Attitude", "Experienced benefits from green products"),
    "4.21": (22, "Awareness", "Aware of environmental impact of products"),
    "4.22": (23, "Attitude", "Believes information on product package"),
    "4.23": (24, "Awareness", "Can differentiate between green products"),
    "4.24": (26, "Attitude", "Purchase behaviour towards green products (agreement scale)"),
    "4.25": (25, "Attitude", "Green products will reduce pollution"),
    "4.26": (27, "Attitude", "Consumer preference for green products (frequency scale)"),
}
# labels that wrap onto a second line in the PDF text
FIX = {"Based on its": "Based on its requirements", "Don’t like purchasing": "Don’t like purchasing others",
       "Personal care": "Personal care products"}

txt = subprocess.run(["pdftotext", "-layout", PDF, "-"], capture_output=True, text=True, check=True).stdout
parts = re.split(r"TABLE NO:\s*([0-9.]+)", txt)
rows, problems = [], []
for i in range(1, len(parts), 2):
    no, body = parts[i], parts[i + 1]
    seg = body.split("(Source")[0]
    found = []
    for line in seg.splitlines():
        m = re.match(r"^\s*(.+?)\s+(\d+)\s+(\d+)\s*$", line)
        if m and not re.search(r"respondents|percentage", m.group(1), re.I):
            found.append((FIX.get(m.group(1).strip(), m.group(1).strip()), int(m.group(2)), int(m.group(3))))
    total = [f for f in found if f[0].lower() == "total"]
    options = [f for f in found if f[0].lower() != "total"]
    q, section, question = META[no]
    if sum(o[1] for o in options) != 100 or (total and total[0][1] != 100):
        problems.append(f"Table {no}: counts sum to {sum(o[1] for o in options)}")
    for label, count, pct in options:
        if count != pct:
            problems.append(f"Table {no} {label}: count {count} != percent {pct}")
        rows.append(["T" + no, q, section, question, label, count, pct])

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["table_no", "questionnaire_q", "section", "question", "option", "respondents", "percent"])
    w.writerows(rows)
print(f"{len(set(r[0] for r in rows))} tables, {len(rows)} rows -> {OUT}")
print("problems:", problems or "none")
