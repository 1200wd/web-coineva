Create a Litecoin Multisig Transaction
======================================

:date: 2018-05-16 19:11
:modified: 2018-05-16 19:54
:tags: litecoin, LTC, multisig, send transaction, create transaction, bitcoinlib, CL wallet
:category: BitcoinLib
:slug: create-litecoin-multisig-transaction
:authors: Lennart Jongeneel
:summary: Create a Litecoin Multisig Transaction with the 2-of-3 multisig wallet using the BitcoinLib Command Line Utility
:language: en


.. :slug: create-litecoin-multisig-transaction:


This guide assumes you `created a Litecoin 2-of-3 wallet <{filename}/create-litecoin-multisig-wallet.rst>`_
following the previous article.

We will create a Litecoin multisig transaction using the command line wallet from
`Python BitcoinLib <{filename}/python-bitcoin-library.rst>`_ with the online main wallet
and an offline wallet.


Create transaction with online wallet
-------------------------------------


..  == Create a transaction
    Update wallet and check balance (UTXO's)
    - cli-wallet LitecoinMS-on
    == Restore wallet from backup
    = Online wallet lost
    Online PC:
    create new temporary wallet with public keys and backup key
    create new multisig wallet
    transfer funds to new wallet (see create transaction section)
    = Offline wallet lost
    Online PC:
    create transaction
    create new multisig wallet
    Offline PC:
    sign transaction with backup key
    Online PC
    send tx to new wallet