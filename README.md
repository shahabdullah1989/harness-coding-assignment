## FastAPI Template

### Setup

- Create a virtual environment: `python -m venv venv`
- Enable the virtual env: `source ./venv/bin/activate`
- Install the dependencies: `pip install -r requirements.txt`

### Commands

- Run the server: `python3 src/server.py`
- Run unit tests: `pytest`
- Validate your OpenAPI schema: `openapi-spec-validator api/openapi.yaml`

### Configuration

All of the properties are defined in the dictionary `config/__init__.py` which are imported and used throughout the project. These property values are also read from a `.env` file, so copy the `.env.example` and edit as needed.

### Routes

Routes are written in the controllers folder.

### Models 

The models folder is for database classes.

### API Documentation

/api/openapi.yaml is the schema documentation for your API. FastAPI also generates an OpenAPI/Swagger HTML view at `localhost:8000/docs`.

### Validation

Before committing changes of the OpenAPI file, you can verify it with:

`openapi-spec-validator api/openapi.yaml`
