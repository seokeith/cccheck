import streamlit as st

def calculate_score(exchange_rate, amount, ideal_rate=0.5):
    """
    Calculate the score for the given exchange rate and amount.
    The score is out of 999, with penalties for higher potential money loss due to non-ideal exchange rates.
    
    :param exchange_rate: The actual exchange rate as a percentage.
    :param amount: The amount of currency being sent.
    :param ideal_rate: The ideal exchange rate (default is 0.5%).
    :return: The score out of 999.
    """
    # Calculate the difference between the actual and ideal rate
    difference = abs(exchange_rate - ideal_rate)
    
    # Calculate potential money lost due to non-ideal exchange rate
    potential_loss = (difference / 100) * amount
    
    # Define the maximum possible loss (arbitrarily set for scaling)
    max_loss = amount * 0.10  # Assuming a 10% difference is the worst case
    
    # Calculate the raw score
    raw_score = max(0, 1 - (potential_loss / max_loss))
    
    # Scale the raw score to be out of 999
    score = int(raw_score * 999)
    
    return score, potential_loss

def main():
    st.title("Currency Exchange Scoring App")
    
    # User inputs
    currency = st.text_input("Enter the currency code (e.g., USD, EUR):", "USD")
    amount = st.number_input("Enter the amount to send:", min_value=0.0, value=1000.0, step=0.01)
    exchange_rate = st.number_input("Enter the exchange rate in %:", min_value=0.0, value=0.5, step=0.01)
    
    if st.button("Calculate Score"):
        # Get the score and potential loss
        score, potential_loss = calculate_score(exchange_rate, amount)
        
        # Display the result
        st.subheader("Results")
        st.write(f"**Currency**: {currency}")
        st.write(f"**Amount**: {amount}")
        st.write(f"**Exchange Rate**: {exchange_rate}%")
        st.write(f"**Potential Money Lost**: ${potential_loss:.2f}")
        st.write(f"**Score**: {score}/999")

if __name__ == "__main__":
    main()
