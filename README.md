# Super tiny and basic Python backend

![](https://github.com/stackbuilders/tiny-python-fullstack/workflows/Flask/badge.svg)

This application just consumes the [Github Public API](https://developer.github.com/v3/) in order to get a specific user information.

## Setup

Create and activate the virtual environment

```bash
virtualenv venv
source venv/bin/activate
```

Run the server

```bash
python app.py
```

The server will be up on http://localhost:5000. To try this out just make a POST request to the `/info` endpoint providing any `user` form parameter. Example:

```bash
curl -XPOST 'localhost:5000/info' -d 'user=stackbuilders'
```

## Requirements

Python >= 3.6

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)
