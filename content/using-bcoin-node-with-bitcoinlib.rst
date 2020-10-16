Using Bcoin node with BitcoinLib
================================

:date: 2020-10-16 10:53
:modified: 2020-10-16 10:55
:tags: bcoin, bitcoin, node, bitcoinlib
:category: Nodes
:slug: using-bcoin-node-with-bitcoinlib
:authors: Lennart Jongeneel
:summary: How to use your Bcoin node in BitcoinLib as service provider
:language: en


.. :slug: using-bcoin-node-with-bitcoinlib:

With Python `BitcoinLib <https://coineva.com/category/bitcoinlib.html>`_ you can manage wallets and create
and receive transactions. BitcoinLib depends on external service providers such as blockchair.com or
blocksmurfer.io to communicate with the Blockchain. But too be more efficient and increase privacy you can
also setup your local Bcoin node and use this in BitcoinLib.

Bcoin is a full bitcoin node implementation used to parse the blockchain and verify blocks and transactions.
In my previous article you can read how to `install a Bcoin node <https://coineva.com/install-bcoin-node-ubuntu.html>`_.


Setup BitcoinLib to use Bcoin node
----------------------------------

First login to your server with the running Bcoin node and check if everything is running as it should.

.. code-block:: bash

    $ sudo su - bcoin
    $ cd bcoin/bin
    $ ./bcoin-cli block 101010

This should return block 101010 as dictionary.

Checkout the Bcoin config file in .bcoin/bcoin.conf and look for the API key. The API key should be a long
random list of characters. You could use a bitcoin private key for this.

.. code-block:: python-cli

    >>> from bitcoinlib.keys import Key
    >>> Key().private_hex
    '13729c7f87c56628eb8070214f3bdc62f6904c70c71c465bfffee36e6aa09b39'

Now go to the Bitcoinlib directory and edit the .bitcoinlib/providers.json file to add an extra service provider.
Add the following json to the provider.json file, make sure to use the correct API key and fill in your server address.

.. code-block:: json

    "bcoin": {
        "provider": "bcoin",
        "network": "bitcoin",
        "client_class": "BcoinClient",
        "provider_coin_id": "",
        "url": "https://x:13729c7f87c56628eb8070214f3bdc62f6904c70c71c465bfffee36e6aa09b39@<your_server_ip>:28332/",
        "api_key": "",
        "priority": 20,
        "denominator": 100000000,
        "network_overrides": null
    },

The priority is set to 20, which is higher then the default priority of 10. This means the Bcoin provider is tried first
and if this fails another provider will be used.

Let's test if the Bcoin provider is used by Bitcoinlib.

.. code-block:: python-cli

    >>> from bitcoinlib.services.services import Service
    >>> srv = Service(providers=['bcoin'])
    >>> srv.getblock(101010)
    <Block(000000000001af33247fff33aae7c31baee4148d5a189e7353bf13bcee618202, 101010, transactions: 4)>

It's works! Bitcoinlib will now use your local Bcoin node whenever possible to retrieve and send information
to the blockchain.

If you still encounter problems please check:

- Is port 28332 open on your server and local machine? Does it need to be forwarded?
- Is SSL correctly setup on the Bcoin server machine, see `install Bcoin node <https://coineva.com/install-bcoin-node-ubuntu.html>`_.
- Check the logs in .bitcoinlib/bitcoinlib.log and on the server in .bcoin/debug.log
- Check the documentation on `Github Bcoin Docs <https://github.com/bcoin-org/bcoin/blob/master/docs/README.md>`_ or `BitcoinLib ReadTheDocs <https://bitcoinlib.readthedocs.io/en/latest/>`_


.. image:: /images/bcoin_logo.png
   :width: 451px
   :alt: Bcoin bitcoin node logo
   :align: right

