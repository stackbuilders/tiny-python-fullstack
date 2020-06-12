# Super tiny and basic Python backend

![](https://github.com/stackbuilders/tiny-python-fullstack/workflows/Flask/badge.svg)
![](https://github.com/stackbuilders/tiny-python-fullstack/workflows/React/badge.svg)

This application just consumes the [Github Public API](https://developer.github.com/v3/) in order to get a specific user information.

## Setup

### Back-end

Create and activate the virtual environment

```bash
virtualenv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
python app.py
```

The server will be up on http://localhost:5000. To try this out just make a POST request to the `/info` endpoint providing any `user` form parameter. Example:

```bash
curl -XPOST 'localhost:5000/info' -d 'user=stackbuilders'
```

### Front-end

Install dependencies

```bash
cd frontend
npm install
```

Run the application (create-react-app):

```bash
npm run start
```

## Requirements

- Python >= 3.6
- Node >= 12.x

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)
