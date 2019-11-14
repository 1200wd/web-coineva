Create a Litecoin Multisig Wallet
=================================

:date: 2018-05-11 17:44
:modified: 2019-11-14 22:46
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

    $ clw -g -n litecoin
    Command Line Wallet for BitcoinLib

    Your mnemonic private key sentence is: donkey blame tunnel album awake turkey fatigue immune keen nice gown alert

    Please write down on paper and backup. With this key you can restore your wallet and all keys

    Type 'yes' if you understood and wrote down your key: yes
    Private Master key, to create multisig wallet on this machine:
    Ltpv71G8qDifUiNetQH49pk8pBpNUeJZx4xBKvzESga8AkuRyqdUfNHKNAnSVK97DjYrq7UcPSkruByUpS6B9sDThcLeHEJ7ALKjVHFioeFf2RB
    Public Master key, to share with other cosigner multisig wallets:
    Ltub2VECoJe5hBU8kNinfTfFsyPz5qfDMiFhPmmWi89yMBGJH9MtjZk6zmhcmvg8FXm3ZBDRibocbSfFzGaczfrUjWT4ZsXNhbCchwr48MZgXyS
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

    $ clw -g -n litecoin
    Your mnemonic private key sentence is: timber replace put whale tunnel swamp lawn alley consider farm betray actor

    Please write down on paper and backup. With this key you can restore your wallet and all keys

    Type 'yes' if you understood and wrote down your key: yes
    Private Master key, to create multisig wallet on this machine:
    Ltpv71G8qDifUiNesRsfsyPyg1qKDQPXs1EQv3th2LT8qQE44UADuQVDiKkvbGkLST5512opQsZaqudU3cdRLsJUUC2zS45XHgYdfK1MsyNJKVN
    Public Master key, to share with other cosigner multisig wallets:
    Ltub2UpT1zg3aS9mgDSoxF1KxXTFWQWJdySpgtQ8WMRX7pFX7BXfshnMjRP4LqApSVETddt6B9NBnjW4XqhWPprZXKfKk9oWEmUV8MsoVZ3EW5f
    Network: litecoin


Copy the public account key and use it to create the wallet in the next step.


Install the offline wallet
--------------------------

You are now ready to create the offline wallet. For this you need the 2 public account
keys created in the previous steps.

.. code-block:: bash

    $ clw LitecoinMS -n litecoin -m 3 2 Ltub2VECoJe5hBU8kNinfTfFsyPz5qfDMiFhPmmWi89yMBGJH9MtjZk6zmhcmvg8FXm3ZBDRibocbSfFzGaczfrUjWT4ZsXNhbCchwr48MZgXyS Ltub2UpT1zg3aS9mgDSoxF1KxXTFWQWJdySpgtQ8WMRX7pFX7BXfshnMjRP4LqApSVETddt6B9NBnjW4XqhWPprZXKfKk9oWEmUV8MsoVZ3EW5f
    Command Line Wallet - BitcoinLib 0.4.11

    Wallet LitecoinMS does not exist, create new wallet [yN]? y

    CREATE wallet 'LitecoinMS' (litecoin network)
    Not all keys provided, creating 1 additional keys

    Your mnemonic private key sentence is: planet fashion payment involve lens night pattern truck feel antenna demand bean

    Please write down on paper and backup. With this key you can restore your wallet and all keys

    Type 'yes' if you understood and wrote down your key: yes
    Wallet info for LitecoinMS
    === WALLET ===
     ID                             35
     Name                           LitecoinMS
     Owner
     Scheme                         bip32
     Multisig                       True
     Multisig Wallet IDs            36, 37, 38
     Cosigner ID                    0
     Witness type                   legacy
     Main network                   litecoin
     Latest update                  None

    = Multisig Public Master Keys =
        0 241 Ltub2VECoJe5hBU8kNinfTfFsyPz5qfDMiFhPmmWi89yMBGJH9MtjZk6zmhcmvg8FXm3ZBDRibocbSfFzGaczfrUjWT4ZsXNhbCchwr48MZgXyS bip32  cosigner *
        1 245 Ltub2V3tPynSv6pHv8tjXE3chMuDNybh1DmQXuKQ9bALUZ1Zw811u9PFS6QyEcKrC72PmK8rSyb1mv1mRHjTt22UrtmsP1hmrvTWz4vdPDZMUvR bip32  main
        2 250 Ltub2UpT1zg3aS9mgDSoxF1KxXTFWQWJdySpgtQ8WMRX7pFX7BXfshnMjRP4LqApSVETddt6B9NBnjW4XqhWPprZXKfKk9oWEmUV8MsoVZ3EW5f bip32  cosigner
    For main keys a private master key is available in this wallet to sign transactions. * cosigner key for this wallet


As you noticed the script creates the 3rd missing key, which is our offline key. I wouldn't
backup this key as it probably only degrades your security.


Final step: Create the Online wallet
------------------------------------

Go back to the online PC again. Use the private key created in the first step on this
online device and the public account keys from backup and offline wallet.

Then to create the new 2 of 3 multisig wallet type:

.. code-block:: bash

    $ clw LitecoinMS-on -n litecoin -m 3 2 Ltpv71G8qDifUiNetQH49pk8pBpNUeJZx4xBKvzESga8AkuRyqdUfNHKNAnSVK97DjYrq7UcPSkruByUpS6B9sDThcLeHEJ7ALKjVHFioeFf2RB Ltub2UpT1zg3aS9mgDSoxF1KxXTFWQWJdySpgtQ8WMRX7pFX7BXfshnMjRP4LqApSVETddt6B9NBnjW4XqhWPprZXKfKk9oWEmUV8MsoVZ3EW5f Ltub2V3tPynSv6pHv8tjXE3chMuDNybh1DmQXuKQ9bALUZ1Zw811u9PFS6QyEcKrC72PmK8rSyb1mv1mRHjTt22UrtmsP1hmrvTWz4vdPDZMUvR
    Command Line Wallet - BitcoinLib 0.4.11

    Wallet LitecoinMS-on does not exist, create new wallet [yN]? y

    CREATE wallet 'LitecoinMS-on' (litecoin network)
    Wallet info for LitecoinMS-on
    === WALLET ===
     ID                             39
     Name                           LitecoinMS-on
     Owner
     Scheme                         bip32
     Multisig                       True
     Multisig Wallet IDs            40, 41, 42
     Cosigner ID                    0
     Witness type                   legacy
     Main network                   litecoin
     Latest update                  None

    = Multisig Public Master Keys =
        0 261 Ltub2VECoJe5hBU8kNinfTfFsyPz5qfDMiFhPmmWi89yMBGJH9MtjZk6zmhcmvg8FXm3ZBDRibocbSfFzGaczfrUjWT4ZsXNhbCchwr48MZgXyS bip32  main     *
        1 266 Ltub2UpT1zg3aS9mgDSoxF1KxXTFWQWJdySpgtQ8WMRX7pFX7BXfshnMjRP4LqApSVETddt6B9NBnjW4XqhWPprZXKfKk9oWEmUV8MsoVZ3EW5f bip32  cosigner
        2 270 Ltub2V3tPynSv6pHv8tjXE3chMuDNybh1DmQXuKQ9bALUZ1Zw811u9PFS6QyEcKrC72PmK8rSyb1mv1mRHjTt22UrtmsP1hmrvTWz4vdPDZMUvR bip32  cosigner
    For main keys a private master key is available in this wallet to sign transactions. * cosigner key for this wallet


Verify if the first address is the same in the offline and online wallet.


Next step: Create a Transaction
-------------------------------

Now your 2 of 3 Litecoin multisig wallet is complete and ready to store litecoins.
In the next article I will explain how to spend them and
`create a Litecoin multisig transaction <{filename}/create-litecoin-multisig-transaction.rst>`_
