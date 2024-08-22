import streamlit as st
pip install --upgrade pip

# Function to calculate the score based on the ideal exchange rate
def calculate_score(amount, exchange_rate):
    ideal_rate = 0.5  # Set the ideal exchange rate to 0.5%

    # Calculate the deviation from the ideal rate
    deviation = abs(exchange_rate - ideal_rate)

    # A basic scoring function where the score decreases as the deviation increases
    score = int(999 - (deviation * 2000 * amount))

    # Ensure the score stays within the range 0 to 999
    if score > 999:
        score = 999
    elif score < 0:
        score = 0

    return score

# Streamlit app layout
st.title('Currency Exchange Score Calculator')

# Dropdowns for currency selection
from_currency = st.selectbox('From Currency', ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY'])
to_currency = st.selectbox('To Currency', ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY'])

# Input fields for amount and exchange rate
amount = st.number_input('Amount Sending', min_value=0.0, value=1000.0)
exchange_rate = st.number_input('Exchange Rate', min_value=0.0, value=1.0)

# Calculate score when the button is clicked
if st.button('Calculate Score'):
    score = calculate_score(amount, exchange_rate)
    st.write(f'Your score for this transaction is: **{score}** / 999')
