Fascinating Bitcoin Transactions Part 1 - Reward to Attack Hashing Algorithms
=============================================================================

:date: 2024-04-23 21:35
:modified: 2024-04-23 21:46
:tags: bitcoin, blockchain, fascinating transactions, collision attacks, hash collision, crack cryptographic algorithms
:category: Fascinating Transactions
:slug: fascinating-bitcoin-transactions-part-1
:authors: Lennart Jongeneel
:summary: Fascinating Bitcoin Transactions Part 1: Get rewarded to crack widely used cryptographic algorithms such as SHA1, SHA256 or RIPEMD160
:language: en

.. :slug: fascinating-bitcoin-transactions-part-1:

.. image:: /images/attack-algorithms.jpg
   :width: 1152px
   :alt: Algorithm attack monsters
   :align: center

In 2013 Peter Todd `offered rewards <https://bitcointalk.org/index.php?topic=293382.0>`_
for anyone who could demonstrate hash collisions in some widely used hashing algorithms.

These cryptographic algorithms such as SHA-256, double SHA-256, RIPEMD-160 and combinations are not only used in Bitcoin
but in many security applications in banking, digital signatures and password hashing.
So a successful attack on SHA-256 or RIPEMD-160 would have far-reaching consequences for the security of
numerous cryptographic applications and systems.

The rewards are locked in utxo's in various transaction which can only be unlocked if someone founds a collision
in one of the hashing algorithms.


What are hash collisions?
-------------------------

In cryptography, hash collisions occur when two different inputs produce the same hash output.
Hash functions are designed to map data of arbitrary size to a fixed-size output, and ideally, each unique
input should produce a unique hash value. However, due to the finite nature of hash outputs and the infinite
nature of possible inputs, collisions can occur.

Hash collisions can be problematic in cryptographic applications because they can potentially undermine the
security of systems that rely on hash functions. For example, in digital signatures, if two different messages
produce the same hash value and one message is signed by a legitimate party, an attacker could substitute the
other message, leading to a forged signature.


The reward transaction
----------------------

In Transaction `397f12ee15f8a3d2ab25c0f6bb7d3c64d2038ca056af10dd8251b98ae0f076b0 <https://blocksmurfer.io/btc/transaction/397f12ee15f8a3d2ab25c0f6bb7d3c64d2038ca056af10dd8251b98ae0f076b0>`_
Peter Todd offered 0.1 bitcoin for anyone who could find a collision for the SHA1, SHA256, RIPEMD160,
RIPEMD160(SHA256()) and SHA256(SHA256()) algorithms.

By offering rewards for demonstrating hash collisions, Todd aimed to encourage researchers to explore
potential weaknesses in various hashing algorithms and to assess its collision resistance.
Finding a hash collision in SHA-256 for example would have significant implications for the security
of Bitcoin and other cryptocurrencies, as it could potentially undermine the integrity of the
blockchain and compromise the immutability of transactions.

.. code-block:: text

    Transaction Details
    ID	            397f12ee15f8a3d2ab25c0f6bb7d3c64d2038ca056af10dd8251b98ae0f076b0
    Network	        bitcoin
    Block	        257674
    Date	        2013-09-13 07:59:09
    Status	        confirmed
    Confirmations	582894
    Type	        legacy
    Coinbase	    False
    Size / VSize	745 / 745
    Fee	            100001 satoshi , 134.2 sat/vB
    Version	        1
    Locktime	    0
    Raw	01000000034da64e544f47eed4075a65051aa62dfac20d36c053...
    Inputs
    0	1FCYd7j4CThTMzts78rh6iQJLBRGPW9fWv	0.00000001	sig_pubkey
    1	1FCYd7j4CThTMzts78rh6iQJLBRGPW9fWv	0.10000000	sig_pubkey
    2	1FCYd7j4CThTMzts78rh6iQJLBRGPW9fWv	0.50000000	sig_pubkey
    Outputs
    0	37k7toV1Nv4DfmQbmZ8KuZDQCYK9x5KpzP	0.10000000	p2sh
    1	35Snmmy3uhaer2gTboc81ayCip4m9DT4ko	0.10000000	p2sh
    2	3KyiQEGqqdb4nqfhUzGKN6KPhXmQsLNpay	0.10000000	p2sh
    3	39VXyuoc6SXYKp9TcAhoiN1mb4ns6z3Yu6	0.10000000	p2sh
    4	3DUQQvz4t57Jy7jxE86kyFcNpKtURNf1VW	0.10000000	p2sh
    5	1FCYd7j4CThTMzts78rh6iQJLBRGPW9fWv	0.09900000	p2pkh

If you look up these addresses on a block explorer you can see other people added bounties to the addresses as
well.


How does this reward work?
--------------------------

The reward is locked up in a transaction output in a regular p2sh (pay-to-script-hash) script, but it's not protected
with a signature but with a computational puzzle. Anyone who can solve the puzzle gets the bitcoins as reward.

The puzzle script looks like this:

.. code-block:: text

    OP_2DUP OP_EQUAL OP_NOT OP_VERIFY OP_SHA1 OP_SWAP OP_SHA1 OP_EQUAL

This script:

* Duplicates 2 sets of data (OP_DUP2) and then tests if they are not equal (OP_EQUAL OP_NOT OP_VERIFY)
* It hashes the first script with SHA1 (OP_SHA1)
* and then it swaps the hash and the other script on the stack and hashes the other data item (OP_SWAP OP_SHA1)
* Finally it checks if the 2 hashes are equal, and if they are you have found a collision


Collision found!
----------------

On 13 february 2017 the SHA-1 hashing algorithm could be considered broken as a hash collision was found, and
the total reward of 2.48 bitcoin was claimed transaction  `8d31992805518fd62daa3bdd2a5c4fd2cd3054c9b3dca1d78055e9528cff6adc <https://blocksmurfer.io/btc/transaction/8d31992805518fd62daa3bdd2a5c4fd2cd3054c9b3dca1d78055e9528cff6adc>`_

Fortunately the SHA-256, RIPEMD-160 and other bounties where not claimed and no hash collisions have been found,
otherwise we and Bitcoin would be in great trouble.

