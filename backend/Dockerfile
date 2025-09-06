FROM python:3.12-alpine


WORKDIR /app

# Copy only requirements.txt first (better for caching)
COPY requirements.txt .

# install all dependencies
RUN pip install -r requirements.txt

ADD . .
# Expose port (Flask default is 5000)
EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]