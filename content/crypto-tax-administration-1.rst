Crypto Administration 2 - Recreate old wallets
==============================================

:date: 2019-11-19 21:16
:modified: 2019-11-19 23:15
:tags: tax, administration, cryptocurrency, recreate, wallets, bitcoinlib, bitcoin
:category: BitcoinLib
:slug: crypto-tax-administration-2-recreate-old-wallets
:authors: Lennart Jongeneel
:summary: Recreate old wallets for your tax administration with Bitcoinlib
:language: en


.. :slug: crypto-tax-administration-2-recreate-old-wallets:

It's much easier to create a new cryptocurrency wallet then opening a bank account, so it can happen you have
created a lot of wallets during your bitcoin career. And as a logical result you might miss some information
from old wallets.

But if you still remember a couple of addresses you can recreate the wallet and all of its transactions with
`Python Bitcoin library <{filename}/python-bitcoin-library.rst>`_ by creating a new readonly wallet.

.. image:: /images/bitcoin-tax.png
   :width: 824px
   :alt: Pay bitcoin taxes!
   :align: center

Setup readonly wallet
---------------------

If you have the public master key or public account key, you can use that key to setup a readonly wallet with
bitcoinlib. The wallet below uses the bitcoin testnet3 network, but you can also specify the bitcoin, litecoin or dash
network.

.. code-block:: python

    from bitcoinlib.wallets import wallet_create_or_open

