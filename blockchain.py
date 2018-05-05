# Libraries

import datetime
import hashlib
import json
from flask import Flask, jsonify

# Structure of Blockchain

class Blockchain:
    
    def __init__(self):
        self.blockchain = []
        self.createBlock(proof = 1, prevHash = '0')
    
    def createBlock(self, proof, prevHash):
        block = {
            'index': len(self.blockchain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'prevHash': prevHash
        }
        self.blockchain.append(block)
        return block
    
    def getPrevBlock(self):
        self.blockchain[-1]
    
    def proofOfWork(self, prevProof):
        newProof = 1
        checkProof = False
        while checkProof is False:
            encryption = hashlib.sha256(str(newProof - prevProof).encode()).hexdigest()
            if encryption[:4] == '0000':
                checkProof = True
            else:
                newProof += 1
        return newProof
        
    def hash(self, block):
        encodedBlock = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()
    
    def isBlockchainValid(self, blockchain):
        prevBlock = blockchain[0]
        blockIndex = 1
        while blockIndex < len(chain):
            block = blockchain[blockIndex]
            if block['prevHash'] != self.hash(prevBlock)
                return False
            prevProof = prevBlock['proof']
            proof = block['proof']
            encryption = hashlib.sha256(str(proof - prevProof).encode()).hexdigest()
            if encryption[:4] != '0000'
                return False
            prevBlock = block
            blockIndex += 1
            
# Mines Blockchain

# Builds Web App

# Builds Blockchain

