Store Documents or Hashed Data on the Blockchain
================================================

:date: 2018-07-12 06:43
:modified: 2018-07-12 06:43
:tags: bitcoin, bitcoinlib, blockchain, nulldata, document hash, proof of existence
:category: BitcoinLib
:slug: proof-existence-store-documents-hash-blockchain
:authors: Lennart Jongeneel
:summary: Proof existence of documents by storing a document hash on the blockchain using the Python BitcoinLib
:language: en


Besides storing value the Blockchain can be used to store small amounts of arbitrary data.
This could be used to store a document hash to proof its existence on a particular date.

This article explains how to store a document hash on the blockchain or a full compressed message.
We do this using a Nulldata transaction, you can read the full details in this article:
`Use Nulldata to Store Data on the Blockchain <{filename}/use-nulldata-to-send-blockchain-messages.rst>`_


1. Create a document hash in Python
-----------------------------------

First let's create a hash of the document. The script below splits the document in blocks of 64Kb so very
large documents can be read as well. The SHA1 algorithm is used to create the hash, you can easily replace this
with another algorithm if you wish.

.. image:: /images/bitcoin-logo.png
   :width: 191px
   :alt: Bitcoin Logo
   :align: center

Create a hash of this bitcoin logo PNG image file:

.. code-block:: python

    from hashlib import sha1

    FILENAME = '/home/guest/Documents/bitcoin-logo.png'
    BLOCKSIZE = 65536

    # Get document hash
    hasher = sha1()
    with open(FILENAME, 'rb') as f:
        buf = f.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(BLOCKSIZE)
    document_hash = hasher.hexdigest()
    print("Hash of %s is %s" % (FILENAME, document_hash))


When you run this script it should return the following output:
.. code-block:: code

    Hash of /home/guest/Documents/bitcoin-logo.png is f6e4f3701cc1ab4695195d809d5a54d8cb3a87aa


2. Store document hash on the blockchain
----------------------------------------

Now store the document hash from the previous step in a transaction output on the Blockchain.

The following script creates a wallet and a deposit address where you have to make a deposit
for the transaction fees.

.. code-block:: python

    from bitcoinlib.transactions import Output
    from bitcoinlib.wallets import wallet_create_or_open
    from bitcoinlib.encoding import varstr

    FEE_PER_TRANSACTION = 0.00005000
    DOCUMENT_HASH = 'f6e4f3701cc1ab4695195d809d5a54d8cb3a87aa'

    wallet = wallet_create_or_open('Messenger')
    wk = wallet.get_key()
    wallet.utxos_update()

    if not wallet.utxos():
        print("Please deposit %.8f Bitcoin to %s to create a Nulldata transaction" % (FEE_PER_TRANSACTION, wk.address))
    else:
        lock_script = b'\x6a' + varstr(DOCUMENT_HASH)
        t = wallet.send([Output(0, lock_script=lock_script)])
        t.info()

Once the deposit has been received the transaction will be created and
pushed to the network.

.. code-block:: none

    Transaction aff2e75be2b82cc179058bbc0255a96310e55b2956fa827a3776c64d6fe91f4d
    Date: None
    Network: bitcoin
    Status: unconfirmed
    Verified: True
    Inputs
    - 18KovL8EsjGGXo1ja4jcMihytbJcjd5sCw 1000 06d0cc8c8f85d7b10d02df8ff3abc5527e746760b19e7af9e2b656c6dc91e7b3 0
      Script type: p2pkh, signatures: 1 (1 of 1)
    Outputs
    - NULLDATA  b'\xf6\xe4\xf3p\x1c\xc1\xabF\x95\x19]\x80\x9dZT\xd8\xcb:\x87\xaa'
    Fee: 1000
    Confirmations: 0
    Pushed to network: True
    Wallet: Messenger


3. Proof existence of a document with the blockchain
----------------------------------------------------

To proof existence of the document on a particular date you need to have the original document and
the transaction ID.

Redo the first step to create a hash of the document. Then retrieve the transaction from the blockchain
and compare the document hash with the Nulldata output.

.. code-block:: python

    txid = 'aff2e75be2b82cc179058bbc0255a96310e55b2956fa827a3776c64d6fe91f4d'
    document_hash = 'f6e4f3701cc1ab4695195d809d5a54d8cb3a87aa'

    srv = Service()
    t = srv.gettransaction(txid)

    found = False
    for o in t.outputs:
        if o.script_type == 'nulldata':
            tx_doc_hash = to_hexstring(o.lock_script[2:])
            if tx_doc_hash == document_hash:
                found = True

    if found:
        print("Existence of document with hash %s proofed in transaction with ID %s on %s" %
              (document_hash, txid, t.date))

If they match you have proofed the document existed on the time the transaction was confirmed.

.. code-block:: none

    Existence of document with hash f6e4f3701cc1ab4695195d809d5a54d8cb3a87aa proofed in transaction with
    ID aff2e75be2b82cc179058bbc0255a96310e55b2956fa827a3776c64d6fe91f4d on 2018-07-12 05:57:59
