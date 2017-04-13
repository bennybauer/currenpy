# Currenpy
[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)

Currency conversion service running on AWS Lambda using [Serverless Framework](https://github.com/serverless/serverless).

The service exposes the following API endpoint:

| **Endpoint** |**Description**|
|-------|------|
| `GET /convert/{from}/{to}/{amount}` | Converts `amount` of `from` currency to `to` currency   |

Example:

`GET /convert/usd/eur/250` will convert 250$ into Euros.

Response:
```json
{
  from: "USD",
  text: "235.1825€",
  rate: 0.94073,
  to: "EUR",
  amount: 250,
  result: 235.18249999999998,
  time: "2017-04-13T19:57:26.385252 UTC"
}
```


## Usage
## Setup
| **Step** | **Command** |**Description**|
|---|-------|------|
|  1. | `npm install -g serverless` | Install Serverless CLI  |
|  2. | Set up an AWS account with admin permissions | [Documentation](https://github.com/serverless/serverless/blob/master/docs/02-providers/aws/01-setup.md)  |
|  3. | `npm install` | Installs dependencies (`serverless-python-requirements`)  |


## Development
| **Step** | **Command** |**Description**|
|---|-------|------|
|  1. | `virtualenv convert` | Create virtual environment |
|  2. | `pip install -r requirements.txt` | Install dependencies|


## Deployment

	sls deploy

# Credits
* [forex-python](https://github.com/MicroPyramid/forex-python)
* [serverless-python-requirements](https://www.npmjs.com/package/serverless-python-requirements) by [@schep_](https://twitter.com/schep_)

