Create a Bitcoin multisig wallet from Python commandline
========================================================

:date: 2019-02-12 11:22
:modified: 2019-02-12 11:22
:tags: multisig, wallets, bitcoinlib, bitcoin, manual
:category: BitcoinLib
:slug: create-multisig-wallet-bitcoin-python
:authors: Lennart Jongeneel
:summary: Create a 2-of-2 Bitcoin multi-signature wallet from the Python commandline
:language: en


.. :slug: create-multisig-wallet-bitcoin-python:

Follow the steps below to create a 2-of-2 multi-signature wallet from the Python commandline with a few simple steps.
It assumes you have the installed the `Python BitcoinLib <{filename}/python-bitcoin-library.rst>`_ with
'pip install bitcoinlib'.


Create some private keys
------------------------

Create the first key using the Mnemonic phrase generator from BitcoinLib

.. code-block:: python-cli

    >>> from bitcoinlib.mnemonic import Mnemonic
    >>> p1 = Mnemonic().generate()
    >>> p1
    'ethics near crew genuine enter panda garment siren tumble slush nation dash'

Make sure to write down this private key passphrase on 2 or more pieces of paper and store them in a safe place.

Now preferably on another (offline) device generate a second key.

.. code-block:: python-cli

    >>> from bitcoinlib.mnemonic import Mnemonic
    >>> p2 = Mnemonic().generate()
    >>> p2
    'poem swamp inside oyster cube sign prefer scatter field health victory false'

Backup this key carefully again. We can now create a public masterkey to share with our main PC.

.. code-block:: python-cli

    >>> from bitcoinlib.keys import HDKey
    >>> key2 = HDKey.from_passphrase(p2, key_type='single')
    >>> key2.wif()
    'xpub661MyMwAqRbcFpdnKAgSoGkJoFfk6LAC7Ncewo9hUxPcQA7yCjY7k6QoMBPxYAv4RsJj3GiuDHVBeMGxABJJb5JsvxEMFwy3ekamoJLXHCc'
    Share this key using a USB stick or use a library such as qrcode to create a printable and scanable code.

.. code-block:: python-cli

    >>> import pyqrcode
    >>> qrcode = pyqrcode.create(key2.wif())
    >>> print(qrcode.terminal())


Create the multisig wallet
--------------------------

We are now ready to create the wallet with the private key from above and the public master key from the other PC.
The first address / key is created with the new_key() method.

.. code-block:: python-cli

    >>> from bitcoinlib.wallets import HDWallet
    >>> wif2 = 'xpub661MyMwAqRbcFpdnKAgSoGkJoFfk6LAC7Ncewo9hUxPcQA7yCjY7k6QoMBPxYAv4RsJj3GiuDHVBeMGxABJJb5JsvxEMFwy3ekamoJLXHCc'
    >>> key2 = HDKey(wif2, key_type='single')
    >>> w = HDWallet.create('bitcoin-multisig-wallet', [p1, key2])
    >>> >>> w.new_key()
    <HDWalletKey(key_id=764, name=Multisig Key 763/755, wif=multisig-37dtoR6QrsiEZEsnarByktVRNreSC61gDf, path=m/45'/0/0/0)>
    >>> w.info()
    === WALLET ===
     ID                             126
     Name                           bitcoin-multisig-wallet
     Owner
     Scheme                         bip32
     Multisig                       True
     Multisig Wallet IDs            127, 128
     Witness type                   legacy
     Main network                   bitcoin

    = Multisig Public Account Keys =
      751 xpub682fymfahPiaB1nHt9JLKfBrkXdJS92LFEwjVkPMJoesjXZSG79DvmtguYDexeCvRrhETF6mcFQScZj47PBX6yR6zY8wQU1qDqEzgQEUNE1 main
      756 xpub68A4hatRFDPrgWatXRoSc72bBVVnV6EiBUSsGa4uwh1ZuZNZ9BhPktWKuzY9jX2xXtoXbyu3JC9cJraQE1FM2cS3jEdVZj7LoUNGqUGPg1v main
    For main keys a private master key is available in this wallet to sign transactions.

    - NETWORK: bitcoin -
    - - Keys
      764 m/45'/0/0/0                  37dtoR6QrsiEZEsnarByktVRNreSC61gDf            Multisig Key 763/755                 0.00000000 BTC

    = Balance Totals (includes unconfirmed) =

The info() method show the 2 public master keys of this wallet. At the end of the line you find 'main' when a private key is available.

Your wallet will be stored in a Sqlite database in your home folder. You can reopen it later using the name or wallet ID.

.. code-block:: python-cli

    >>> w = HDWallet('bitcoin-multisig-wallet')
    >>> w = HDWallet(126)


Create a Transaction
--------------------

Now fund your wallet with a small amount of bitcoins so we can create a transaction.

Update your wallet:

.. code-block:: python-cli

    >>> w.utxos_update()
    1

The utxos_update method returns the number of new UTXO's found, so '1' means funds received! If you call the w.info()
method again you can find the details of the UTXO's and total balance available in this wallet.

Imagine you want to donate all the funds in your wallet to the
`Internet Archive
<https://archive.org/donate/>`_
Then you can use the wallets sweep() method to spent all UTXO's.

.. code-block:: python-cli

    >>> t = w.sweep('1Archive1n2C579dMsAu3iC6tWzuQJz8dN')
    >>> t.info()
    Transaction 1e4e979c9622d64c51cbba0b17386e3b5a7ddfb9aad4a4ec3a935a01bff87666
    Date: None
    Network: bitcoin
    Version: 1
    Witness type: legacy
    Status: new
    Verified: False
    Inputs
    - 37dtoR6QrsiEZEsnarByktVRNreSC61gDf 388813 9b3ff0e4ebf336036a30cdf1d5ed6e45ef39d661315faed069efa3371770297b 1
      legacy p2sh_multisig; sigs: 1 (2-of-2) not validated
    Outputs
    - 1Archive1n2C579dMsAu3iC6tWzuQJz8dN 387813 p2pkh
    Size: 337
    Vsize: 337
    Fee: 1000
    Confirmations: None
    Pushed to network: False
    Wallet: bitcoin-multisig-wallet
    Errors: Cannot verify transaction


This will create a transaction and as you can see it could not be verified. The first input needs 2 signatures but
the wallet contains only 1 private key. So we need to copy the transaction to the other PC to sign it.

.. code-block:: python-cli

    >>> t.raw_hex()
    '010000000...etc...5d88ac00000000'


Now on the other PC import this raw transaction and sign.

    >>> t = Transaction.import_raw('010000000...etc...5d88ac00000000')
    >>> t.sign(key2)
    >>> t.verify()
    >>> t.info()
    Transaction 47f4a511aef839fa9fea9d900b1eba2866ab397fee558e8aaec3c90586072768
    Date: None
    Network: bitcoin
    Version: 1
    Witness type: legacy
    Status: new
    Verified: True
    Inputs
    - 37dtoR6QrsiEZEsnarByktVRNreSC61gDf 388813 9b3ff0e4ebf336036a30cdf1d5ed6e45ef39d661315faed069efa3371770297b 1
      legacy p2sh_multisig; sigs: 2 (2-of-2) valid
    Outputs
    - 1Archive1n2C579dMsAu3iC6tWzuQJz8dN 387813 p2pkh
    Size: 230
    Vsize: 230
    Fee: None
    Confirmations: None

The transaction input now has 2 signatures and is ready to send. You could copy-n-paste the raw transaction and send
it with a service such as https://live.blockcypher.com/btc/pushtx/ or -when the PC is online- you can send it
with BitcoinLib.

    >>> from bitcoinlib.service import Service
    >>> Service().sendrawtransaction(t.raw())

Which will return a transaction ID when sending was successful.
