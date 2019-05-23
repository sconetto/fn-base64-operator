# Base64-Operator

FaaS function to encode and decode base64 messages.

## Expected Message

This functions expects a JSON encoded as a string with the following keys:

```json
{
    "operation": "encode",
    "message": "encode this!"
}
```

The allowed operations are `encode` and `decode`.

## Deploy Function

You should have configured Open FaaS previously. Follow this steps to deploy you function:

```shell
faas-cli build -f base64-operator.yml
faas-cli deploy -f base64-operator.yml
```