Bitcoinlib and Multiple Bitcoin Core Wallets
============================================

:date: 2024-05-17 15:47
:modified: 2024-05-17 17:34
:tags: bitcoin, bitcoin node, bitcoind, bitcoinlib, wallets
:category: BitcoinLib
:slug: bitcoinlib-and-multiple-bitcoin-core-wallets
:authors: Lennart Jongeneel
:summary: In this short guide we explain how to connect Bitcoinlib to multiple Bitcoin Core wallets. The private keys are stored and managed by Bitcoin Core and the wallet is managed with BitcoinLib, which makes it a powerful combinations.
:language: en

.. :slug: bitcoinlib-and-multiple-bitcoin-core-wallets:

In this guide we explain how to manage multiple Bitcoin Core wallets with Bitcoinlib. Bitcoin Core contains the wallets with the main private keys. And Bitcoinlib connect to those wallets and manages everything, creating some nice possibilities. The Bitcoin Core node is connected to other nodes and thus the Blockchain, so you are not dependant on third party service providers, which makes this a safe, reliable and fast setup.

.. image:: /images/bitcoinlib-manage-bitcoincore-wallets2.jpg
   :width: 1152px
   :alt: Multiple Bitcoin Wallet - text2img deepai generated
   :align: center


The Setup
---------

You need to use Bitcoinlib version 0.7 or higher for this setup to work, older versions do not support connections to multiple bitcoind wallets.

You need Bitcoin Core version 0.21 or higher. In version 0.21 descriptor wallets where introduced. Descriptor
wallets can easily export public master account keys, so you can generate new keys / addresses in Bitcoinlib.

* Bitcoinlib >= 0.7
* Bitcoin node >= 0.21


Create wallets in Bitcoin Core
------------------------------

First create two Bitcoin wallets on the device with a running and fully synced Bitcoin Core node:

.. code-block:: bash

    $ bitcoin-cli createwallet bclwallet1
    $ bitcoin-cli createwallet bclwallet2

The Bitcoin nodes now has two wallets, you can export descriptors with the listdescriptors command. This command
export a list of public master account keys in the descriptor format. Notice in the command below you have to add the
'-rpcwallet=bclwallet1' option so the node knows which wallet you use.

.. code-block:: bash

    bitcoin-cli -rpcwallet=bclwallet1 listdescriptors

In the list of descriptors you can find the wallet's public master account key for segregated witness keys,
you can recognise the key path looks like: [.../84h/1h/0h]. Where 84h is the code for segwit key paths.

.. code-block:: text

    wpkh([9af741ff/84h/1h/0h]tpubDDLXsfWUnPRrYLceKtRq38L6KhXFgN6zuJ46RDn5KgPs57QbMV8HRB9TTUNj1vVZXD4KaDnf5r1fBa2GeNwBzP1i6aPwLn1YfiZgCcvaPGW/0/*)#jf9hpecn

The tpub... is the public key you need to copy to Bitcoinlib to create and manage the wallet there. Repeat the steps
above for the second wallet.

Before we connect the wallet we need to correctly setup the connection to Bitcoind. To do this add the correct connection string in the .bitcoinlib/providers.json file.

.. code-block:: text

    "bitcoind.testnet": {
        "provider": "bitcoind",
        "network": "testnet",
        "client_class": "BitcoindClient",
        "provider_coin_id": "",
        "url": "http://local:...mypassword...@bitcoinnode:18332/wallet/{wallet_name}",
        "api_key": "",
        "priority": 10,
        "denominator": 100000000,
        "network_overrides": null
    },

Fill in your own username, password and servername. Leave the '{wallet_name}' string intact, this will be replaced
in Bitcoinlib's bitcoind service client.

To test the connection you can perform a simple blockcount request.

.. code-block:: python

    srv = Service(network='testnet', providers=['bitcoind'])
    print(srv.blockcount())


The last step is to create the wallets in Bitcoinlib. To do so copy the public master key into your Python code.
Also be sure to use the same wallet name in Python as in Bitcoin Core. If your provider.json file contains more then
the link to your Bitcoin node you need to specify the use of bitcoind, or else it will result in a lot of incorrect
requests to other service providers.

.. code-block:: python

    pubmaster1 = \
        'tpubDDLXsfWUnPRrYLceKtRq38L6KhXFgN6zuJ46RDn5KgPs57QbMV8HRB9TTUNj1vVZXD4KaDnf5r1fBa2GeNwBzP1i6aPwLn1YfiZgCcvaPGW'
    w = wallet_create_or_open('bclwallet1', witness_type='segwit', keys=pubmaster1)
    w.providers = ['bitcoind']
    w.scan(scan_gap_limit=1)
    w.info()

That is all there is to it. You can now easily update your wallet, create new keys and send / receive funds.
