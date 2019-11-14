Guide: Create a safe offline wallet without printer
===================================================

:date: 2018-04-09 21:54
:modified: 2018-04-09 21:54
:tags: bitcoin, litecoin, paper wallets, no printer, passphrase, bitcoinlib, manual
:category: Paper Wallets
:slug: create-safe-offline-wallet-without-printer
:authors: Lennart Jongeneel
:summary: Create a safe offline crypto currency wallet on an offline system without using a printer
:language: en


.. _create-safe-offline-wallet-without-printer:

What's wrong with a printer?
----------------------------

Many things. Most printers contain a large storage device which remembers all printed documents for a indefinite amount
of time. There are good changes you communicate to your printer via a wireless network which packages can be easily
intercepted in various ways. And almost all modern printers are online, continuously connected to the internet and
safety is not high on the list of priorities of most printer manufacturers.

So if you print an offline 'super secure' paper wallet it could be intercepted and emptied before the print is
finished or the funds could disappear after 5 years when your dump your printer in the garbage and someone is so
clever to check the hard drive in the printer.

.. image:: /images/noprinter.png
   :width: 1200px
   :alt: No printers
   :align: center

Steps to create an offline wallet: Prepare Laptop
-------------------------------------------------

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
-----------------------------------------

After your laptop is configured and the BitcoinLib is working take if offline so we can create a new secure wallet.

Go to the tools directory of BitcoinLib, create a new wallet and generate an addresses to receive funds:

.. code-block:: bash

   clw mywallet-priv -u

Type 'y' to create an new wallet and write down to passphrase to at least 2 pieces of paper as backup. You can
recreate a wallet with one of these pieces of papers if you lose access to your PC/Laptop


.. code-block:: bash

   lennart@c:~$ clw mywallet-priv -u
   Command Line Wallet for BitcoinLib

   Wallet mywallet-priv does not exist, create new wallet [yN]? y

   CREATE wallet 'mywallet-priv' (bitcoin network)

   Your mnemonic private key sentence is: toward music glory great faith sustain work length gossip easy dizzy clever

   Please write down on paper and backup. With this key you can restore your wallet and all keys

   Type 'yes' if you understood and wrote down your key: yes
   Updating wallet
   Wallet info for mywallet-priv
   === WALLET ===
    ID                             3
    Name                           mywallet-priv
    Owner
    Scheme                         bip44
    Main network                   bitcoin

   = Wallet Master Key =
    ID                             72
    Private                        True
    Depth                          0

   - NETWORK: bitcoin -
   - - Keys
      72 m                            1M4bY9QqkiJsmrAmpD611bksrPfjFoMbgY            mywallet-priv                        0.00000000 BTC
      73 m/44'                        1GZwumEZTXjxBwTpfaqCHwiNphpcXnydEM            mywallet-priv                        0.00000000 BTC
      74 m/44'/0'                     17zdAqPsqG57ztr5gAPk8dDTAArvxBoPKH            mywallet-priv                        0.00000000 BTC
      75 m/44'/0'/0'                  1M81iGJqXpXU2De4eutj3c1gSprqfUZbdJ            Account #0                           0.00000000 BTC
      76 m/44'/0'/0'/0                1GsmxzLQbBKXkUAEsxvRmQs3o3L5yRDvDc            Account #0 Payments                  0.00000000 BTC
      77 m/44'/0'/0'/1                1Jmv5EhGPMVVmG5Bn5PPq1ovkG9ccfocpT            Account #0 Change                    0.00000000 BTC
      78 m/44'/0'/0'/0/0              1DJT5PtdrkRvPUTaPXEmCjL7RzVBRsnuhL            Key 0                                0.00000000 BTC
      79 m/44'/0'/0'/0/1              1Bo1ZSw3rkqyoVLHGrD1TpnVWMZmV8eoCs            Key 1                                0.00000000 BTC
      80 m/44'/0'/0'/0/2              18bhdmbv5YDae7Aw28XtQuP8WJ47bPBzYS            Key 2                                0.00000000 BTC
      81 m/44'/0'/0'/0/3              126FWpggWSLAzQYcJ3zQCjh85ZKVv5VE3M            Key 3                                0.00000000 BTC
      82 m/44'/0'/0'/0/4              1Ay2KnQyyEEYfM1BoEpyQneqLZjAyZYzyd            Key 4                                0.00000000 BTC
      83 m/44'/0'/0'/1/0              1Pq9ZANWmSXsMgdjsiMcmN2grdog6MKRv6            Change 0                             0.00000000 BTC
      84 m/44'/0'/0'/1/1              1Lnrdad7ZPK7G6ysgDuUhsc3e43SCCgkDM            Change 1                             0.00000000 BTC
      85 m/44'/0'/0'/1/2              1CkiLqUq8bWhgf3vQKeGSSwVCsE5RFHc38            Change 2                             0.00000000 BTC
      86 m/44'/0'/0'/1/3              1HSYFNrgaa3Aoof9pz44Jy8w8iZAQE6cxZ            Change 3                             0.00000000 BTC
      87 m/44'/0'/0'/1/4              13295LYWJz2smeG1PbBDTA3LDdiPqmPUwT            Change 4                             0.00000000 BTC

   - - Transactions (Account 0, xpub6CDUND4VWCjyL4bYqY9ngbSrnmSeqTPtwqdDVQ8p5YYLhippqKiLFmbCHvP4ZbpE3C1DzkiAHMkWpycmY6kqhSvRHTCVWiyAYhA4j3StK8Q)

   = Balance Totals (includes unconfirmed) =

The '-u' option is to update transactions and in this case it is used to create new addresses / keys/

Now copy your public account key WIF showed in the wallet info on the line starting with '- - Transactions'. In this case:
xpub6C5F532enEXKa4Q8RFGVUeLwQ86BNCWaqMCgq8uSqxeRFtiAziDPYG9sH2SJB1dmzVAfTnZiWQNxBeXRcGSnyNc7rRD38Pe2vU5RW1o9mhK


Create an online wallet
-----------------------

On your online PC create an online public wallet using the public account key from the offline wallet. Use the '-u'
option again to creates a couple of new keys / addresses.

.. code-block:: bash

   clw mywallet-pub -u -c xpub6CZhfzY66MTQFXuwMoKNUJWeBY152kPEFASoESfvgLj2SzeF7DZZN64UKv9foLNQ5STxyMEfWWXon6J7oVBFyw7nmDqpahWbWGF3HQkj9fp

A new wallet has been created and all key addresses should be the same.

The public wallet is a watch-only wallet it cannot sign and send transaction. But with the public wallet you can:
- Create new addresses (keys)
- View your balance
- Download transactions and unspent outputs
- Create new unsigned transactions

Receive a payment
-----------------

Now send funds to a wallet's receive address. Show an available address with:

.. code-block:: bash

   clw mywallet-pub -r

If you have installed the qrcodelib you can now scan the QR code with another online application to get the
address so you can transfer funds to your wallet.

Your wallet will be updated when you call clw without extra options. Once you have send the funds they
should show on your online PC with:

.. code-block:: bash

   clw mywallet-pub -u


Create and send a transaction
-----------------------------

Now on create a transaction with your online wallet like this:

.. code-block:: bash

   lennart@c:~$ clw mywallet-pub -t 3LrXizKejCGYyGUxYzGweyuxFVtfs3odEe 100000
   Command Line Wallet for BitcoinLib

   Transaction created
   Transaction
   Date: None
   Network: bitcoin
   Status: new
   Verified: False
   Inputs
   - 1Ay2KnQyyEEYfM1BoEpyQneqLZjAyZYzyd 148414 db158f07381d9cc87ef27eed4ecb604b7405163e1ab4563e6c10537fc6aa6ee9 1
     Script type: p2pkh, signatures: 0 (1 of 1)
   Outputs
   - 3LrXizKejCGYyGUxYzGweyuxFVtfs3odEe 100000
   - 13295LYWJz2smeG1PbBDTA3LDdiPqmPUwT 46194
   Fee: 2220
   Confirmations: None
   Pushed to network: False
   Wallet: mywallet-pub

   Transaction created but not send yet. Transaction dictionary for export:
   {'fee': 2220,
    'inputs': [{'address': '1Ay2KnQyyEEYfM1BoEpyQneqLZjAyZYzyd',
                'output_n': 1,
                'prev_hash': 'db158f07381d9cc87ef27eed4ecb604b7405163e1ab4563e6c10537fc6aa6ee9',
                'signatures': [],
                'value': 148414}],
    'network': 'bitcoin',
    'outputs': [{'address': '3LrXizKejCGYyGUxYzGweyuxFVtfs3odEe', 'value': 100000},
                {'address': '13295LYWJz2smeG1PbBDTA3LDdiPqmPUwT', 'value': 46194}],
    'raw': '0100000001e96eaac67f53106c3e56b41a3e1605744b60cb4eed7ef27ec89c1d38078f15db0100000000ffffffff02a08601000000000017a914d237028e93ddb5e063c5f47685557e7b7265549e8772b40000000000001976a914162768737af6846894ec022692825c1e714f21de88ac00000000'}

This will output a transaction overview with a python dictionary style output. Copy the transaction dictionary to
your offline PC for instance with the help of an USB stick.

.. code-block:: bash

   clw mywallet-priv -a <path-to-usb>/txdict.txt

The transaction will be imported and signed by the offline wallet and the transaction information is showed. Copy the
raw transaction hash and save it to the USB stick.

To push the transaction to the network import the raw transaction on the online PC.

.. code-block:: bash

   clw mywallet-pub -i "0100000001e96eaac67f53106c3e56b41a3e1605744b60cb4eed7ef27ec89c1d38078f15db010000006b483045022100ed3681a573783a691f85311a5c4af6302742c331f049bf793b7d7eca30d2e60402201126c83895d1f3bd0f0e32a3d2e6fb2c22da11615e33282c7cb6d2b0de151505012102babad319637c497291a81ac53a84dd0485971303cc52ea635915640dc3cde097ffffffff02a08601000000000017a914d237028e93ddb5e063c5f47685557e7b7265549e8772b40000000000001976a914162768737af6846894ec022692825c1e714f21de88ac00000000" -p

And if transaction is successfully pushed you will receive a message like this:

.. code-block:: bash

   Transaction pushed to network. Transaction ID: 8606205a652d9340569444f728fddfb03acadd1d270063872b4e4bc5bd3d4291

When you open the wallet again you will see the updated balance and transaction.

Good luck,

Lennart

PS: There are still a little bit of sathosis left on this wallet with the private key shown above. If you are the first
one to find them: congratulations and drink a coffee or beer on me!