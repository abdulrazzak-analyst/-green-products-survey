# Consumer Attitude and Awareness on Green Products
### A primary survey study (with special reference to Salem city)

B.Com research project, Sona College of Arts and Science, Salem. I designed a questionnaire, surveyed **100 consumers in Salem city**, and analysed how aware consumers are of green products, what drives their buying, and what stops them.

**Method:** primary survey (questionnaire) · random sampling · simple percentage analysis
**Data:** 26 result tables (28-item questionnaire), summarised in [`data/survey_results_tidy.csv`](data/survey_results_tidy.csv)

## Objectives
1. Assess the factors that encourage consumption of organic / green products in the study area.
2. Measure consumers' awareness of green products.
3. Analyse the challenges consumers face when using green products.
4. Offer suggestions to improve consumer awareness of green products.

## Key findings
| Theme | Finding | Source |
|---|---|---|
| Awareness | 77% know about the environmental impact of products | T4.21 |
| Awareness | Only 35% say they can clearly tell green products apart; 52% are "moderately aware", 13% unaware | T4.23 |
| Awareness | 63% first heard of green products through friends (36%) or social media (27%) | T4.8 |
| Attitude | 87% think green products will reduce pollution (48% "absolutely", 39% "possibly") | T4.25 |
| Attitude | 72% trust the information printed on green-product packaging | T4.22 |
| Attitude | 77% agree or strongly agree with the statements on purchase behaviour | T4.24 |
| Behaviour | 56% use green products frequently or very frequently; 5% never do | T4.13 |
| Why they buy | Quality (37%) and health (32%) lead; low price is the main reason for only 8% | T4.15 |
| Where they buy | Wholesalers 42%, departmental stores 35%, online 23% | T4.16 |
| Barriers | **Availability (39%) and limited choice (29%) matter more than price (22%)** | T4.18 |

**The gap in the data:** awareness and positive attitudes are high (77% and 77%), but regular use is lower (56%). The barriers table suggests the gap is more about availability and choice than about cost.

## Suggestions from the study
- Government and NGOs should run awareness programmes (street plays, television, debates) on green marketing and product benefits.
- Encourage buying eco-labelled products (for example star-rated appliances) and use clear, visible green logos on packaging.
- Keep the price gap between standard and green products small, and make green product quality at least as good.
- Build trust through transparency, and use customer feedback in product development.

## Repository contents
```
green-products-survey/
├── report/                 Full_Report.pdf, plus the five chapters as separate PDFs
├── questionnaire/          Questionnaire.pdf (the blank survey form)
├── data/
│   └── survey_results_tidy.csv
├── scripts/
│   └── parse_report_tables.py
└── README.md
```

## About the data
`survey_results_tidy.csv` holds the **aggregated results** from the 26 tables in Chapter 4 (one row per answer option). It does not contain individual respondent answers.

| Column | Meaning |
|---|---|
| `table_no` | Table number in the report (T4.1 to T4.26) |
| `questionnaire_q` | Question number in the questionnaire |
| `section` | Demographics, Awareness, Usage behaviour, Barriers or Attitude |
| `question` | Short question wording |
| `option` | Answer option |
| `respondents` | Number of respondents (out of 100) |
| `percent` | Percentage of respondents |

### Data notes
- **Table 4.11** (amount spent on green products) is reproduced as published: its four rows add up to 90 respondents although the printed total is 100.
- **Questions 26 and 27** of the questionnaire contain several statements or categories each. The report presents one combined distribution for each (T4.24 and T4.26), so per-statement results are not in this dataset.
- Table numbers are prefixed with `T` so that spreadsheet tools do not read `4.10` as `4.1`.

## Limitations
- Sample of 100 respondents from Salem city only; results cannot be generalised to all consumers.
- The sample skews young: 81% are under 30 and 50% are students.
- Responses depend on respondents' own recall.
- Analysis uses simple percentages only; no significance testing was done.
