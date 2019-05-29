FROM python:3
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /confiscated_ms

# Set the working directory to /confiscated_ms
WORKDIR /confiscated_ms

# Copy the current directory contents into the container at /confiscated_ms
ADD . /confiscated_ms/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN chmod +x waitforMYSQL.sh
CMD ["waitforMYSQL.sh"]

EXPOSE 4003
