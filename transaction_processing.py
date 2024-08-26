import datetime

# Error Handling with try-except
def process_transaction(transaction_data):
    try:
        if not isinstance(transaction_data, dict):
            raise ValueError("Transaction data must be a dictionary.")
        
        # Sample validation
        if 'amount' not in transaction_data or transaction_data['amount'] <= 0:
            raise ValueError("Invalid transaction amount.")
        
        # Simulate transaction processing
        print("Processing transaction...")
        print(f"Transaction successful: {transaction_data}")

    except ValueError as ve:
        log_error(f"ValueError: {ve}")
        print(f"Error: {ve}")
    except Exception as e:
        log_error(f"General Error: {e}")
        print(f"An unexpected error occurred: {e}")

# Validation
def validate_transaction_data(transaction_data):
    if 'amount' not in transaction_data or transaction_data['amount'] <= 0:
        raise ValueError("Invalid transaction amount.")
    if 'account_number' not in transaction_data or len(transaction_data['account_number']) != 10:
        raise ValueError("Invalid account number.")
    # Add more validation as needed

# Logging Errors
def log_error(error_message):
    with open('error_log.txt', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {error_message}\n")

# User Feedback
def user_feedback():
    while True:
        transaction_data = {}
        try:
            transaction_data['account_number'] = input("Enter account number (10 digits): ")
            transaction_data['amount'] = float(input("Enter transaction amount: "))

            validate_transaction_data(transaction_data)
            process_transaction(transaction_data)

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        cont = input("Do you want to process another transaction? (yes/no): ")
        if cont.lower() != 'yes':
            break

# Running the user interface
try:
    user_feedback()
except Exception as e:
    log_error(f"Critical Error: {e}")
    print(f"A critical error occurred: {e}")