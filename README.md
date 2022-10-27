<h1 align="center">Xetia Point Service</h1>

### Tech-Stack
- Framework: [Fastapi](https://fastapi.tiangolo.com/)
- ORM: [Tortoise-ORM](https://tortoise.github.io)
- ASGI Server: [Uvicorn](https://www.uvicorn.org/)
- Migration Tool: [Aerich](https://github.com/tortoise/aerich)
- Test Framework: [PyTest](https://docs.pytest.org/)

### Setup Development Environment
1. Setup virtual environtment [venv](https://docs.python.org/3/tutorial/venv.html) or [virtaulenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
2. clone this repo
3. install requirements dependency by `pip -r requirements.txt` or `poetry install`
4. start database and other required app, primarily postresql and redis (available in docker compose)
5. copy `template.env` and rename to `.env` then fill-in required field
6. Generate and run migration when you need to
7. **if you are running on Windows, i highly recommend to setup development env inside WSL**, because some of used library doesn't works well in Windows
8. to start development app run
    ```shell
    uvicorn index:app --port 8000 --reload --reload-exclude .docker/ --reload-exclude database/migration
    ```

### Contribution Rule
1. Respect other contributors
2. Comment any `todo`, `bug`, `fixme` if you find something to do with the code
3. Use linter if you can for easy code maintenance and readability
4. Write code as clear as you can, avoid complex code if you can make it simple.
5. Never copy-paste a code from the internet withot knowing what it does.
6. Communication is key to build successfull app. So you need to talk to other contributor if find some difficulty.

### Branching strategy
Everytime you need to change somthing inside, always create a new branch then send a *pull request*, branch name should prefixed by what current change is point to e.g `fix.errors_not_found`, `hotfix.wrong_path`, `feat.new_feature`. and **please always write a good commit message**

---
<p align="center">*** Happy Coding ***</p>
# fastapi-boilerplate
