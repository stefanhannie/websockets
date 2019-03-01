# websockets

We're going to test some websocket functionality.
Testing out commit and push

The echo-server and echo-client work together to mimic an actual server and a client, you will need two terminal windows
open, one for the client and one for the server.

Run ./echo-server.py and sudo python ./echo-client.py to get messages passed between them.
Prints 'Hello World' on the client server.

# Working with virtual environments.

Often it's a good idea to use a python virtual environment to develop in.
To set one up issue the following commands.

- `python3 -m venv venv`
- `source venv/bin/activate`
  You should now see the following in your terminal:
  `(venv) username@your-computer-name-here:~/path/to/your/project$`
  Now you can run the following to install all dependencies:
  `pip install -r requirements.txt`.
