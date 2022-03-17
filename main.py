from fastapi import FastAPI
from Meow import Truemoney
import time

app = FastAPI()
truemoney = Truemoney()

@app.post("/money")
def get_money_i_sus_money(phone: str):
    truemoney.phone_number = phone
    if truemoney.verify() == "verified":        
        data = truemoney.get_money_go_go()
        time.sleep(1)
        truemoney.refresh()
        time.sleep(1)
        truemoney.verify()
        return {"data": data}
    return {"Msg": "เกิดไรไม่รู้ช่างแม่งแต่ใช้ไม่ได้"}
    

@app.post("/set_voucher")
def vouchers(voucher: str):
    truemoney.vouchers = voucher
    return {"status":"ตั้ง voucher ละ"}

