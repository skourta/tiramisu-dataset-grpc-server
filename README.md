# Tiramisu Dataset GRPC Server

This is a GRPC server for the Tiramisu dataset. It is written in Python and uses the [gRPC](https://grpc.io/) framework.

## Installation

1. Install Python 3.10 or higher
2. Install dependencies using poetry: `poetry install`


## Tests
1. Launch the server using: `python dataset_grp_server/server.py`
2. Run the tests using: `pytest`

###  Notes!

> **The tests require the server to be running.**

> **The save path of the datasets needs to be empty for the final test to pass.**
## Usage
Launch the server using: `python dataset_grp_server/server.py`

## Example

An example of a client can be found in `examples/client.py`.

To launch the example client, run: `python examples/client.py` after launching the server.