# LAYA (Jev's Open Source Alternative)

# Install Packages
You need `Python` installed.

```
pip install torch laya huggingface_hub
```

# Download Laya Model

```
python download_model.py
```

# Run the Program

```
python first.py
```

# First Example

### I was charged twice. Please refund the duplicate payment.

Which team should handle this message?

'billing':'payments, duplicate charges, refunds',

'technical':'software errors, bugs, login problems',

'sales':'pricing or buying the product',

'other':'unclear request or none of these'

## Output

```
{
  "type": "choice",
  "choice": "billing",
  "probabilities": {
    "billing": 0.9806,
    "technical": 0.0062,
    "sales": 0.0061,
    "other": 0.007
  },
  "confidence": 0.9157,
  "answer_confidence": 0.9806,
  "action": {
    "act_probability": 1.0
  }
}
```

`Billing` is the correct answer.