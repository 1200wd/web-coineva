Crypto Administration 2 - Recreate old wallets
==============================================

:date: 2020-05-11 09:20
:modified: 2020-05-11 09:20
:tags: tax, administration, cryptocurrency, recreate, wallets, bitcoinlib, bitcoin, cryptalyse
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

.. image:: /images/Aleutianwallet.gif
   :width: 824px
   :alt: Ancient wallet - source Wikipedia
   :align: center


Cryptalyse
----------

Install Cryptalyse to allow to analyse, reconstruct and export wallets with Bitcoinlib more easily.

.. code-block:: bash

    $ git clone https://github.com/1200wd/cryptalyse.git

Cryptalyse contains a class CryptalyseWallet based on the HDWallet class from Bitcoinlib with some extra helper methods.
This class adds a clusters() and inputs_correlated() method which looks for correlated inputs. For instance if
a transaction contains 2 or more inputs, you can assume those inputs are created by the same person and the used
addresses belong to the same wallet.

You can check out the source code at `<https://github.com/1200wd/cryptalyse>`_.



Recreate Wallet
~~~~~~~~~~~~~~~

Assume you want to recover transactions in an old wallet of which you only know 2 addresses. First create a wallet
with the first address.

.. code-block:: python

    >>> from cryptalyse.cryptalyse import CryptalyseWallet
    >>> w = CryptalyseWallet.create('reconstructed', 'tb1qe7h6l8sg7nf8z0rz6a4kfgavatjjac5qardt5z')

If you now update the wallet you can see it found 2 transactions with this address.

.. code-block:: python

    >>> w.scan()
    >>> w.info()
    === WALLET ===
     ID                             2
     Name                           reconstructed
     Owner
     Scheme                         single
     Multisig                       False
     Witness type                   segwit
     Main network                   testnet
     Latest update                  2020-05-11 10:59:30.056860

    = Wallet Master Key =
     ID                             11
     Private                        False
     Depth                          0

    - NETWORK: testnet -
    - - Keys

    - - Transactions Account 0 (2)
    356d8aa5dbf816e499cae8329811d9baa7aa46d1dfd68d33d7819c78f64206ff tb1qe7h6l8sg7nf8z0rz6a4kfgavatjjac5qardt5z   110982          9000
    ab4f559c4d1ed91f20089b124009597f281f54bbcaa8ae96d1779f97856722f6 tb1qe7h6l8sg7nf8z0rz6a4kfgavatjjac5qardt5z   110972         -9000

    = Balance Totals (includes unconfirmed) =


When you use the extra methods from Cryptalyse you can see 1 correlated address is found, and the wallet consists of
1 cluster with 2 addresses.

.. code-block:: python

    >>> w.inputs_correlated
    ['tb1qvlnztnn6eqr02c7gte2gmnda3x7js5jcws2gh4']
    >>> w.clusters()
    [{'tb1qvlnztnn6eqr02c7gte2gmnda3x7js5jcws2gh4', 'tb1qe7h6l8sg7nf8z0rz6a4kfgavatjjac5qardt5z'}]


If you look at the second transaction, you can see why the addresses are correlated. They are both used as input in the
same transaction.

.. code-block:: python

    >>> w.transactions()[1].info()
    Transaction ab4f559c4d1ed91f20089b124009597f281f54bbcaa8ae96d1779f97856722f6
    Date: 2019-12-16 19:44:50
    Network: testnet
    Version: 1
    Witness type: segwit
    Status: confirmed
    Verified: False
    Inputs
    - tb1qe7h6l8sg7nf8z0rz6a4kfgavatjjac5qardt5z 9000 356d8aa5dbf816e499cae8329811d9baa7aa46d1dfd68d33d7819c78f64206ff 1
      segwit sig_pubkey; sigs: 0 (1-of-0) not validated
    - tb1qvlnztnn6eqr02c7gte2gmnda3x7js5jcws2gh4 8000 b11291114358ba84e4e9e644ef5e1e92d240f7c04c55a0fe34050a97d7336d41 0
      segwit sig_pubkey; sigs: 0 (1-of-0) not validated
    Outputs
    - 2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE 9000 p2sh S
    - tb1qq0k9jh4npm5y7dgy5uj759ysgq6uzv7sp857np 6346 p2wpkh S
    Size: 372
    Vsize: 372
    Fee: 1654
    Confirmations: 110972
    Pushed to network: False
    Wallet: reconstructed


Import addresses
~~~~~~~~~~~~~~~~

We can now import the correlated address we found and add the other address we know to the wallet.

.. code-block:: python

    >>> from bitcoinlib.keys import Address
    >>> key = Address.import_address('tb1qvlnztnn6eqr02c7gte2gmnda3x7js5jcws2gh4')
    >>> w.import_key(key)
    <HDWalletKey(key_id=12, name=import_key_00001, wif=None, path=import_key_00001)>
    >>> key = Address.import_address('tb1q35cc0y9tfp0mswskpkka7cxqpap4st4wpzkewv')
    >>> w.import_key(key)
    <HDWalletKey(key_id=13, name=import_key_00002, wif=None, path=import_key_00002)>
    >>> w.scan()
    >>> w.info()
    === WALLET ===
     ID                             2
     Name                           reconstructed
     Owner
     Scheme                         single
     Multisig                       False
     Witness type                   segwit
     Main network                   testnet
     Latest update                  2020-05-11 11:23:20.486931

    = Wallet Master Key =
     ID                             11
     Private                        False
     Depth                          0

    - NETWORK: testnet -
    - - Keys

    - - Transactions Account 0 (6)
    356d8aa5dbf816e499cae8329811d9baa7aa46d1dfd68d33d7819c78f64206ff tb1qe7h6l8sg7nf8z0rz6a4kfgavatjjac5qardt5z   110983          9000
    82a3ee8315bad3e188a49b95e62442acf315615a1da7d4e6eaef05f259145897 tb1q35cc0y9tfp0mswskpkka7cxqpap4st4wpzkewv   110983          5000
    b11291114358ba84e4e9e644ef5e1e92d240f7c04c55a0fe34050a97d7336d41 tb1qvlnztnn6eqr02c7gte2gmnda3x7js5jcws2gh4   110982          8000
    ab4f559c4d1ed91f20089b124009597f281f54bbcaa8ae96d1779f97856722f6 tb1qe7h6l8sg7nf8z0rz6a4kfgavatjjac5qardt5z   110973         -9000
    ab4f559c4d1ed91f20089b124009597f281f54bbcaa8ae96d1779f97856722f6 tb1qvlnztnn6eqr02c7gte2gmnda3x7js5jcws2gh4   110973         -8000
    dc4a01d552631920475940135459592629c72c0f3b8fa2a77e025ed6fbb6317c tb1q35cc0y9tfp0mswskpkka7cxqpap4st4wpzkewv   110972         -5000

    = Balance Totals (includes unconfirmed) =

Some new transactions are found. And if we look the correlated addresses and clusters, we see 2 clusters of addresses
and a new correlated address. Which we can also add to the wallet.

.. code-block:: python

    >>> w.inputs_correlated
    ['tb1qq0k9jh4npm5y7dgy5uj759ysgq6uzv7sp857np']
    >>> w.clusters()
    [{'tb1qvlnztnn6eqr02c7gte2gmnda3x7js5jcws2gh4', 'tb1qe7h6l8sg7nf8z0rz6a4kfgavatjjac5qardt5z'}, {'tb1qq0k9jh4npm5y7dgy5uj759ysgq6uzv7sp857np', 'tb1q35cc0y9tfp0mswskpkka7cxqpap4st4wpzkewv'}]
    >>> key = Address.import_address('tb1qq0k9jh4npm5y7dgy5uj759ysgq6uzv7sp857np')
    >>> w.import_key(key)
    <HDWalletKey(key_id=14, name=import_key_00003, wif=None, path=import_key_00003)>


After a rescan, we see no correlated inputs are found. So we now we have reconstructed the wallet.

.. code-block:: python

    >>> w.scan()
    >>> w.inputs_correlated
    []
    >>> w.info()
    === WALLET ===
     ID                             2
     Name                           reconstructed
     Owner
     Scheme                         single
     Multisig                       False
     Witness type                   segwit
     Main network                   testnet
     Latest update                  2020-05-11 11:39:37.420613

    = Wallet Master Key =
     ID                             11
     Private                        False
     Depth                          0

    - NETWORK: testnet -
    - - Keys

    - - Transactions Account 0 (8)
    356d8aa5dbf816e499cae8329811d9baa7aa46d1dfd68d33d7819c78f64206ff tb1qe7h6l8sg7nf8z0rz6a4kfgavatjjac5qardt5z   110985          9000
    82a3ee8315bad3e188a49b95e62442acf315615a1da7d4e6eaef05f259145897 tb1q35cc0y9tfp0mswskpkka7cxqpap4st4wpzkewv   110984          5000
    b11291114358ba84e4e9e644ef5e1e92d240f7c04c55a0fe34050a97d7336d41 tb1qvlnztnn6eqr02c7gte2gmnda3x7js5jcws2gh4   110983          8000
    ab4f559c4d1ed91f20089b124009597f281f54bbcaa8ae96d1779f97856722f6 tb1qe7h6l8sg7nf8z0rz6a4kfgavatjjac5qardt5z   110975         -9000
    ab4f559c4d1ed91f20089b124009597f281f54bbcaa8ae96d1779f97856722f6 tb1qvlnztnn6eqr02c7gte2gmnda3x7js5jcws2gh4   110975         -8000
    ab4f559c4d1ed91f20089b124009597f281f54bbcaa8ae96d1779f97856722f6 tb1qq0k9jh4npm5y7dgy5uj759ysgq6uzv7sp857np   110975          6346
    dc4a01d552631920475940135459592629c72c0f3b8fa2a77e025ed6fbb6317c tb1q35cc0y9tfp0mswskpkka7cxqpap4st4wpzkewv   110974         -5000
    dc4a01d552631920475940135459592629c72c0f3b8fa2a77e025ed6fbb6317c tb1qq0k9jh4npm5y7dgy5uj759ysgq6uzv7sp857np   110974         -6346

    = Balance Totals (includes unconfirmed) =


The code this example is based on can be found on
`Github <https://github.com/1200wd/cryptalyse/blob/master/example_wallet_reconstruction.py>`_.
