Bitcoinlib and Multiple Bitcoin Core Wallets
============================================

:date: 2024-10-12 08:56
:modified: 2024-10-12 09:34
:tags: blockbook, trezor, bitcoin, bitcoin node, bitcoind, bitcoinlib
:category: BitcoinLib
:slug: blockbook-setup-as-bitcoinlib-backend
:authors: Lennart Jongeneel
:summary: How to setup Trezor's Blockbook to use as backend Service provider for Bitcoinlib. Run your own Blockbook Service provider for stable, fast and private blockchain queries.
:language: en
:status: draft

.. :slug: blockbook-setup-as-bitcoinlib-backend:

.. image:: /images//home/lennart/Downloads/blockbook-bitcoin-backend.jpeg
   :width: 640px
   :alt: Blockbook as Bitcoinlib service provider
   :align: center

In this guide we explain how to manage multiple Bitcoin Core wallets with Bitcoinlib. Bitcoin Core contains the wallets with the main private keys. And Bitcoinlib connect to those wallets and manages everything, creating some nice possibilities. The Bitcoin Core node is connected to other nodes and thus the Blockchain, so you are not dependant on third party service providers, which makes this a safe, reliable and fast setup.


The Setup
---------

What you need:

A spare server with at least 2 TB diskspace
Installed with Ubuntu 22.04 or other Linux distro
Two or more days to wait for blockchain download and Blockbook synchronisation
Installatie

Eerst docker installeren en python3-dev + python3-pip
Versie Ubuntu 24.04 werkte niet op vierkant nu versie 22.04 gebruikt
Blockbook downloaden van https://github.com/trezor/blockbook
Zie installatie instructies: https://trezor.io/learn/a/custom-backend-in-trezor-suite

Port 9130 open zetten.
