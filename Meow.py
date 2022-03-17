import requests

class Truemoney:
    def __init__(self):
        self.phone_number = ""
        self.vouchers = ""
        self.__hearder = {
            "Content-Type": "application/json",
            "Accept": 'application/json',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }
    def refresh(self):
        response = requests.get(
            url=f"https://gift.truemoney.com/campaign/?v={self.vouchers}/",
            headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"},
        )
    
    def verify(self):
        response = requests.get(
            url=f"https://gift.truemoney.com/campaign/vouchers/{self.vouchers}/verify",
            headers=self.__hearder, 
            params={"mobile": self.phone_number}
        )
        if response.status_code == 200:
            print(response.json())
            return "verified"
        elif response.status_code == 400:
            print(response.json())
            return "used"
        else:
            return "have a problem"

    def get_money_go_go(self):
        response = requests.post(
            url = f"https://gift.truemoney.com/campaign/vouchers/{self.vouchers}/redeem",
            headers=self.__hearder,
            json={
                "mobile": self.phone_number,
                "voucher_hash": self.vouchers
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return "have a problem"

