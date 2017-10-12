Use Nulldata to write messages on the Bitcoin Blockchain
========================================================

:date: 2017-10-12 11:14
:modified: 2017-10-12 11:18
:tags: bitcoin, bitcoinlib, blockchain, nulldata, op_return, message
:category: BitcoinLib
:slug: use-nulldata-to-send-blockchain-messages
:authors: Lennart Jongeneel
:summary: How to send messages or store data on the Bitcoin blockchain
:language: en


Blockchain to Send and Store Data
---------------------------------

Not many people know that besides transacting and storing value, the bitcoin blockchain offers
an option to send data and store small amounts of data in the blockchain.

To store data in the blockchain you just send a transaction, but instead of sending it to another bitcoin
address you send a Null Data transaction with a zero value output. So 1 of the outputs does not contain
an amount and address, but a message and an amount of zero.

A Null Data transaction and consists of an OP_RETURN byte followed by the lenght of the and then
the actual 0 to 80 bytes of data.

The output amount of the Null Data output is zero, but the transaction still requires an input with enough value
to cover the transaction fees.


How to Send a Message Transaction
---------------------------------

As far as I know there is no GUI wallet offering the option to send a data transaction at the moment,
but with some code and the `Python BitcoinLib <{filename}/python-bitcoin-library.rst>`_
it is easy to do.

.. code-block:: python

    from bitcoinlib.transactions import Output
    from bitcoinlib.wallets import wallet_create_or_open
    from bitcoinlib.encoding import varstr

    wallet = wallet_create_or_open('Messenger')
    wk = wallet.get_key()
    wallet.utxos_update()
    utxos = wallet.utxos()

    if not utxos:
        print("Please deposit to %s to start creating Nulldata transactions" % wk.address)
    else:
        lock_script = b'j' + varstr(b'Please leave a message after the beep')
        t_output = Output(0, lock_script=lock_script)
        print(wallet.send([t_output]))

The locking script of the Null Data output starts with the OP_RETURN opcode followed by the data string.
The data string can contain anything you like, a size byte is added by the varstr() method.


Where can this be used for?
---------------------------

Besides tagging the blockchain with your graffiti this has some useful applications. The blockchain
is a timestamped database of records which cannot be modified or deleted after they are included in the
blockchain. This is nice (and necessary) for storing value but can also be used to prove existence of a document
on a specific date: a renting contract or birth certificate for instance.

On the Proof Of Existence website (https://poex.io) you can store a hash of any document, which proves the existence of
a document on a specific data.

But Null Data messages can also be used to build another layer on the blockchain network to store assets
or other crypto currencies. Colored coins (https://en.wikipedia.org/wiki/Colored_coin)
or Counterparty (https://counterparty.io) are examples of this.
