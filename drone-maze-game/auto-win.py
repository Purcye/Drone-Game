import requests

def win(score):
    """
        Call endpoint to signal a game win
    """
    endpoint = '192.168.0.2'
    print("Sending win message with score: " + str(score))
    requests.get(f'http://{endpoint}/updatescore?game=coding&score=300')
    print(f"Win message sent to {endpoint}")

win(90)
