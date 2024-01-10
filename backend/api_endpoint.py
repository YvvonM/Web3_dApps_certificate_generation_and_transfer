from typing import Optional
from fastapi import FastAPI

from algosdk import account, encoding , mnemonic 
from algosdk.error import WrongChecksumError ,WrongMnemonicLengthError
from algosdk.v2client import algod , indexer

from schemes import * 

algod_client=algod.AlgodClient("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","http://localhost:4001") #Initializing the algod client
indexer_client=indexer.IndexerClient("","http://localhost:8980") #initializing the validator

app = FastAPI() #Create a base application instance

#creating an account
@app.get("/account")
def create_account():                                   # a function that creates an account
    private_key, address = account.generate_account()
    passphrase = mnemonic.from_private_key(private_key)

    return {"address":address,"passphrase":passphrase}

@app.get("/account/{Address}")   
def get_account_info(Address:str):              #Create a function that returns information about an account by its ID
    info=algod_client.account_info(Address)

    return {"Address":info}