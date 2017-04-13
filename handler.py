import json
import datetime
from forex_python.converter import CurrencyRates, CurrencyCodes


def convert(event, context):
    from_currency = event['pathParameters']['from'].upper()
    to_currency = event['pathParameters']['to'].upper()
    amount = int(event['pathParameters']['amount'])
    time = datetime.datetime.utcnow().isoformat()

    rate = CurrencyRates().get_rate(from_currency, to_currency)
    symbol = CurrencyCodes().get_symbol(to_currency)

    body = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "rate": rate,
        "result": rate * amount,
        "text": str(rate * amount) + symbol,
        "time": time + ' UTC'
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
