# Madeleine Waldie
# CSCI 181 HW6

import random

# Assumptions:
# Assume you have access to everyone’s correct public key. 
# Public keys are also included in the recipient field of the transaction. 
# Also assume there is a function already implemented that verifies signatures and returns True or False: 
# boolean verifySignature(pubKey, message, signature)


# Create a PayCoin transaction data structure or class with all the fields it requires.

class Coin: # Coin structure comprised of num, value, recipient, and signature
    def __init__(self, num, value, recipient, signature):
        self.num = num
        self.value = value
        self.recipient = recipient

class PayCoinTransaction:
    # consumedCoins: an array of Coins
    # signatures: an array of signatures
    def __init__(self, consumedCoins):
        self.totalValue = 0
        self.consumedCoins = consumedCoins

        # Compute the total value of the consumed coins
        i = 0
        for coin in consumedCoins:
            self.totalValue += coin.value
            self.signatures[i] = coin.signature
            i += 1
        
        # Assign random values to the createdCoins
        j = 0
        valRemaining = self.totalValue
        while valRemaining > 0:
            self.createdCoins[j].num = j
            val = random.randrange(0, valRemaining)
            valRemaining -= val
            self.createdCoins[j].value = val
            j += 1


# Create the blockchain (ledger), (assume the data part of each block contains only one
# transaction of type PayCoin). You do not need to compute the hashes

class Block:
    # transaction: type of a PayCoinTransaction
    def __init__(self, transaction):
        self.transaction = transaction
        self.nextBlock = None

class Blockchain:
    def __init__(self):
        self.head = None

    # Add a block to the blockchain
    def addBlock(self, transaction):
        if isValidTransaction(transaction):
            newBlock = Block(transaction)
            if self.head is None:
                self.head = newBlock
            else:
                currentBlock = self.head
                while currentBlock.nextBlock is not None:
                    currentBlock = currentBlock.nextBlock
                currentBlock.nextBlock = newBlock

# Write a function that checks whether a given new transaction is valid or not. If valid
# then add it to the blockchain. The definition of “valid” transaction is in the lecture notes. 


def isValidTransaction(transaction):
    # Check if all the consumed coins are valid and have valid signatures
    for coin in transaction.consumedCoins:
        if not verifySignature(coin.recipient, coin.value, coin.signature):
            return False

    # Check if the total value of consumed coins matches the total value of created coins
    consumedValue = sum(coin.value for coin in transaction.consumedCoins)
    createdValue = sum(coin.value for coin in transaction.createdCoins)
    if consumedValue != createdValue:
        return False

    # Check if any of the consumed coins have already been consumed
    consumed_coin_nums = [coin.num for coin in transaction.consumedCoins]
    if len(consumed_coin_nums) != len(set(consumed_coin_nums)):
        return False

    # If all checks pass, the transaction is valid
    return True
