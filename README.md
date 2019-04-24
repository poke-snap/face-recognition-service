# Face Recognition Service

The Face Recognition Service is a Machine Learning Application that extracts faces from a given image and learns a face encoding mapped to a given username. It is responsible for being able to add, classify, and identify new faces to the model on the fly. It is designed as a Microservice that utilizes a REST API to invoke any of its functions. It is also responsible for saving image files to a given Filesystem (e.g. AWS S3).

## Getting Started

### Prerequisites
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/)

### Installation

Run the following command(s):

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Deployment
The project is intended to be built as a Docker image and deployed as a container.

You can build the project with 
```
docker build .
```

Then run it using
```
docker run <image-name>
```

## Built With
- Flask
- face_recognition

## License
[MIT](https://github.com/poke-snap/face-recognition-service/blob/master/LICENSE)

