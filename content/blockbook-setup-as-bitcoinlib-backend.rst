Setup Blockbook as Backend for Bitcoinlib
=========================================

:date: 2024-10-15 09:12
:modified: 2025-02-10 16:48
:tags: blockbook, trezor, bitcoin, bitcoin node, bitcoind, bitcoinlib
:category: BitcoinLib
:slug: blockbook-setup-as-bitcoinlib-backend
:authors: Lennart Jongeneel
:summary: How to setup Trezor's Blockbook to use as backend Service provider for Bitcoinlib. Run your own Blockbook Service provider for stable, fast and private blockchain queries.
:language: en
:status: published

.. :slug: blockbook-setup-as-bitcoinlib-backend:

.. image:: /images/blockbook-bitcoin-backend.jpeg
   :width: 640px
   :alt: Blockbook as Bitcoinlib service provider
   :align: center


This article provides installation instructions Trezor's Blockbook and setup guidelines on how to use Blockbook as
provider for Bitcoinlib.

Blockbook is a well maintained advanced backend for Trezor wallet and it used to parse and query the Bitcoin blockchain.
It can also be used to serve Bitconlib wallets and other Bitcoinlib applications. Blockbook is fast, reliable and
can be used privately. Besides Bitcoin, other networks such as Litecoin, Dogecoin and Dash are supported.


Install Blockbook
-----------------

Blockbook used a full Bitcoin core node and adds another layer to be able to query the Blockchain for address
transactions and balances. So you will need a powerful server with steady internet connection and a least 2 TB of
diskspace and 32GB memory (RAM). And then wait at least 2 days before everything is synchronised and parsed.

For this guide I used Ubuntu 22.04 LTS server. When trying to install the latest version Ubuntu 24.04.01
as of november 2024 I was running into multiple errors, but when you read this that could be solved already.

Before installing Blockbook (and bitcoinlib) you need to make sure the Python development packages are installed.

.. code-block:: bash

 $ apt install build-essential python3-dev python3-pip

Now install Docker using the instructions below. Detailed instructions for your OS can be found on
https://docs.docker.com/engine/install/. This are the instructions for Ubuntu:

.. code-block:: bash

 # Add Docker's official GPG key:
 $ sudo apt-get update
 $ sudo apt-get install ca-certificates curl
 $ sudo install -m 0755 -d /etc/apt/keyrings
 $ sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
 $ sudo chmod a+r /etc/apt/keyrings/docker.asc

 # Add the repository to Apt sources:
 $echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
 $ sudo apt-get update
 $ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

Now clone and build Blockbook

.. code-block:: bash

 $ git clone https://github.com/trezor/blockbook
 $ cd blockbook
 $ make all-bitcoin

When the building is done install the Bitcoin core backend and start it

.. code-block:: bash

 $ cd build
 $ sudo apt install ./<package name> (e.g., apt install ./backend-bitcoin_0.16.1-satoshilabs1_amd64.deb)
 $ sudo systemctl start backend-bitcoin.service

To check the status run

.. code-block:: bash

  $ sudo tail -f /opt/coins/data/bitcoin/backend/debug.log

It is now downlooading the Bitcoin blockchain, which could to 24 hours or more. If the blockchain is finished
you can continue installing the Blockbook package.

.. code-block:: bash

 $ apt install ./<blockbook package> (e.g., apt install ./blockbook-bitcoin_0.0.6_amd64.deb)

If you run the Blockbook server on your local network, you can remove the -certfile option from the systemctl deamon.
Also you could add the workers option to avoid memory problems, see next paragraph.

.. code-block:: bash

 $ sudo nano /lib/systemd/system/blockbook-bitcoin.service
 $ sudo systemctl daemon-reload
 $ systemctl start blockbook-bitcoin.service

Make sure to open port 9130 if you are using a firewall. Blockbook start synchronising with the blockchain and
this can take several days. To view the progress you can check your browser at https://<servername>:9130 or check the logs
at:

.. code-block:: bash

  $ sudo tail -f /opt/coins/blockbook/bitcoin/logs/blockbook.INFO

This installation instructions are based on https://trezor.io/learn/a/custom-backend-in-trezor-suite, you can find more
details there if you run into problems.


Problems during Blockbook sync
------------------------------

Unfortunately after 2 days of synchronising I experienced some database errors

.. code-block:: go

  1075 blockbook.go:184] internalState: database is in inconsistent state and cannot be used

The process probably got interrupted because there was not enough free memory. The server has 32 GB RAM, but other
software is using RAM as well. The only solution is to delete the database and start over again.

The problem was solved by added the workers=1 parameter to reduce memory usage. More info can be found here:
https://github.com/trezor/blockbook/issues/89

.. code-block:: bash

    $ sudo nano /lib/systemd/system/blockbook-bitcoin.service
    # Add the -workers=1 to the ExecStart line
    $ sudo systemctl daemon-reload
    $ sudo systemctl start blockbook-bitcoin.service


Connect to Bitcoinlib
---------------------

Install Bitcoinlib using instruction from https://bitcoinlib.readthedocs.io/en/latest/source/_static/manuals.install.html
The Blockbook api only works if it is fully synchronised, you can check the status.

When the api is running you can easily connect it to Bitcoinlib, add the following json to ~/.bitcoinlib/providers.json.
Make sure to replace <server> with you servername. Priority is set to 20 so this provider will be used first.

.. code-block:: json

  "blockbook": {
    "provider": "blockbook",
    "network": "bitcoin",
    "client_class": "BlockbookClient",
    "provider_coin_id": "",
    "url": "http://<servername>:9130/api/v2/",
    "api_key": "",
    "priority": 20,
    "denominator": 100000000,
    "network_overrides": null
  }

For a simple test do

.. code-block:: python

 >>> from bitcoinlib.services.services import Service
 >>> srv = Service(providers=['blockbook'])
 >>> srv.blockcount()
 869969

If you check in ~/.bitcoinlib/bitcoinlib.log you should see your own Blockbook node is being queried and used as
Service provider.