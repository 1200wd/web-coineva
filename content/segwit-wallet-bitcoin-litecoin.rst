Create a Bitcoin and Litecoin Segwit Wallet
===========================================

:date: 2018-12-05 12:04
:modified: 2018-12-05 13:18
:tags: segwit, wallets, bitcoinlib, bitcoin, litecoin, manual
:category: BitcoinLib
:slug: create-litecoin-bitcoin-segwit-wallet
:authors: Lennart Jongeneel
:summary: Create a Bitcoin and Litecoin Segregated Witness Wallet with a single private key
:language: en


.. :slug: create-litecoin-bitcoin-segwit-wallet:

Storing private keys in a safe way can be cumbersome, so if you work with multiple cryptocurrencies, it
is handy to use a single private key for multiple networks for example Bitcoin and Litecoin.

This article describes how to create a Segwit wallet with Python BitcoinLib from the Python console.
It assumes you have the installed the `Python BitcoinLib <{filename}/python-bitcoin-library.rst>`_ with
'pip install bitcoinlib'.

.. image:: /images/bitcoin-litecoin-segwit.jpg
   :width: 640px
   :alt: Bitcoin and Litecoin SegWit Wallet, credits @Frankieboy93
   :align: right

Thanks to Peter Dalby for the image, https://twitter.com/Frankieboy93


Create the private key
----------------------

.. code-block:: python-cli

    >>> from bitcoinlib.mnemonic import Mnemonic
    >>> key = Mnemonic().generate()
    >>> key
    'scheme unfold sea follow canvas food average knife stamp random collect slot'

Make sure to write down this private key passphrase on 2 or more pieces of paper and store them in a safe place.


Create the wallet
-----------------

Now create a Bitcoin segwit wallet and add an account for the Litecoin network:

.. code-block:: python-cli

    >>> from bitcoinlib.wallets import HDWallet
    >>> w = HDWallet.create('mywallet', key, witness_type='segwit', network='bitcoin')
    >>> w.new_account(network='litecoin')
    >>> w.info()
    === WALLET ===
     ID                             13
     Name                           mywallet
     Owner
     Scheme                         bip32
     Multisig                       False
     Witness type                   segwit
     Main network                   bitcoin

    = Wallet Master Key =
     ID                             116
     Private                        True
     Depth                          0

    - NETWORK: bitcoin -
    - - Keys
      121 m/84'/0'/0'/0/0              bc1qjalwm3tr6jz5fecprutheejj84axlvsunj267k    address index 0                      0.00000000 BTC
      129 m/84'/0'/0'/1/0              bc1qyuwzqgn0czf40k2vdf9qsz3wlsfsmcfw59ag07    address index 0                      0.00000000 BTC

    - - Transactions (Account 0, zpub6qrL6kaP9pEhD9RXiJrbVC9JmMd2XwXJh6nxH4rNk6Q1qHC7fgEEarNLKAFseRxXY8cZLymniczWvyqJp8CZGnmDSX6US1tit2BxHroAPCR)

    - NETWORK: litecoin -
    - - Keys
      125 m/84'/2'/0'/0/0              ltc1qpeez5d09uq7ruead6lh5m7aq09r47muvutgsgd   address index 0                      0.00000000 LTC
      127 m/84'/2'/0'/1/0              ltc1qzwus8mmd8y302aw20wg84whhszj6h0ay75vyhm   address index 0                      0.00000000 LTC

    - - Transactions (Account 0, Mtub2sXpSFfX3mYCLHrNtJFNfaMcTU5M7UdbasVAQDUVBwrvqEwFTeAcJVkCtgrv9MViXistThqQNPt77sUSvpj4dTwsRD4tFa5jwDcujaHQacL)

    = Balance Totals (includes unconfirmed) =

A wallet with the first derived addresses has been created. This wallet will be stored in a Sqlite database in your
home folder. You can reopen it later with:

.. code-block:: python-cli

    >>> w = HDWallet('mywallet')


Create a Transaction
--------------------

First fund your wallet with a small amount of litecoins or bitcoins so we can create a transaction.

Update your wallet:

.. code-block:: python-cli

    >>> w.utxos_update()
    1

The utxos_update method outputs how many new unspent outputs or new funds are added, so '1' means a new UTXO is found.

To create an transaction type:

.. code-block:: python-cli

    >>> t = w.send_to('ltc1qzwus8mmd8y302aw20wg84whhszj6h0ay75vyhm', 94118, fee=1000, offline=True)
    >>> t.info()
    Transaction
    Date: None
    Network: litecoin
    Version: 1
    Witness type: segwit
    Status: new
    Verified: True
    Inputs
    - ltc1qpeez5d09uq7ruead6lh5m7aq09r47muvutgsgd 95118 4b2698a851b2a38ebef43c2af7da4726058b3a88e6dda4cace43d2e944d99227 0
      Script type: sig_pubkey (segwit), signatures: 1 (1-of-1), valid
    Outputs, s
    - ltc1qzwus8mmd8y302aw20wg84whhszj6h0ay75vyhm 94118
    Size: 141
    Vsize: 141
    Fee: 1000
    Confirmations: None
    Pushed to network: False
    Wallet: mywallet

If everything looks fine you can push the transaction:

.. code-block:: python-cli

    >>> t.send()
    True
    >>> t.info()
    Transaction b68ea01a4521048bece5f208932d36add3f85981f13bb446bf05a065f0c43405
    Date: None
    Network: litecoin
    Version: 1
    Witness type: segwit
    Status: unconfirmed
    Verified: True
    Inputs
    - ltc1qpeez5d09uq7ruead6lh5m7aq09r47muvutgsgd 95118 4b2698a851b2a38ebef43c2af7da4726058b3a88e6dda4cace43d2e944d99227 0
      Script type: sig_pubkey (segwit), signatures: 1 (1-of-1), valid
    Outputs
    - ltc1qzwus8mmd8y302aw20wg84whhszj6h0ay75vyhm 94118
    Size: 191
    Vsize: 141
    Fee: 1000
    Confirmations: 0
    Pushed to network: True
    Wallet: mywallet


After sending the transaction object is updated with the transaction ID, and send results. The status should show as
'unconfirmed' and pushed to network should be True. If any errors occur when sending they will also be added to the
object.

This is it. You can reopen your wallet later as all information is stored in the database. And you can restore or
recreate your wallet with the passphrase.

Please note that this wallet is not super-secure as private keys are stored unencrypted on your device, so you should
only use it for testing or small amounts of pocket money. To add extra security you can
`create a multisig wallet <{filename}/create-litecoin-multisig-wallet.rst>`_
and/or encrypt your wallet private keys with a extra password.
