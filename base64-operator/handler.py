import base64
import binascii
import json

operations = {
    1: 'decode',
    2: 'encode'
}

def turn_to_bytes(msg):
    try:
        byte_message = bytes(msg, 'ascii') 
    except Exception as err:
        raise Exception(err)
    else:
        return byte_message


def decode_message(msg):
    try:
        decoded = base64.b64decode(msg, validate=True)
    except Exception as err:
        raise Exception(err)
    else:
        return decoded


def encode_message(msg):
    try:
        encoded = base64.b64encode(msg)
    except Exception as err:
        raise Exception(err)
    else:
        return encoded


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    try:
        data = json.loads(req)
        op = data['operation']
        msg = data['message']

        msg = turn_to_bytes(msg)

        if op == operations[1]:
            result = decode_message(msg)
        elif op == operations[2]:
            result = encode_message(msg)
        else:
            raise Exception(f'Unknonw operation: {op}')
        
        if type(result) != bytes:
            raise Exception(f'Unexpected result. Result should be bytes.'
                            f' Received result: {type(result)}')
        
        response = result.decode('ascii')

    except json.JSONDecodeError as err:
        return (f'[ERROR] Error while trying to decode JSON. Traceback: {err}')
    except Exception as err:
        return (f'[ERROR] Error while trying to execute function.'
                f' Traceback: {err}')
    else:
        return json.dumps({'response': response})