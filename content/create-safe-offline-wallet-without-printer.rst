Guide: Create a safe offline wallet without printer
===================================================

:date: 2018-02-23 21:54
:modified: 2018-02-23 21:54
:tags: bitcoin, litecoin, paper wallet, no printer, passphrase, bitcoinlib, guide
:category: How To
:slug: create-safe-offline-wallet-without-printer
:authors: Lennart Jongeneel
:summary: Create a (almost) 100% safe offline crypto currency vault on an offline system without using a printer
:language: en


What's wrong with a printer?
----------------------------

Many things. Most printers contain a large storage device which remembers all printed documents for a indefinite amount
of time. There are good changes you communicate to your printer via a wireless network which packages can be easily
intercepted in various ways. And almost all modern printers are online, continuously connected to the internet and
safety is not high on the list of priorities of the printer manufacturers.

So if you print an offline 'super secure' paper wallet it could be intercepted and emptied before the print is
finished or the funds could disappear after 5 years when your dump your printer in the garbage and someone is so
clever to check the hard drive in the printer.


Steps to create an offline wallet: Prepare Laptop
=================================================

First you need a old PC or laptop which you can miss and keep offline. Install a fresh copy of Linux OS such as
Debian or Ubuntu on it and then install the Python BitcoinLib. See https://github.com/1200wd/bitcoinlib

Ubuntu allows you to encrypt your home folder or the full disc. It is adviced to use this option, but select a
strong encryption password and do not forget it.

.. code-block:: bash

   pip install bitcoinlib

Look at http://bitcoinlib.readthedocs.io/en/latest/_static/manuals.install.html for detailed installation instructions.

To show QR codes in the terminal you can optionaly install a python QR code module

.. code-block:: bash

   pip install qrcodelib

Disclaimer: The Python Bitcoin Library BitcoinLib has been tested and used extensively but is still in Alpha
development phase. To use it technical knowledge is required and a basic understanding of python is recommended.
Please use carefully and at your own risk.


Next Step: Create a Wallet
==========================

After your laptop is configured and the BitcoinLib is working take if offline so we can create a new secure wallet.

Go to the tools directory of bitcoinlib, create a new wallet and generate an address to receive funds.

.. code-block:: bash

   python cli-wallet.py offline-wlt -r

Type 'y' to create an new wallet and write down to passphrase to at least 2 pieces of paper as backup. You can
recreate a wallet with one of these pieces of paper if you lose access to your PC/Laptop

.. image:: /images/bitcoinlib-create-wallet.png
   :width: 800px
   :alt: Create a BitcoinLib wallet
   :align: center


Receive funds in your offline wallet
====================================

If you have installed the qrcodelib you can now scan the QR code with another online application to get the
address so you can transfer funds to the offline wallet.

Without QR code module you have to retype the address in the application you wish to use to create a transaction.

You can create as many receive addresses as you wish by recalling the CLI wallet with the -r option.
.. code-block:: bash

   python cli-wallet.py offline-wlt -r


Send funds with an offline wallet
=================================

Now if you would like to spend the funds in your offline wallet you have to create a transaction on your offline PC.

