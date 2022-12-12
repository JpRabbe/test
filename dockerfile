
FROM python:3

RUN pip install scikit-learn streamlit joblib

WORKDIR app/

COPY model_dashboard.py .
COPY regression.joblib .

CMD streamlit run model_dashboard.py
