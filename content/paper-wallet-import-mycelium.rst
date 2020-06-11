Import a paper wallet into Mycelium
===================================

:date: 2017-06-01 14:36
:modified: 2018-06-28 17:12
:tags: bitcoin, wallets, mycelium, paper wallets, manual
:category: Paper Wallets
:slug: paper-wallet-import-mycelium
:authors: Lennart Jongeneel
:summary: How to import a paper wallet into Mycelium
:language: en


.. _paper-wallet-import-mycelium:

After you have successfully
`setup a Mycelium wallet <{filename}/create-mycelium-wallet.rst>`_
on your phone you can
continue to import your paper wallet. Select 'Cold storage' (= Paper wallets)
from the main menu and then select 'QR code'
to scan the Private key from your paper wallet.

.. image:: /images/mycelium-your-account.png
   :width: 400px
   :alt: Scan private key with Mycelium from 'cold storage'
   :align: center

Now you are ready to create the transaction. Be sure to select an address from your own wallet.
You should see a warning: You are sending a payment to your own address.

.. image:: /images/mycelium-create-transaction.png
   :width: 400px
   :alt: Scan private key with Mycelium from 'cold storage'
   :align: center

It is advised to take all the bitcoins of the paper wallet in one transaction. To do
this click on the keyboard and select 'max'. In case you are not in a hurry, you can
select 'low-prio' from the miner fee selection.

.. image:: /images/mycelium-create-transaction-max-amount.png
   :width: 400px
   :alt: Sweep complete cold storage / paper wallet
   :align: center

Your transaction is now being processed and shows up in your wallet as pending.
It might take a couple of hours or more if you have selected low priority fee,
but you can already use your bitcoins.

.. image:: /images/mycelium-transaction-done.png
   :width: 400px
   :alt: Waiting to confirm...
   :align: center
