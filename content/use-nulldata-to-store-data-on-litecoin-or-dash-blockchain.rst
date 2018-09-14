Use Nulldata to store data on the Bitcoin Blockchain
====================================================

:date: 2018-09-14 08:45
:modified: 2018-09-14 08:45
:tags: litecoin, dash, bitcoinlib, blockchain, nulldata, op_return, data
:category: BitcoinLib
:slug: use-nulldata-to-store-data-on-litecoin-or-dash-blockchain
:authors: Lennart Jongeneel
:summary: Use nulldata outputs to store data on the Litecoin or Dash blockchain
:language: en


Store data on Litecoin or Dash blockchain
-----------------------------------------

In a previous article we described
`how to store data on the Bitcoin Blockchain <{filename}/use-nulldata-to-send-blockchain-messages.rst>`_.
But another and perhaps cheaper option is to store data on the Litecoin or Dash blockchain.
Both blockchains allow Null Data Transactions just as the bitcoin protocol.

A Null Data Transaction looks just like a normal transaction. But instead of sending value the output is a
data string, an OP_RETURN byte followed by some data. The transaction still needs an input, an unspent output of
a previous transaction to cover the transactions fees.


Send a Data Transaction
-----------------------

As far as I know there is no GUI wallet offering the option to send a data transaction at the moment,
but with some code and the `Python BitcoinLib <{filename}/python-bitcoin-library.rst>`_
it is easy to do.

.. code-block:: python

    from bitcoinlib.transactions import Output
    from bitcoinlib.wallets import wallet_create_or_open
    from bitcoinlib.encoding import varstr

    wallet = wallet_create_or_open('ExpensiveDatabase', network='litecoin')
    wk = wallet.get_key()
    wallet.utxos_update()
    utxos = wallet.utxos()

    if not utxos:
        print("Please deposit to %s to start creating Nulldata transactions" % wk.address)
    else:
        lock_script = b'\x6a' + varstr(b'This is message for the Litecoin network')
        t_output = Output(0, lock_script=lock_script)
        print(wallet.send([t_output]).hash)

The locking script of the Null Data output starts with the OP_RETURN opcode (HEX 6A) followed by the data string.
The data string can contain anything you like, a size byte is added by the varstr() method.


Find your message
-----------------

When your successfully broadcasted your message transaction to the Litecoin network the script above return a
transaction ID. With this ID or the address you can look it up on a block explorer such as Chain.so:
https://chain.so/tx/LTC/1e57b40392edaa6a64d9e5df3d8729a679e9d9205daf575fd71d1bd2d18c0005

The OP_RETURN output is marked as 'nonstandard' but you can read the decoded message.

Not all nodes and Service providers accept Nulldata transactions or accept only Nulldata with a
maximum size of 40 bytes. If you encounter this problem, you could set up your own node and use
this or specify an service provider when sending the transaction.

To push transaction with a specific provider add the following line to the script above before
the wallet.send([t_output]) action. You can substitute 'chainso' for any other working provider.

.. code-block:: python

    wallet.providers = ['chainso']


Create a Data Transaction for the Dash network
----------------------------------------------

To create a Nulldata transaction for the Dash network simply replace 'litecoin' in the script above with 'dash'.
The Dash, Litecoin and Bitcoin network have the same specifications for Nulldata transactions.

This is an example of a Dash Nulldata transaction:
https://chain.so/tx/DASH/96dfdba1b214609ecb6db577c4f39d2daa36742e41da76e3dc9bcfe909b867ba


Where can this be used for?
---------------------------

Besides tagging the blockchain with your graffiti this has some useful applications. The blockchain
is a timestamped database of records which cannot be modified or deleted after they are included in the
blockchain. This is nice (and necessary) for storing value but can also be used to prove existence of a document
on a specific date: a renting contract or birth certificate for instance.

On the Proof Of Existence website (https://poex.io) you can store a hash of any document, which proves the existence of
a document on a specific data. And in my article: "
`Proof existence of documents using Nulldata <{filename}/proof-existence-store-documents-hash-blockchain.rst>`_ "
I explain how to do this yourself with BitcoinLib.

But Null Data messages can also be used to build another layer on the blockchain network to store assets
or other crypto currencies. Colored coins (https://en.wikipedia.org/wiki/Colored_coin)
or Counterparty (https://counterparty.io) are examples of this.
