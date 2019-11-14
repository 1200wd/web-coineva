Create a Litecoin Multisig Transaction
======================================

:date: 2018-05-23 10:11
:modified: 2019-11-14 22:55
:tags: litecoin, multisig, bitcoinlib, commandline wallets, manual
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

.. image:: /images/litecoin-transactions.jpg
   :width: 495px
   :alt: Litecoin Multisig Transaction
   :align: right

Create transaction with online wallet
-------------------------------------

First update your wallet and unspent transaction outputs:

.. code-block:: bash

    $ clw LitecoinMS-on -x
    Command Line Wallet - BitcoinLib 0.4.11

    Wallet info for LitecoinMS-on
    === WALLET ===
     ID                             39
     Name                           LitecoinMS-on
     Owner
     Scheme                         bip32
     Multisig                       True
     Multisig Wallet IDs            40, 41, 42
     Cosigner ID                    0
     Witness type                   legacy
     Main network                   litecoin
     Latest update                  2019-11-14 22:57:24.785464

    = Multisig Public Master Keys =
        0 261 Ltub2VECoJe5hBU8kNinfTfFsyPz5qfDMiFhPmmWi89yMBGJH9MtjZk6zmhcmvg8FXm3ZBDRibocbSfFzGaczfrUjWT4ZsXNhbCchwr48MZgXyS bip32  main     *
        1 266 Ltub2UpT1zg3aS9mgDSoxF1KxXTFWQWJdySpgtQ8WMRX7pFX7BXfshnMjRP4LqApSVETddt6B9NBnjW4XqhWPprZXKfKk9oWEmUV8MsoVZ3EW5f bip32  cosigner
        2 270 Ltub2V3tPynSv6pHv8tjXE3chMuDNybh1DmQXuKQ9bALUZ1Zw811u9PFS6QyEcKrC72PmK8rSyb1mv1mRHjTt22UrtmsP1hmrvTWz4vdPDZMUvR bip32  cosigner
    For main keys a private master key is available in this wallet to sign transactions. * cosigner key for this wallet

    - NETWORK: litecoin -
    - - Keys
      280 m/45'/0/0/0                  MFvNqhAWJY58yjLAME5V6ppivh9iVJJ6TH            Multisig Key 276/265/279             0.03266639 LTC

    - - Transactions (Account 0, Ltub2SSUS19CirucWsPQ8ekikRQ5BKr3FiQBfPUHoW4p9LP9MT7ifG5HBJvR3kkowxFm8aXiMSXXgRQfZHVGQCDWyMnBvnsDUzMkKT9eBQnt1nk)
      10 9a9b4c9c9decefd50b7f40c3a243bbd514a18958cda70aa4fe9f82e0726e4d2f   MFvNqhAWJY58yjLAME5V6ppivh9iVJJ6TH        1       3266639 U

    = Balance Totals (includes unconfirmed) =
    litecoin             (Account 0)                0.03266639 LTC

If unspent transaction outputs are found you can create a transaction. We create a transaction
to send 0.01 LTC to another address.

.. code-block:: bash

    $ clw LitecoinMS-on -t LgaczM5X63xd7QNnKrLjLK4rhrSQqfxuKv 1000000
    Command Line Wallet for BitcoinLib

    Transaction created
    Transaction
    Date: None
    Network: litecoin
    Status: new
    Verified: False
    Inputs
    - MFvNqhAWJY58yjLAME5V6ppivh9iVJJ6TH 3266639 9a9b4c9c9decefd50b7f40c3a243bbd514a18958cda70aa4fe9f82e0726e4d2f 0
      Script type: p2sh_multisig, signatures: 1 (2 of 3)
    Outputs
    - LgaczM5X63xd7QNnKrLjLK4rhrSQqfxuKv 1000000
    - 3LPmJ7DLR9v4ax6cSdPtgMB9jh7CDQ4Y64 2209347
    Fee: 57292
    Confirmations: None
    Pushed to network: False
    Wallet: LitecoinMS-on

    Transaction created but not send yet. Transaction dictionary for export:
    {'fee': 57292,
     'inputs': [{'address': 'MFvNqhAWJY58yjLAME5V6ppivh9iVJJ6TH',
                 'output_n': 0,
                 'prev_hash': '9a9b4c9c9decefd50b7f40c3a243bbd514a18958cda70aa4fe9f82e0726e4d2f',
                 'signatures': [{'pub_key': '0364170e13312e6a2a867ce65e868a5539d53ed79017943f95059a2525fef5bb0f',
                                 'sig_der': '304502210091ddefdd9b18e036b0fe930a395914522f189c812c40fbbfbfe0d9936e645bfb022064c29a3fb85f0fac6ae0debeff410aca8c310c339def1ffa0e47b63a68b89f1a',
                                 'signature': '91ddefdd9b18e036b0fe930a395914522f189c812c40fbbfbfe0d9936e645bfb64c29a3fb85f0fac6ae0debeff410aca8c310c339def1ffa0e47b63a68b89f1a'}],
                 'value': 3266639}],
     'network': 'litecoin',
     'outputs': [{'address': 'LgaczM5X63xd7QNnKrLjLK4rhrSQqfxuKv',
                  'value': 1000000},
                 {'address': '3LPmJ7DLR9v4ax6cSdPtgMB9jh7CDQ4Y64',
                  'value': 2209347}],
     'raw': '01000000012f4d6e72e0829ffea40aa7cd5889a114d5bb43a2c3407f0bd5efec9d9c4c9b9a00000000b50048304502210091ddefdd9b18e036b0fe930a395914522f189c812c40fbbfbfe0d9936e645bfb022064c29a3fb85f0fac6ae0debeff410aca8c310c339def1ffa0e47b63a68b89f1a014c6952210364170e13312e6a2a867ce65e868a5539d53ed79017943f95059a2525fef5bb0f21038de68940ee5bf5c3004c940768155338f0fd404049ecd5760219e7386726b97f2103ddd8009546aa3300d97cd6d49be227be78095ac72b05af8fe77490fd2091ce3f53aeffffffff0240420f00000000001976a914ea4349b431766be64c1c5015afd865e267d77a6988ac43b621000000000017a914cd271b873341f5364c9eb0217b5255be25f11cf98700000000'
    }

The commandline wallet outputs the transaction in human readable format and as a Python dictionary.
The transaction does not verify yet because it is only signed by 1 signature and it needs 2.

Now save the Python dictionary to a USB stick in text format and name it 'tx_dict.txt'.


Sign transaction with offline wallet
------------------------------------

Go to the offline device to sign the transaction with the second key. Use the following command to
import the freshly transaction dictionary.

.. code-block:: bash

    $ clw LitecoinMS -a <path-to-usb-stick>/tx_dict.txt
    Command Line Wallet for BitcoinLib

    Transaction
    Date: None
    Network: litecoin
    Status: new
    Verified: True
    Inputs
    - MFvNqhAWJY58yjLAME5V6ppivh9iVJJ6TH 3266639 9a9b4c9c9decefd50b7f40c3a243bbd514a18958cda70aa4fe9f82e0726e4d2f 0
      Script type: p2sh_multisig, signatures: 2 (2 of 3)
    Outputs
    - LgaczM5X63xd7QNnKrLjLK4rhrSQqfxuKv 1000000
    - 3LPmJ7DLR9v4ax6cSdPtgMB9jh7CDQ4Y64 2209347
    Fee: 57292
    Confirmations: None
    Pushed to network: False
    Wallet: LitecoinMS
    Signed transaction:
    {'fee': 57292,
     'inputs': [{'address': 'MFvNqhAWJY58yjLAME5V6ppivh9iVJJ6TH',
                 'output_n': 0,
                 'prev_hash': '9a9b4c9c9decefd50b7f40c3a243bbd514a18958cda70aa4fe9f82e0726e4d2f',
                 'signatures': [{'pub_key': '0364170e13312e6a2a867ce65e868a5539d53ed79017943f95059a2525fef5bb0f',
                                 'sig_der': '304502210091ddefdd9b18e036b0fe930a395914522f189c812c40fbbfbfe0d9936e645bfb022064c29a3fb85f0fac6ae0debeff410aca8c310c339def1ffa0e47b63a68b89f1a',
                                 'signature': '91ddefdd9b18e036b0fe930a395914522f189c812c40fbbfbfe0d9936e645bfb64c29a3fb85f0fac6ae0debeff410aca8c310c339def1ffa0e47b63a68b89f1a'},
                                {'pub_key': '038de68940ee5bf5c3004c940768155338f0fd404049ecd5760219e7386726b97f',
                                 'sig_der': '3045022100ed4f1c06fecc53df9b36dd54a79d5b8764f147fc5538f707df6c4a6afd3070390220419311e194d9e42984f8c4ec246f12e587b9f9e67caaf417ad51c7a23a6bf52e',
                                 'signature': 'ed4f1c06fecc53df9b36dd54a79d5b8764f147fc5538f707df6c4a6afd307039419311e194d9e42984f8c4ec246f12e587b9f9e67caaf417ad51c7a23a6bf52e'}],
                 'value': 3266639}],
     'network': 'litecoin',
     'outputs': [{'address': 'LgaczM5X63xd7QNnKrLjLK4rhrSQqfxuKv',
                  'value': 1000000},
                 {'address': '3LPmJ7DLR9v4ax6cSdPtgMB9jh7CDQ4Y64',
                  'value': 2209347}],
     'raw': '01000000012f4d6e72e0829ffea40aa7cd5889a114d5bb43a2c3407f0bd5efec9d9c4c9b9a00000000fdfe000048304502210091ddefdd9b18e036b0fe930a395914522f189c812c40fbbfbfe0d9936e645bfb022064c29a3fb85f0fac6ae0debeff410aca8c310c339def1ffa0e47b63a68b89f1a01483045022100ed4f1c06fecc53df9b36dd54a79d5b8764f147fc5538f707df6c4a6afd3070390220419311e194d9e42984f8c4ec246f12e587b9f9e67caaf417ad51c7a23a6bf52e014c6952210364170e13312e6a2a867ce65e868a5539d53ed79017943f95059a2525fef5bb0f21038de68940ee5bf5c3004c940768155338f0fd404049ecd5760219e7386726b97f2103ddd8009546aa3300d97cd6d49be227be78095ac72b05af8fe77490fd2091ce3f53aeffffffff0240420f00000000001976a914ea4349b431766be64c1c5015afd865e267d77a6988ac43b621000000000017a914cd271b873341f5364c9eb0217b5255be25f11cf98700000000'}

This will create a signed transaction and as you can see now it is verified and ready to send.

But before you continue please check if the transaction is the same as the original transaction. Besides
software or human mistakes it is a possibility someone hacks into your online PC and change the
transaction so it sends outputs to another address.


Send transaction
----------------

Copy the transaction dictionary (or just the 'raw' part) to the USB stick. You can send the transaction
with any online transaction broadcast service, but below we will explain how to send it with your
online wallet. This way your online wallet is updated as well.

To send the transaction import the transaction in your online wallet. You could import it without
the 'push' option first to double check the transaction.

To broadcast your transaction to the network import the raw transaction and push.

.. code-block:: bash

    $ clw LitecoinMS -p -i 01000000012f4d6e72e0829ffea40aa7cd5889a114d5bb43a2c3407f0bd5efec9d9c4c9b9a00000000fdfe000048304502210091ddefdd9b18e036b0fe930a395914522f189c812c40fbbfbfe0d9936e645bfb022064c29a3fb85f0fac6ae0debeff410aca8c310c339def1ffa0e47b63a68b89f1a01483045022100ed4f1c06fecc53df9b36dd54a79d5b8764f147fc5538f707df6c4a6afd3070390220419311e194d9e42984f8c4ec246f12e587b9f9e67caaf417ad51c7a23a6bf52e014c6952210364170e13312e6a2a867ce65e868a5539d53ed79017943f95059a2525fef5bb0f21038de68940ee5bf5c3004c940768155338f0fd404049ecd5760219e7386726b97f2103ddd8009546aa3300d97cd6d49be227be78095ac72b05af8fe77490fd2091ce3f53aeffffffff0240420f00000000001976a914ea4349b431766be64c1c5015afd865e267d77a6988ac43b621000000000017a914cd271b873341f5364c9eb0217b5255be25f11cf98700000000


..  == Restore wallet from backup
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