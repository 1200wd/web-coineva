Use Nulldata to write messages on the Bitcoin Blockchain
========================================================

:date: 2017-10-12 11:14
:modified: 2018-04-27 21:22
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

    if not wallet.utxos():
        print("Please deposit to %s to start creating Nulldata transactions" % wk.address)
    else:
        lock_script = b'j' + varstr(b'Please leave a message after the beep')
        t = wallet.send([Output(0, lock_script=lock_script)])
        t.info()

The locking script of the Null Data output starts with the OP_RETURN opcode followed by the data string.
The data string can contain anything you like, a size byte is added by the varstr() method.


Read your message
-----------------

You can use the BitcoinLib to retreive transactions and read nulldata messages. Some blockexplorers such
as smartbit.au.com and btc.com also show decode nulldata messages.

I couldn't help it and embedded the Python script above in the bitcoin blockchain. The script has been
split up in seven parts as one nulldata script can only contain 80 bytes. And a transaction can only contain
one nulldata script, so seven transactions are needed. The first byte in the script is used to determine the
order.

Technically you can create a transaction with multiple nulldata scripts. Such a transaction is considered valid
but is non-standard and will be rejected by most bitcoin clients.


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


Just for fun
------------

The Python script above is embedded in plaintext format as Nulldata on the bitcoin blockchain.

The python script can be found in these 8 transactions:
`c6960cd3a688db18550c06b08ed744382cfc9abce63cf6f97981e4b61bba81dc
<https://www.smartbit.com.au/tx/c6960cd3a688db18550c06b08ed744382cfc9abce63cf6f97981e4b61bba81dc>`_,
`7af7bea324b9cf4d6692d7b63518c076c55616c7943310dec9c23b2435ca4609
<https://www.smartbit.com.au/tx/7af7bea324b9cf4d6692d7b63518c076c55616c7943310dec9c23b2435ca4609>`_,
`31328c4e23abd547e4b6f49546a584ed969ed9b106f177f06365ea8f2222d576
<https://www.smartbit.com.au/tx/31328c4e23abd547e4b6f49546a584ed969ed9b106f177f06365ea8f2222d576>`_,
`8f0551fd70fa8cb4a92121277fdab51e88856c669a1ae4a8143c1ccf1fce3d26
<https://www.smartbit.com.au/tx/8f0551fd70fa8cb4a92121277fdab51e88856c669a1ae4a8143c1ccf1fce3d26>`_,
`2bb9e14d2005bd633e632399c702bcbd8438f0a4ea636400a6efceb14b8d14d0
<https://www.smartbit.com.au/tx/2bb9e14d2005bd633e632399c702bcbd8438f0a4ea636400a6efceb14b8d14d0>`_,
`055a22998664a6ffb5bddb7db38933bded2442c22991ea76dd363a1265ec4967
<https://www.smartbit.com.au/tx/055a22998664a6ffb5bddb7db38933bded2442c22991ea76dd363a1265ec4967>`_,
`da6fc4129b7fcd1c79fe9d96cb128c9edca897090048ff7b136ffcaf3baf50c6
<https://www.smartbit.com.au/tx/da6fc4129b7fcd1c79fe9d96cb128c9edca897090048ff7b136ffcaf3baf50c6>`_.
