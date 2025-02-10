Install ElectrumX as Backend for Bitcoinlib
===========================================

:date: 2025-02-10 14:34
:modified: 2025-02-10 16:34
:tags: electrumx, electrum, bitcoin, bitcoin node, bitcoind, bitcoinlib
:category: BitcoinLib
:slug: install-electrumx-as-bitcoinlib-backend
:authors: Lennart Jongeneel
:summary: Install ElectrumX to use as backend Service provider for Bitcoinlib. Run your own ElectrumX server for stable, fast and private blockchain queries.
:language: en
:status: published

.. :slug: install-electrumx-as-bitcoinlib-backend:

.. image:: /images/electrumx-rpc-server.jpg
   :width: 640px
   :alt: ElectrumX as Bitcoinlib service provider
   :align: center


This article provides setup instructions for ElectrumX. ElectrumX is commonly used as backend service provider for the
Electrum wallet, but can also be used for Bitcoinlib.

ElectrumX is an active project and is writen in pure Python. It uses a full Bitcoin core node as backend and adds a
leveldb or rocksdb database with address, utxo, mempool and block information. It allow Bitcoinlib to make fast, local and private queries to update wallet, block and transaction information.

Bitcoinlib connects to ElectrumX with asynchronous RPC calls which make if fast and reliable. ElectrumX is normally
used as wallet backend so it cannot receive or parse blocks and might have trouble with large or non-standard transactions.

Source code for ElectrumX can be found on https://github.com/spesmilo/electrumx and documentation at https://electrumx-spesmilo.readthedocs.io/en/latest/


Install ElectrumX
-----------------

First install the required packages

.. code-block:: bash

    $ sudo apt install python3-virtualenv

Then create an new electrumx user and login

.. code-block:: bash

    $ adduser electrumx
    $ sudo su - electrumx

Clone the ElectrumX code from spesmilo, and create 2 new directories

.. code-block:: bash

    $ git clone https://github.com/spesmilo/electrumx.git
    $ mkdir service
    $ mkdir db

Now create a virtual environment, activate the environment and install the required packages

.. code-block:: bash

    $ mkdir .virtualenv
    $ virtualenv .virtualenv/electrumx
    $ source .virtualenv/electrumx/bin/activate
    $ python -m pip install electrumx

Now create a config file with the ElectrumX settings

.. code-block:: bash

    $ nano electrumx.conf

With the following content, update the daemon url to point to your bitcoind node. This includes some
specific settings for optimization for use with Bitcoinlib. The MAX_SEND increase the maximum response size
to be able to retrieve very large transactions.

.. code-block:: text

    DAEMON_URL=http://rpcuser:rpcpass@servername:8030
    COIN=Bitcoin
    DB_DIRECTORY=/home/electrumx/db
    ELECTRUMX=/home/electrumx/electrumx/electrumx_server
    NET=mainnet
    USERNAME=electrumx

    # Bitcoinlib specific settings
    CACHE_MB=1800
    MAX_SESSIONS = 500
    INITIAL_CONCURRENT = 50
    MAX_SEND = 5000000
    SERVICES=tcp://:50001


.. code-block:: bash

Now logout the electrumx user and create a Systemd service with the following content

.. code-block:: text

    [Unit]
    Description=Electrumx
    After=network.target

    [Service]
    EnvironmentFile=/home/electrumx/electrumx.conf
    ExecStart=/home/electrumx/.virtualenv/electrumx/bin/python3 /home/electrumx/electrumx/electrumx_server
    ExecStop=/home/electrumx/.virtualenv/electrumx/bin/python3 /home/electrumx/electrumx/electrumx_rpc -p 8000 stop
    User=electrumx
    LimitNOFILE=8192
    TimeoutStopSec=30min

    [Install]
    WantedBy=multi-user.target

.. code-block:: bash

    $ sudo nano /etc/systemd/system/electrumx.service
    $ sudo systemctl daemon-reload
    $ sudo systemctl start electrumx
    $ sudo systemctl status electrumx.service

Now you can check the logs and progress with journalctl and if everything works as expected you can enable the service

.. code-block:: bash

    $ journalctl -u electrumx -f
    $ systemctl enable electrumx

It can take up to a few days for ElectrumX to scan the blockchain files and build the index.

Also make sure to open up port 50001

.. code-block:: bash

    $ ufw allow 50001


Connect to Bitcoinlib
---------------------

ElectrumX is ready to query after the blockchain is fully scanned and indexed, which may take several days.

First make sure to install the aoirpcx package so bitcoinlib can connect to your ElectrumX server more reliable
and make queries much faster. The library works without aiorpcx but is about 20 times slower and can give timeout or
errors when making larger or consecutive queries.

When the server is running you can connect it to Bitcoinlib by adding the following json to ~/.bitcoinlib/providers.json. Make sure to replace localhost with you servername if applicable.

Please note: The url must just contain hostname:port, as a low level TCP protocol is used.

.. code-block:: json

  "electrumx": {
    "provider": "electrumx",
    "network": "bitcoin",
    "client_class": "ElectrumxClient",
    "provider_coin_id": "",
    "url": "localhost:50001",
    "api_key": "",
    "priority": 10,
    "denominator": 100000000,
    "network_overrides": null
  }

For a simple test call the blockcount method

.. code-block:: python

 >>> from bitcoinlib.services.services import Service
 >>> srv = Service(providers=['electrumx'])
 >>> srv.blockcount()
 888888

If you check in ~/.bitcoinlib/bitcoinlib.log you should see your own ElectrumX node is being queried and used as
Service provider.