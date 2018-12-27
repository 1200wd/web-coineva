Create a Litecoin Multisig Wallet
=================================

:date: 2018-05-11 17:44
:modified: 2018-06-28 16:29
:tags: litecoin, multisig, wallets, bitcoinlib, commandline wallets, manual
:category: BitcoinLib
:slug: create-litecoin-multisig-wallet
:authors: Lennart Jongeneel
:summary: How to Create a Litecoin Multisig Wallet with the BitcoinLib Command Line Utility
:language: en


.. :slug: create-litecoin-multisig-wallet:

This guide explains how to create a Litecoin 2 of 3 multisig wallet with the python
BitcoinLib command line wallet. The wallet has 3 private keys: one stored on a
online device, one on a offline device and one on a paper backup. Transactions are created
on the online device and then signed with the offline PC with the second signature.

If one device gets lost or broken the litecoins can be accessed with the backup key.
And if someone gets access to one of the devices your litecoins are still safe.

The safety of this wallet also depends on the safety of your devices and storage of the
backup key but this is out of scope for this article, so I leave that up to your common sense.

.. image:: /images/litecoin-multisig-2-of-3.jpg
   :width: 308px
   :alt: Litecoin Multisig Wallet with three Keys
   :align: right


Create the first key on your online device
------------------------------------------

Install the `Python BitcoinLib <{filename}/python-bitcoin-library.rst>`_ on your online
device.

Create the first key on your online device with the command line wallet:

.. code-block:: bash

    $ cli-wallet -k -n litecoin
    Command Line Wallet for BitcoinLib

    Your mnemonic private key sentence is: expect soul bleak false pistol soldier candy patch van chief gown hidden

    Please write down on paper and backup. With this key you can restore your wallet and all keys

    Type 'yes' if you understood and wrote down your key: yes
    Private master key, to create multisig wallet on this machine: Ltpv71G8qDifUiNetzgZt3GLfqZrjm9rBTqXasNG8XJXD9bYm5veLM2rAhp9oM9CQK6hqhjy7LRLdm5aUxmj1gj2Xdryd1WnT1Bfe65zQEpnAnW
    Public account key, to share with other cosigner multisig wallets: Ltub2ZqiB1iohBAr39Ge8ahyh7y5mWM7nqewTSCxM9Ad8p7KZbLue6yCyiLUWExjfgJRtraSH6NL4d2rVWKasogDFB2aH1aD1FvX5Pynma2ws9x
    Network: litecoin

Now store the private and public key on a safe location on your online device.

(You can choose to create a backup of this key on paper or on another encrypted device in
case both your online and offline device get lost or broken. This creates an extra
security risk of course, so I leave it up to you. In any case: Do not store this backup
together with the offline device or other paper backup!)


The backup key
--------------

Install BitcoinLib on your offline device and then make sure it never goes online again.

Create the backup key and write down the Mnemonic passphrase on a piece of paper. Or on
a couple of papers and store them in vaults around the globe.

.. code-block:: bash

    $ cli-wallet -k -n litecoin
    Your mnemonic private key sentence is: uphold armed exclude deputy notice vapor walk want refuse hamster voice luggage

    Please write down on paper and backup. With this key you can restore your wallet and all keys

    Type 'yes' if you understood and wrote down your key: yes
    Private master key, to create multisig wallet on this machine: Ltpv71G8qDifUiNetAk2BX3zATxqrQ3xb3D5HmJWnffypn8eB6Htxxe23aoE31ze9REecUoZfwVEYgtBWNLzcEa1fy413MQY9DUmUWbbMSBoCL2
    Public account key, to share with other cosigner multisig wallets: Ltub2YHuCvWXkysuEArgYFXTasxVL8mCqq4GJjFMC9KYE71bvBY3Xf2EbS7bWQPpae4BLkL2mJh4HPqubzgD2cnYaJX3rwurRbHg5iV417HsDaf


Copy the public account key and use it to create the wallet in the next step.


Install the offline wallet
--------------------------

You are now ready to create the offline wallet. For this you need the 2 public account
keys created in the previous steps.

.. code-block:: bash

    $ cli-wallet LitecoinMS -n litecoin -m 3 2 Ltub2ZqiB1iohBAr39Ge8ahyh7y5mWM7nqewTSCxM9Ad8p7KZbLue6yCyiLUWExjfgJRtraSH6NL4d2rVWKasogDFB2aH1aD1FvX5Pynma2ws9x Ltub2YHuCvWXkysuEArgYFXTasxVL8mCqq4GJjFMC9KYE71bvBY3Xf2EbS7bWQPpae4BLkL2mJh4HPqubzgD2cnYaJX3rwurRbHg5iV417HsDaf
    Command Line Wallet for BitcoinLib

    Wallet LitecoinMS does not exist, create new wallet [yN]? y

    CREATE wallet 'LitecoinMS' (litecoin network)
    Not all keys provided, creating 1 additional keys

    Your mnemonic private key sentence is: remind trend relax shoot depth song attract horse woman pulse hotel often

    Please write down on paper and backup. With this key you can restore your wallet and all keys

    Type 'yes' if you understood and wrote down your key: yes
    Updating wallet
    Wallet info for LitecoinMS
    === WALLET ===
     ID                             21
     Name                           LitecoinMS
     Owner
     Scheme                         multisig
     Multisig Wallet IDs            22, 23, 24
     Main network                   litecoin

    = Multisig Public Account Keys =
      207 Ltub2YHuCvWXkysuEArgYFXTasxVL8mCqq4GJjFMC9KYE71bvBY3Xf2EbS7bWQPpae4BLkL2mJh4HPqubzgD2cnYaJX3rwurRbHg5iV417HsDaf cosigner
      208 Ltub2ZqiB1iohBAr39Ge8ahyh7y5mWM7nqewTSCxM9Ad8p7KZbLue6yCyiLUWExjfgJRtraSH6NL4d2rVWKasogDFB2aH1aD1FvX5Pynma2ws9x cosigner
      209 Ltub2Z59wHwYHf9Yu448iWRDHZh8tLicBSM1bx5XVoNNkKhhVnkhEwa8tDKtugKZhCwbv4DHf2B6UhoCMptc6x3g3MsRuCMuNAaMrkZVKnvzwJ6 main
    For 'main' keys a private master key is available in this wallet to sign transactions.


As you noticed the script creates the 3rd missing key, which is our offline key. I wouldn't
backup this key as it probably only degrades your security.


Final step: Create the Online wallet
------------------------------------

Go back to the online PC again. Use the private key created in the first step on this
online device and the public account keys from backup and offline wallet.

Then to create the new 2 of 3 multisig wallet type:

.. code-block:: bash

    $ cli-wallet LitecoinMS-on -n litecoin -m 3 2 Ltpv71G8qDifUiNetzgZt3GLfqZrjm9rBTqXasNG8XJXD9bYm5veLM2rAhp9oM9CQK6hqhjy7LRLdm5aUxmj1gj2Xdryd1WnT1Bfe65zQEpnAnW Ltub2Z59wHwYHf9Yu448iWRDHZh8tLicBSM1bx5XVoNNkKhhVnkhEwa8tDKtugKZhCwbv4DHf2B6UhoCMptc6x3g3MsRuCMuNAaMrkZVKnvzwJ6 Ltub2YHuCvWXkysuEArgYFXTasxVL8mCqq4GJjFMC9KYE71bvBY3Xf2EbS7bWQPpae4BLkL2mJh4HPqubzgD2cnYaJX3rwurRbHg5iV417HsDaf
    CREATE wallet 'LitecoinMS-on' (litecoin network)
    Updating wallet
    Wallet info for LitecoinMS-on
    === WALLET ===
     ID                             25
     Name                           LitecoinMS-on
     Owner
     Scheme                         multisig
     Multisig Wallet IDs            26, 27, 28
     Main network                   litecoin

    ...

    - NETWORK: litecoin -
    - - Keys
      234 m/45'/2'/0'/0/0              3Pp8bBac8UGLAHtV7R1PtDwiEXw7HY6qpD            Multisig Key 233/232/230             0.00000000 LTC


Verify if the first address is the same in the offline and online wallet.


Next step: Create a Transaction
-------------------------------

Now your 2 of 3 Litecoin multisig wallet is complete and ready to store Litecoins.
In the next article I will explain how to spend them and
`create a Litecoin multisig transaction <{filename}/create-litecoin-multisig-transaction.rst>`_
