Create a Litecoin Multisig Transaction
======================================

:date: 2018-05-16 19:11
:modified: 2018-05-16 19:54
:tags: litecoin, LTC, multisig, send transaction, create transaction, bitcoinlib, CL wallet
:category: BitcoinLib
:slug: create-litecoin-multisig-transaction
:authors: Lennart Jongeneel
:summary: Create a Litecoin Multisig Transaction with the 2-of-3 multisig wallet using the BitcoinLib Command Line Utility
:language: en


.. :slug: create-litecoin-multisig-transaction:


This guide assumes you `created a Litecoin 2-of-3 wallet <{filename}/create-litecoin-multisig-wallet.rst>`_
following the previous article.

We will create a Litecoin multisig transaction using the command line wallet from
`Python BitcoinLib <{filename}/python-bitcoin-library.rst>`_ with the online main wallet
and an offline wallet.


Create transaction with online wallet
-------------------------------------

First update your wallet and unspent transaction outputs:

.. code-block:: bash

    $ cli-wallet LitecoinMS-on
    Command Line Wallet for BitcoinLib

    Updating wallet
    Wallet info for LitecoinMS-on
    === WALLET ===
     ID                             25
     Name                           LitecoinMS-on
     Owner
     Scheme                         multisig
     Multisig Wallet IDs            26, 27, 28
     Main network                   litecoin

    = Multisig main keys =
      221 m/45'/2'/0'                  LVcDqvm8wJ29KDZb4KUyi8jP2LYRbAbzry            LitecoinMS-on-cosigner-0
      222 m/45'/2'/0'                  LPHQRc7pWM8kT1bxk1tSEFD69ms3zDwyev            LitecoinMS-on-cosigner-1
      223 m                            LP5Rwvu4FVjiSThXssnN3nb4UYVi3N77vi            LitecoinMS-on-cosigner-2

    - NETWORK: litecoin -
    - - Keys
      234 m/45'/2'/0'/0/0              3Pp8bBac8UGLAHtV7R1PtDwiEXw7HY6qpD            Multisig Key 233/232/230             0.03266639 LTC

    - - Transactions (Account 0, Ltub2SSUS19CirucWsPQ8ekikRQ5BKr3FiQBfPUHoW4p9LP9MT7ifG5HBJvR3kkowxFm8aXiMSXXgRQfZHVGQCDWyMnBvnsDUzMkKT9eBQnt1nk)
      10 9a9b4c9c9decefd50b7f40c3a243bbd514a18958cda70aa4fe9f82e0726e4d2f   3Pp8bBac8UGLAHtV7R1PtDwiEXw7HY6qpD        1       3266639 U

    = Balance Totals (includes unconfirmed) =
    litecoin             (Account 0)                0.03266639 LTC


..  == Restore wallet from backup
    = Online wallet lost
    Online PC:
    create new temporary wallet with public keys and backup key
    create new multisig wallet
    transfer funds to new wallet (see create transaction section)
    = Offline wallet lost
    Online PC:
    create transaction
    create new multisig wallet
    Offline PC:
    sign transaction with backup key
    Online PC
    send tx to new wallet