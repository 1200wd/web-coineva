Create an Electrum Wallet
=========================

:date: 2017-06-01 14:36
:modified: 2017-06-01 14:36
:tags: bitcoin, wallets, electrum, manual
:category: Software Wallets
:slug: create-electrum-wallet
:authors: Lennart Jongeneel
:summary: Step-by-step instruction guide to create Electrum wallet
:language: en


.. _create-electrum-wallet:

Go to http://electrum.org and download the easy installation software for your platform,
i.e.: Windows, Android, Linux.

.. image:: /images/electrum-download.png
   :width: 1200px
   :alt: Download Electrum wallet
   :align: center

Start the Electrum software and select auto connect, after this you will be guided to the setup
process the create a new wallet.

.. image:: /images/electrum-create-wallet.png
   :width: 1200px
   :alt: Create new Electrum Wallet
   :align: center

Use the default settings, so choose 'Standard wallet' and then 'Create a new seed'.
Write down the 12 words on a piece of paper and put them in a safe place.
Preferable 2 or more pieces of paper depending on the
amount off bitcoins you are going to store. Do not copy-paste, print-screen or store your 12 word seed
electronically, then you will more vulnerable for an attack.

.. image:: /images/electrum-create-new-seed.png
   :width: 1200px
   :alt: Generate a new seed
   :align: center

To verify you have got the passphrase correctly you will be asked to enter the 12 words again.
This is a bit of a hassle, but is really necessary to 'play your own bank' and secure your bitcoins.
After setting everything up you only need your password to enter and use your wallet.

.. image:: /images/electrum-confirm-seed.png
   :width: 1200px
   :alt: Confirm your private key seed
   :align: center

Now choose a strong password and remember it or store it in a password manager. If you forgot your
password you will able to recreate your wallet with the 12-word passphrase.

.. image:: /images/electrum-strong-password.png
   :width: 1200px
   :alt: Enter a strong password
   :align: center

Your wallet is ready, you can now
`transfer funds from your paper wallet into Electrum <{filename}/paper-wallet-import-electrum.rst>`_
or buy some bitcoins.


Security
--------

Your wallet is protected with a password and is secured against loss with writen backups of
the private key. However if your computer has bad security and anyone gains access and is capable
of installing software they can gain access to your bitcoins. So please update regularly, choose strong passwords,
use a good virus scanner and firewall. This is not the place to elaborate too much about security, there is
`more security information <https://antivirus.comodo.com/blog/computer-safety/5-simple-steps-protect-pc/>`_
out there.
