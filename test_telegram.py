import requests

def send_message(message):
    # Replace 'token' and 'chat_id' with your actual values
    token = '6902120953:AAF0DmINhkSFGNoLWRCq2Yb6ZLABZdwxphU'
    chat_id = '6393249406'
    
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, params=params)
    print(response, 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
    return response.json()

if __name__ == "__main__":
    # test_message = "This is a test message from the test_telegram script."
    response = send_message(test_message)
    print(response)
