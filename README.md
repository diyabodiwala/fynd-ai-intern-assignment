# Fynd AI Intern – Take Home Assessment

This repository contains my submission for the **Fynd AI Intern Take-Home Assessment**, covering both required tasks:

- **Task 1:** Rating Prediction via Prompting  
- **Task 2:** Two-Dashboard AI Feedback System (User + Admin)

---

## 📁 Repository Structure

├── task1_rating_prediction.ipynb # Task 1 notebook (prompting + evaluation)
├── streamlit_app.py # Task 2: Combined User & Admin dashboard
├── llm_utils.py # LLM helper functions
├── data_store.json # Shared data store for dashboards
├── requirements.txt
└── README.md


---

## ✅ Task 1 – Rating Prediction via Prompting

### Objective
Classify Yelp reviews into **1–5 star ratings** using **LLM prompting**, returning structured JSON output.

### Dataset
- Yelp Reviews Dataset (Kaggle):  
  https://www.kaggle.com/datasets/omkarsabnis/yelp-reviews-dataset
- A subset of ~200 reviews was sampled for evaluation.

### Prompting Approaches
Three prompting strategies were implemented and iteratively improved:
1. **Zero-shot prompting**
2. **Rule-based prompting**
3. **Few-shot prompting**

Each iteration was designed to improve output reliability, structured formatting, and prediction accuracy.

### Prompting Approaches

Three prompting strategies were implemented and iteratively refined to improve prediction accuracy, output reliability, and structured JSON compliance:

- **Zero-shot prompting**
- **Rule-based prompting**
- **Few-shot prompting**

Each subsequent prompt was modified based on observed shortcomings in the previous version.

---

### Prompt Iterations & Improvement Rationale

#### Zero-shot Prompt

The zero-shot prompt provided a minimal instruction asking the LLM to classify the Yelp review into a 1–5 star rating and return the result in JSON format.

**Why it was changed:**
- The model frequently produced verbose or unstructured responses
- JSON formatting was often invalid or missing
- Output consistency was very low across samples

This demonstrated that minimal instructions were insufficient for enforcing structured outputs.

---

#### Rule-based Prompt

The rule-based prompt introduced explicit sentiment-to-rating rules (e.g., very negative → 1 star, neutral → 3 stars) along with strict instructions to return only valid JSON.

**Why it was improved:**
- To reduce ambiguity in rating interpretation
- To constrain the model’s behavior
- To improve consistency and enforce output structure

**Observed improvement:**
- JSON validity increased significantly
- Outputs became more reliable and consistent
- Accuracy improved slightly due to clearer rating boundaries

---

#### Few-shot Prompt

The few-shot prompt added example input–output pairs demonstrating correct rating decisions and the required JSON structure.

**Why it was improved:**
- To show the model the expected reasoning pattern
- To improve semantic understanding of nuanced reviews
- To further increase prediction accuracy

**Observed improvement:**
- Achieved the highest accuracy among all prompts
- Maintained high JSON validity, with minor formatting deviations due to longer context

---

### Summary of Prompt Evolution

Each prompt iteration was motivated by empirical evaluation results:

- **Zero-shot → Rule-based:** Improved structure and reliability
- **Rule-based → Few-shot:** Improved semantic reasoning and accuracy

This highlights the trade-off between **strict output control** and **reasoning flexibility** when designing prompts for LLM-based systems.

---

## Evaluation Metrics

Each prompting approach was evaluated using the following metrics:

- **Accuracy:** Comparison of predicted star ratings against ground truth ratings.
- **JSON Validity Rate:** Percentage of LLM responses that were valid, parseable JSON.
- **Reliability & Consistency:** Stability of structured outputs across multiple samples.

These metrics were chosen to evaluate both **prediction quality** and **output robustness**, which are critical for real-world LLM-based systems.

---

## Results Summary

| Prompt Type | Accuracy | JSON Validity |
|------------|----------|---------------|
| Zero-shot | 0.533 | 0.075 |
| Rule-based | 0.579 | 0.975 |
| Few-shot | 0.625 | 0.800 |

---

## Key Insights from Task 1

- Zero-shot prompting is unreliable for tasks requiring strict output structure.
- Rule-based prompting significantly improves JSON compliance and consistency.
- Few-shot prompting achieves the best balance between semantic accuracy and structured output.
- There is a clear trade-off between **format reliability** and **reasoning flexibility**.

---

## Execution Note

Although each individual prediction returned structured JSON as specified in the output format, the notebook presents **aggregated evaluation metrics** (accuracy and JSON validity) for clarity and readability rather than printing raw JSON outputs for every review.

---

## Task 2 – Two-Dashboard AI Feedback System

### Objective

The objective of Task 2 is to build a web-based AI feedback system with two dashboards:

- **User Dashboard (Public-Facing)**
- **Admin Dashboard (Internal-Facing)**

Both dashboards must read from and write to the **same persistent data source** and leverage LLMs for intelligent responses and insights.

---

## System Architecture

- Implemented as a **single Streamlit web application**
- Role-based dashboards accessible via **sidebar navigation**
- **Shared data source:** `data_store.json`
- Ensures live updates and data consistency across dashboards

This design avoids synchronization issues and reflects production-ready application architecture.

---

## User Dashboard (Public-Facing)

The User Dashboard allows users to:

- Select a star rating
- Write a short textual review
- Submit feedback

### On Submission
- An **AI-generated user-facing response** is displayed
- The rating, review, and AI-generated outputs are stored persistently

---

## Admin Dashboard (Internal-Facing)

The Admin Dashboard displays a **live-updating list of all submissions**, including:

- User rating
- User review
- AI-generated summary
- AI-suggested recommended action
- Timestamp

---

## Admin Analytics

The Admin Dashboard also includes basic analytics such as:

- Total number of submissions
- Average user rating
- Overview of recent feedback trends

These analytics provide quick insights into customer sentiment.

---

## LLM Usage in Task 2

LLMs are used for the following purposes:

- Generating polite and contextual **user-facing responses**
- **Summarising customer feedback** for administrative review
- Suggesting **recommended next actions** for internal teams

Defensive parsing and fallback logic are implemented to handle malformed LLM outputs gracefully.

---

## Deployment

- The application is fully deployed as a **web-based Streamlit app**
- Both dashboards are accessible via **public URLs**
- The Admin Dashboard is accessed via sidebar navigation within the same app
- This ensures both dashboards operate on the same persistent data source

---

## Security Considerations

- No API keys are hard-coded in the repository
- Environment variables are used for sensitive configuration
- Task 1 LLM calls are disabled by default for safe evaluation
- Task 2 does not expose any secrets

---

## Conclusion

This project demonstrates:

- Iterative prompt engineering driven by empirical evaluation
- Reliable enforcement of structured LLM outputs
- Clean system design with shared persistence
- Robust handling of LLM variability
- Deployment-ready, production-aware implementation

All requirements of the Fynd AI Intern Take-Home Assessment are fully satisfied.

---


## Author

Diya Bodiwala
Submission for **Fynd AI Intern – Take Home Assessment**
