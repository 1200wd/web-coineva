Guide: Create a safe offline wallet without printer
===================================================

:date: 2018-02-23 21:54
:modified: 2018-02-23 21:54
:tags: bitcoin, litecoin, paper wallet, no printer, passphrase, bitcoinlib, guide
:category: How To
:slug: create-safe-offline-wallet-without-printer
:authors: Lennart Jongeneel
:summary: Create a (almost) 100% safe offline crypto currency vault on an offline system without using a printer
:language: en


What's wrong with a printer?
----------------------------

Many things. Most printers contain a large storage device which remembers all printed documents for a indefinite amount
of time. There are good changes you communicate to your printer via a wireless network which packages can be easily
intercepted in various ways. And almost all modern printers are online, continuously connected to the internet and
safety is not high on the list of priorities of most printer manufacturers.

So if you print an offline 'super secure' paper wallet it could be intercepted and emptied before the print is
finished or the funds could disappear after 5 years when your dump your printer in the garbage and someone is so
clever to check the hard drive in the printer.


Steps to create an offline wallet: Prepare Laptop
=================================================

First you need a old PC or laptop which you can miss and keep offline. Install a fresh copy of Linux OS such as
Debian or Ubuntu on it and then install the Python BitcoinLib. See https://github.com/1200wd/bitcoinlib

Ubuntu allows you to encrypt your home folder or the full disc. It is advised to use this option, but select a
strong encryption password and do not forget it.

.. code-block:: bash

   pip install bitcoinlib

Look at http://bitcoinlib.readthedocs.io/en/latest/_static/manuals.install.html for detailed installation instructions.

To show QR codes in the terminal you can optionally install a python QR code module

.. code-block:: bash

   pip install qrcodelib

Disclaimer: The Python Bitcoin Library BitcoinLib has been tested and used extensively but is still in Alpha
development phase. To use it technical knowledge is required and a basic understanding of python is recommended.
Please use carefully and at your own risk.


Next Step: Create a secure offline Wallet
=========================================

After your laptop is configured and the BitcoinLib is working take if offline so we can create a new secure wallet.

Go to the tools directory of BitcoinLib, create a new wallet and generate an address to receive funds.

.. code-block:: bash

   cli-wallet mywallet-priv

Type 'y' to create an new wallet and write down to passphrase to at least 2 pieces of paper as backup. You can
recreate a wallet with one of these pieces of papers if you lose access to your PC/Laptop


.. code-block:: bash

   lennart@c:~$ cli-wallet mywallet-priv
   Command Line Wallet for BitcoinLib

   Wallet mywallet-priv does not exist, create new wallet [yN]? y

   CREATE wallet 'mywallet-priv' (bitcoin network)

   Your mnemonic private key sentence is: erase burden model museum upgrade ozone foster oyster maximum visit clump vendor

   Please write down on paper and backup. With this key you can restore your wallet and all keys

   Type 'yes' if you understood and wrote down your key: yes
   Updating wallet
   Wallet info for mywallet-priv
   === WALLET ===
    ID                             4
    Name                           mywallet-priv
    Owner
    Scheme                         bip44
    Main network                   bitcoin

   = Wallet Master Key =
    ID                             88
    Private                        True
    Depth                          0

   - NETWORK: bitcoin -
   - - Keys
      88 m                            12Wmiym4ZrVpH6esSBgt8RDudQzajEdWpc            mywallet-priv                        0.00000000 BTC
      89 m/44'                        16RbR7bnLfWzyeqM8CEXRDfe42sHbj73DT            mywallet-priv                        0.00000000 BTC
      90 m/44'/0'                     1KGasy1LRjNt9iTwZ3Lqj1TtdjPoxuZsMK            mywallet-priv                        0.00000000 BTC
      91 m/44'/0'/0'                  1BihnPy8QaUNejqkpLyKYFpLQGJfo6GZw7            Account #0                           0.00000000 BTC
      92 m/44'/0'/0'/0                1MtocyALJoUuVSFFbjYYPDNJUusNkAiXyC            Account #0 Payments                  0.00000000 BTC
      93 m/44'/0'/0'/1                1LwXXHVP5qSR9AhvPiuErN7V32Ydcz2Xte            Account #0 Change                    0.00000000 BTC
      94 m/44'/0'/0'/0/0              1AJgdgd9wP3egy81vbehtqpZnTqQK5xqnc            Key 0                                0.00000000 BTC
      95 m/44'/0'/0'/0/1              19vURyBHiEjvRaHJfx763ZgGsq4fxxGJ9d            Key 1                                0.00000000 BTC
      96 m/44'/0'/0'/0/2              1F7ZezH5WcsDWzdvU7P2fHpGejzE1amDiT            Key 2                                0.00000000 BTC
      97 m/44'/0'/0'/0/3              1KPoQczLocAPVmX6zeV4qMvdS9rXkvJoYK            Key 3                                0.00000000 BTC
      98 m/44'/0'/0'/0/4              18oEp47qMujEc6gAcTQN81c3E4LtpHp1Q5            Key 4                                0.00000000 BTC
      99 m/44'/0'/0'/1/0              1FRQnuKxoJ9zbueHGpPp9Rr8MEad9zXhp             Change 0                             0.00000000 BTC
     100 m/44'/0'/0'/1/1              1JrqD41KF2v32nAxfFhYjVGejcSM3jCiDS            Change 1                             0.00000000 BTC
     101 m/44'/0'/0'/1/2              19Nto3ms62o9ELRuDkDmtmh1mVPpofwC3q            Change 2                             0.00000000 BTC
     102 m/44'/0'/0'/1/3              1MH1HZ2fU5ZRHyf5yGy4YWvZ7Aah3YD2hq            Change 3                             0.00000000 BTC
     103 m/44'/0'/0'/1/4              17hZkiMZELjPQmFR3TTAFkFyi9q9QBEgGq            Change 4                             0.00000000 BTC

   - - Transactions (Account 0, xpub6D8CV1m9LQJSvV24i6SVLGVecb9J9oC3n2p5UnspRPFBp52q7tL8cW4TqCUNcFfB7PB7zJwor2X9oRYSV7KPBTjBBdVgd57pcsTmFqurov4)

   = Balance Totals (includes unconfirmed) =

Now copy your public account key WIF showed in the wallet info on the line starting with '- - Transactions'. In this case:
xpub6D8CV1m9LQJSvV24i6SVLGVecb9J9oC3n2p5UnspRPFBp52q7tL8cW4TqCUNcFfB7PB7zJwor2X9oRYSV7KPBTjBBdVgd57pcsTmFqurov4


Create an online wallet
=======================

On your online PC create an online public wallet using the public account key from the offline wallet

.. code-block:: bash

   cli-wallet mywallet-pub -c xpub6CZhfzY66MTQFXuwMoKNUJWeBY152kPEFASoESfvgLj2SzeF7DZZN64UKv9foLNQ5STxyMEfWWXon6J7oVBFyw7nmDqpahWbWGF3HQkj9fp

A new wallet has been created and all key addresses should be the same.

The public wallet is a watch-only wallet it cannot sign and send transaction. But with the public wallet you can:
- Create new addresses (keys)
- View your balance
- Download transactions and unspent outputs
- Create new unsigned transactions

Receive a payment
=================

Now send funds to a wallet's receive address. Show an available address with:

.. code-block:: bash

   cli-wallet mywallet-pub -r

If you have installed the qrcodelib you can now scan the QR code with another online application to get the
address so you can transfer funds to your wallet.

Your wallet will be updated when you call cli-wallet without extra options. Once you have send the funds they
should show with:

.. code-block:: bash

   cli-wallet mywallet-pub


Create a transaction
====================

Now on create a transaction with your online wallet like this:

.. code-block:: bash

   cli-wallet mywallet-pub -t 1GXErvQ8Wrd7T92aDV67x4U2YFic8Fz4v5 40000

This will output a transaction overview with a python dictionary style output and a raw transaction hash. Now copy
the raw transaction to your offline PC.

Traceback (most recent call last):
  File "/home/lennart/.local/bin/cli-wallet", line 11, in <module>
    sys.exit(main())
  File "/home/lennart/.local/lib/python3.5/site-packages/bitcoinlib/tools/cli_wallet.py", line 240, in main
    t = wlt.transaction_import_raw(args.import_raw)
  File "/home/lennart/.local/lib/python3.5/site-packages/bitcoinlib/wallets.py", line 2694, in transaction_import_raw
    rt = self.transaction_create(t_import.outputs, t_import.inputs, network=network)
  File "/home/lennart/.local/lib/python3.5/site-packages/bitcoinlib/wallets.py", line 2598, in transaction_create
    to_hexstring(prev_hash), address))
bitcoinlib.wallets.WalletError: UTXO 32e90c36ea81a7fa4cbf3634cdcb1dfe0a44a5199731ed71c123456be8790546 and key with address  not found in this wallet




Now if you would like to spend funds from your offline wallet you have to:
* create a transaction on your online PC then
* sign it on your offline PC, export the raw transaction and
* push the transaction to the network on a online PC

