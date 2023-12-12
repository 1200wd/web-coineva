Send and Receive Bitcoin from Commandline
=========================================

:date: 2022-10-07 08:48
:modified: 2022-10-07 09:32
:tags: bitcoin, wallet, transactions, commandline, bitcoinlib, python
:category: Software Wallets
:slug: send-receive-bitcoin-from-commandline
:authors: Lennart Jongeneel
:summary: Send and Receive Bitcoin from Python Commandline with Bitcoinlib in a few easy steps
:language: en


.. :slug: send-receive-bitcoin-from-commandline:

.. image:: /images/commandline-wallet.png
   :width: 800px
   :alt: Python commandline wallet
   :align: right

Sometimes you just need a simple or temporary wallet to send and receive crypto. In the example below we create a wallet and send bitcoiins with single line python commands. No need for complex software installation or time consuming backup procedures.

Make sure `Python BitcoinLib <https://bitcoinlib.readthedocs.io/en/latest/source/_static/manuals.install.html>`_ is installed before you start.

.. code-block:: bash

   pip install bitcoinlib


Create Wallet
-------------

Now lets create a wallet and get an address to receive Bitcoin Testnet coins.

.. code-block:: python

    >>> from bitcoinlib.wallets import Wallet
    >>> w = Wallet.create("My Testnet Wallet", network="testnet")
    >>> w.info()
    === WALLET ===
     ID                             3
     Name                           My Testnet Wallet
     Owner
     Scheme                         bip32
     Multisig                       False
     Witness type                   legacy
     Main network                   testnet
     Latest update                  None

    = Wallet Master Key =
     ID                             21
     Private                        True
     Depth                          0

    - NETWORK: testnet -
    - - Keys
       26 m/44'/1'/0'/0/0              mvrtuQvMhP79x4p4fPNChGopWoUvVttjUP            address index 0                     0.00000000 TBTC

    - - Transactions Account 0 (0)

    = Balance Totals (includes unconfirmed) =


Make a copy of the wallet private key in case anything goes wrong.

.. code-block:: python

    >>> w.main_key.wif
    'tprv8ZgxMBicQKsPeTWfDcHDjngYVa8LR4VQnn4GtoJLXEtQYpRRkRt6TsqKp2nBRfnJt9vjUTREV8YpjPr8jecxNh1USymackFnAHnD7MEQo7r'


Receive Bitcoins
----------------

We have an address (mvrtuQvMhP79x4p4fPNChGopWoUvVttjUP) and we can receive bitcoins, so lets find a bitcoin faucet and
see if we can get some testnet coins. Just Google for 'bitcoin testnet faucet' and see what you find. I used https://bitcoinfaucet.uo1.net/

The faucet will give you a transaction id, in this case `99f9a76d7b05c409ff4955ba7d91ee83a8835a9f9821c32ff2e987ab8a3fba85 <https://blocksmurfer.io/tbtc/transaction/99f9a76d7b05c409ff4955ba7d91ee83a8835a9f9821c32ff2e987ab8a3fba85>`_
Open any block explorer and you can see if the transaction is received by the network and wait until it confirms.

Let the wallet scan for transactions and see if you have received the testnet coins.

.. code-block:: python

    >>> w.scan(scan_gap_limit=1)
    >>> w.info()
    === WALLET ===
     ID                             3
     Name                           My Testnet Wallet
     Owner
     Scheme                         bip32
     Multisig                       False
     Witness type                   legacy
     Main network                   testnet
     Latest update                  2022-10-07 09:52:56.606693

    = Wallet Master Key =
     ID                             21
     Private                        True
     Depth                          0

    - NETWORK: testnet -
    - - Keys
       26 m/44'/1'/0'/0/0              mvrtuQvMhP79x4p4fPNChGopWoUvVttjUP            address index 0                     0.00010000 TBTC
       28 m/44'/1'/0'/1/0              mtGdVm451fQYh4wQEoMWYAUm6JocHK9LZs            address index 0                     0.00000000 TBTC
       29 m/44'/1'/0'/0/1              n1UDMjicDJ6c2Kuv8eHLcYrZUmGGXfH2Nu            address index 1                     0.00000000 TBTC

    - - Transactions Account 0 (1)
    99f9a76d7b05c409ff4955ba7d91ee83a8835a9f9821c32ff2e987ab8a3fba85          mvrtuQvMhP79x4p4fPNChGopWoUvVttjUP        1       0.00010000 TBTC U

    = Balance Totals (includes unconfirmed) =
    testnet              (Account 0)               0.00010000 TBTC


Send Bitcoins
-------------

With a single line command we can send some bitcoins back to the faucet address:

.. code-block:: python

    >>> w.send_to('tb1ql7w62elx9ucw4pj5lgw4l028hmuw80sndtntxt', 1000, offline=False)
    <WalletTransaction(input_count=1, output_count=2, status=unconfirmed, network=testnet)>

This creates a `transaction <https://blocksmurfer.io/tbtc/transaction/4c0807e0630b772b59db68d9d2b172e415cbdde0a0ea9180f40cbaacfbf34081>`_ and pushes it to the testnet network.

However in a normal situation we would like to check the transaction first before sending it.

.. code-block:: python

    >>> t = w.send_to('tb1ql7w62elx9ucw4pj5lgw4l028hmuw80sndtntxt', 1000)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/lennart/.virtualenvs/bitcoinlib/lib/python3.8/site-packages/bitcoinlib/wallets.py", line 3928, in send_to
        return self.send(outputs, input_key_id=input_key_id, account_id=account_id, network=network, fee=fee,
      File "/home/lennart/.virtualenvs/bitcoinlib/lib/python3.8/site-packages/bitcoinlib/wallets.py", line 3863, in send
        transaction = self.transaction_create(output_arr, input_arr, input_key_id, account_id, network, fee,
      File "/home/lennart/.virtualenvs/bitcoinlib/lib/python3.8/site-packages/bitcoinlib/wallets.py", line 3528, in transaction_create
        selected_utxos = self.select_inputs(amount_total_output + fee_estimate, transaction.network.dust_amount,
      File "/home/lennart/.virtualenvs/bitcoinlib/lib/python3.8/site-packages/bitcoinlib/wallets.py", line 3381, in select_inputs
        raise WalletError("Create transaction: No unspent transaction outputs found or no key available for UTXO's")
    bitcoinlib.wallets.WalletError: Create transaction: No unspent transaction outputs found or no key available for UTXO's

Ah, nasty errors... This means the previous transaction is not confirmed yet.

Normally we would wait a little, but we are in a hurry, so we include the min_confirms=0 to be able to spent unconfirmed outputs.

.. code-block:: python

    >>> t = w.send_to('tb1ql7w62elx9ucw4pj5lgw4l028hmuw80sndtntxt', 1000, min_confirms=0)
    >>> t.info()
    Transaction 24f28bd6be541b61ff1b07b18b35dbc194c466d8671e86678ef812802170c4b1
    Date: None
    Network: testnet
    Version: 1
    Witness type: legacy
    Status: new
    Verified: True
    Inputs
    - mtGdVm451fQYh4wQEoMWYAUm6JocHK9LZs 0.00008773 tBTC 4c0807e0630b772b59db68d9d2b172e415cbdde0a0ea9180f40cbaacfbf34081 0
      legacy sig_pubkey; sigs: 1 (1-of-1) valid
    Outputs
    - tb1ql7w62elx9ucw4pj5lgw4l028hmuw80sndtntxt 0.00001000 tBTC p2wpkh U
    - mhBuzpdhpnb3uf8ZUSPHHsNxiLp1QJvQGs 0.00007546 tBTC p2pkh U
    Size: 222
    Vsize: 222
    Fee: 227
    Confirmations: None
    Block: None
    Pushed to network: False
    Wallet: My Testnet Wallet


    >>> t.send()
    >>> t.info()
    Transaction 24f28bd6be541b61ff1b07b18b35dbc194c466d8671e86678ef812802170c4b1
    Date: None
    Network: testnet
    Version: 1
    Witness type: legacy
    Status: unconfirmed
    Verified: True
    Inputs
    - mtGdVm451fQYh4wQEoMWYAUm6JocHK9LZs 0.00008773 tBTC 4c0807e0630b772b59db68d9d2b172e415cbdde0a0ea9180f40cbaacfbf34081 0
      legacy sig_pubkey; sigs: 1 (1-of-1) valid
    Outputs
    - tb1ql7w62elx9ucw4pj5lgw4l028hmuw80sndtntxt 0.00001000 tBTC p2wpkh U
    - mhBuzpdhpnb3uf8ZUSPHHsNxiLp1QJvQGs 0.00007546 tBTC p2pkh U
    Size: 222
    Vsize: 222
    Fee: 227
    Confirmations: 0
    Block: None
    Pushed to network: True
    Wallet: My Testnet Wallet

So we created a transaction object, checked it and then send it with the Transaction.send() command. As you can see the transaction is pushed to the network and we received a transaction ID.

When the transactions are done and we are finished we can empty the wallet and sweep it to another wallet with a single command.

.. code-block:: python

    >>> w.sweep('tb1ql7w62elx9ucw4pj5lgw4l028hmuw80sndtntxt', offline=False, min_confirms=0)
    <WalletTransaction(input_count=1, output_count=1, status=unconfirmed, network=testnet)>
    >>> w.info()
    === WALLET ===
     ID                             3
     Name                           My Testnet Wallet
     Owner
     Scheme                         bip32
     Multisig                       False
     Witness type                   legacy
     Main network                   testnet
     Latest update                  2022-10-07 09:52:56.606693

    = Wallet Master Key =
     ID                             21
     Private                        True
     Depth                          0

    - NETWORK: testnet -
    - - Keys
       29 m/44'/1'/0'/0/1              n1UDMjicDJ6c2Kuv8eHLcYrZUmGGXfH2Nu            address index 1                     0.00000000 TBTC

    - - Transactions Account 0 (6)
    99f9a76d7b05c409ff4955ba7d91ee83a8835a9f9821c32ff2e987ab8a3fba85          mvrtuQvMhP79x4p4fPNChGopWoUvVttjUP        2       0.00010000 TBTC
    4c0807e0630b772b59db68d9d2b172e415cbdde0a0ea9180f40cbaacfbf34081          mvrtuQvMhP79x4p4fPNChGopWoUvVttjUP        0      -0.00010000 TBTC
    4c0807e0630b772b59db68d9d2b172e415cbdde0a0ea9180f40cbaacfbf34081          mtGdVm451fQYh4wQEoMWYAUm6JocHK9LZs        0       0.00008773 TBTC
    24f28bd6be541b61ff1b07b18b35dbc194c466d8671e86678ef812802170c4b1          mtGdVm451fQYh4wQEoMWYAUm6JocHK9LZs        0      -0.00008773 TBTC
    24f28bd6be541b61ff1b07b18b35dbc194c466d8671e86678ef812802170c4b1          mhBuzpdhpnb3uf8ZUSPHHsNxiLp1QJvQGs        0       0.00007546 TBTC
    97647f0530f810aa5eea5d1062f570f7ee581908c54b61ffb34de3595c49c2ee          mhBuzpdhpnb3uf8ZUSPHHsNxiLp1QJvQGs        0      -0.00007546 TBTC

    = Balance Totals (includes unconfirmed) =
    testnet              (Account 0)               0.00000000 TBTC

And it is empty!

Check `Python BitcoinLib <{filename}/python-bitcoin-library.rst>`_ for more about the bitcoin library.
