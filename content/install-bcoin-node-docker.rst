Install Bcoin with Docker
=========================

:date: 2023-12-12 09:35
:modified: 2023-12-12 12:46
:tags: bcoin, bitcoin, docker, bitcoinlib
:category: Nodes
:slug: install-bcoin-node-docker
:authors: Lennart Jongeneel
:summary: How to install a Bcoin full node with Docker. Bcoin is an alternative Bitcoin node.
:language: en
:status: draft

.. :slug: install-bcoin-node-docker:

Bcoin is a full bitcoin node implementation used to parse the blockchain and verify blocks and transactions.
Besides the standard bitcoin node it has some extra features such as an index on address and transactions.

This makes it possible to query the node for transactions or UTXO's of a specific address. The library Bitcoinlib
can make use of the Bcoin node so it can run locally and doesn't need external blockchain services. The
`Blocksmurfer explorer <https://blocksmurfer.io>`_ uses a Bcoin node to query for blocks, transactions and
address data.


Install and build Bcoin
-----------------------

First install Docker if not already installed on your system.

.. code-block:: bash

    $ sudo apt install docker.io
    $ sudo systemctl start docker
    $ sudo systemctl enable docker

git clone https://github.com/1200wd/bcoin-docker.git

.. image:: /images/bcoin_logo.png
   :width: 451px
   :alt: Bcoin bitcoin node logo
   :align: right


Make sure you have at least 500GB disk space available for the blockchain database.

Update packages and install required repositories, Node.js and the Node.js package manager npm.

.. code-block:: bash

    $ sudo apt update
    $ sudo apt upgrade
    $ sudo apt install build-essential
    $ sudo apt install nodejs
    $ sudo apt install npm

Add a new user, specify a password and login as that user.

.. code-block:: bash

    $ sudo adduser bcoin
    $ sudo su - bcoin

Check the latest version of bcoin on https://github.com/bcoin-org/bcoin/tags and download the code.

.. code-block:: bash

    $ git clone --depth 1 --branch v2.1.2 https://github.com/bcoin-org/bcoin.git
    $ cd bcoin

Then rebuild the bcoin package. This can take a pretty long time.

.. code-block:: bash

    $ npm rebuild

Let's test it!

.. code-block:: bash

    $ ./bin/bcoin

It should now start downloading and parsing blocks. Press Ctrl-C to stop downloading so we can change some settings
first.


Bcoin Setup
-----------

[OPTIONAL] Setup SSL and create private key and certificate.

.. code-block:: bash

    $ cd secrets
    $ mkdir certs
    $ cd certs
    $ openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout privkey.pem -out cert.pem

[OPTIONAL] Setup firewall. Depends of course on the system and firewall you are using.

.. code-block:: bash

    $ sudo ufw allow 28332

Go to the newly create .bcoin directory in the home folder and create a bcoin.conf file.

.. code-block:: bash

    $ cd
    $ cd .bcoin
    $ nano bcoin.conf

Add the following contents to the bcoin.conf file. The main settings are put there as an example. Update to your
own needs and make sure to create your own secure API key. For more configuration settings see
https://github.com/bcoin-org/bcoin/blob/master/docs/configuration.md

.. code-block:: text

    # Bcoin.conf configuration example by Coineva
    #

    # HTTP host to listen on (default: 127.0.0.1). Use 0.0.0.0 to listen to all
    http-host: 0.0.0.0

    # HTTP port to listen on (default: 8332 for mainnet). Use another port if a bitcoind node is already running
    #http-port: 28332

    # Port to listen on (default: 8333)
    #port: 28333

    # Index transactions (enables transaction endpoints in REST api)
    index-tx: true

    # Index transactions and utxos by address
    index-address: true

    # Public host and port to advertise on network
    #public-host: 0.0.0.0
    #public-port: 8444

    # API key - Please enter your own secure (hexadecimal) key!
    api-key: replace-with-long-and-random-api-key

    # Use SSL
    ssl: true
    ssl-cert: @/ssl/cert.pem
    ssl-key: @/ssl/privkey.pem

Now test again and see if 'txindexer' and 'addrindexer' show up in the logs. Abort with Ctrl-C

.. code-block:: bash

    $ ~/bcoin/bin/bcoin


Create a service and download blockchain
----------------------------------------

Create a service to manage the bcoin process.

.. code-block:: bash

    $ logout
    $ sudo nano /lib/systemd/system/bcoin.service

.. code-block:: text


    [Unit]
    Description=Bcoin daemon
    After=network.target

    [Service]
    ExecStart=/home/bcoin/bcoin/bin/bcoin --daemon

    # Process management
    ####################

    Type=forking
    Restart=on-failure
    TimeoutStopSec=600

    # Directory creation and permissions
    ####################################

    User=bcoin
    Group=bcoin

    [Install]
    WantedBy=multi-user.target

Start service and check status.

.. code-block:: bash

    $ sudo systemctl start bcoin
    $ sudo systemctl status bcoin

Enable at startup.

.. code-block:: bash

    $ sudo systemctl enable bcoin

Some command to check the progress of your download and logs.

.. code-block:: bash

    $ sudo su - bcoin
    $ ./bcoin/bin/bcoin-cli info
    $ ./bcoin/bin/bcoin-cli --help
    $ tail -f .bcoin/debug.log

Your full Bcoin node is now up and running! Downloading and parsing the blockchain can hours or days, depending on
the system.

You can run some tests to see if everything is working.

.. code-block:: bash

    $ sudo su - bcoin
    $ cd bcoin/bin
    $ ./bcoin-cli block 0
    $ ./bcoin-cli tx 1HLoD9E4SDFFPDiYfNYnkBLQ85Y51J3Zb1
    $ ./bcoin-cli rpc getrawtransaction 9b0fc92260312ce44e74ef369f5c66bbb85848f2eddd5a7a1cde251e54ccfdd5

For a full list of commands run 'bcoin-cli help' or 'bcoin-cli rpc help'. All documentation of Bcoin can be found
at https://github.com/bcoin-org/bcoin/tree/master/docs