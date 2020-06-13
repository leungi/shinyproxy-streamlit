FROM python:3.7
RUN pip install streamlit
COPY . /app
WORKDIR /app
EXPOSE 8501
# ENTRYPOINT ["streamlit","run"]
CMD ["streamlit", "run", "app.py", "--server.port=8501"]