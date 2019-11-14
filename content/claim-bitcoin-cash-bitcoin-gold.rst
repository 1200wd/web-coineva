Claim your Bitcoin Gold, Bitcoin Cash or other forks
====================================================

:date: 2017-12-13 13:54
:modified: 2017-12-13 18:22
:tags: bitcoin, bitcoin gold, bitcoin cash, bitcoin diamond, claim, fork, manual
:category: Software Wallets
:slug: claim-bitcoin-cash-bitcoin-gold-or-other-forks
:authors: Lennart Jongeneel
:summary: How to claim your Bitcoin Cash, Bitcoin Gold or other coins after a bitcoin hard fork
:language: en


When can you claim your Bitcoin Cash or Gold?
---------------------------------------------

If you had bitcoins in your hardware of software wallet on the date of the fork you can claim
your coins. You need to know the private keys of the corresponding bitcoin addresses containing
value on the date of the fork.

You can not claim any forked coin if you stored your bitcoins on an exchange or online wallet.

.. image:: /images/forks-are-cool.jpg
   :width: 450px
   :alt: Cool Forks
   :align: left

Bitcoin Cash forked on August 1th 2017, Bitcoin Gold on October 24th and Bitcoin Diamond on
November 24th. More forks will probably follow, a complete list can be found on Wikipedia
(https://en.wikipedia.org/wiki/List_of_Bitcoin_forks)


What is a fork, what happened?
------------------------------

When the first major Bitcoin fork in August 2017 took place nothing happened to Bitcoin itself.
The network, protocol and blockchain with all the transactions stayed exactly the same.
The only thing what happened was that some people / miners copied the blockchain with all the
transactions - and thus address balances - and changed a few things in the protocol.

With the Bitcoin Cash fork for instance the size of the blocks was increased, allowing more
transactions but increasing demand on storage and bandwidth. But no politics here, just
Google 'blocksize debate' to find more about this fierce debate with lasted for years.


Do I have to claim my Bitcoin Gold, Cash or Diamond?
----------------------------------------------------

No. If you have the private keys and keep them you are already the owner of the Bitcoin Gold,
Diamond or Cash coins or whatever future forks might occur. You can always claim them later.
Only if you want to use or exchange them you need to take some actions described below.


How do I claim Bitcoin Gold, Cash or Diamond?
---------------------------------------------

There are many ways to do this, but on this page I will try to describe the easiest way in my
opinion.

1. Transfer the bitcoins to another address in the same or another wallet.
2. Second step is to find the private key.
3. Then sweep the private key and transfer it to your Coinomi wallet.
4. As final step you can leave the coins in your Coinomi wallet or exchange it for Bitcoins or another coin.

First a little warning:


Beware of phishing and scams
----------------------------

Some website ask you to enter a private key to claim your forked coins.
This is not the way to claim your coins. It could be a phishing website, the
website could be hacked or someone could intercept your internet traffic resulting in loss
of all your bitcoins.

So never enter your private key on any website, even if you fully trust the website!


Step 1: Transfer the bitcoins to another address
------------------------------------------------

To reduce risks it is advisable to transfer the bitcoins to another private key / address.
It is not needed but just good practice before you start working with a private key.

If you bitcoins are stored on a paper wallet you find more information on how transfer on
this page:
`What to do with my paper wallet? <{filename}/what-to-do-with-my-paper-wallet.rst>`_

Otherwise just create a transaction in your wallet and send to one of your own addresses:
Copy the address from receive and paste it to send.


Step 2: Look for your private key
---------------------------------

Now look for your private keys. This is different for every wallet, in Electrum for instance
go to the address tab and right click on an address which had funds on the day of the fork -
could be in 'used' addresses - and then select 'Private Key'. If you cannot find a private key in
your wallet you might have to unlock it first.

.. image:: /images/electrum-get-private-key.png
   :width: 600px
   :alt: Get your private key from Electrum
   :align: center

Be careful with your private key, do not share it with anyone.


Step 3: Sweep the private key with Coinomi
------------------------------------------

Install or update Coinomi on your android device. Follow the installation instructions and
make sure you make a backup of the Coinomi recovery phrase.

.. image:: /images/coinomi-add-coin.png
   :width: 450px
   :alt: Add Bitcoin Gold to Coinomi
   :align: center

Next open the left menu and select '+ Coins' and add Bitcoin Gold, Bitcoin Diamond or any other
forked coin.

Go to the coin, select 'Sweep wallet' from the right menu and scan the QR code of the private
key from the previous step. Your coins are now swept to your coinomi wallet and are visible within
a few moments. Before you can use them they need to be confirmed / included in a block this
can take a while.

Repeat this process with every address with coins in your wallet.


Step 4: Exchange, Transfer or store your new coins
--------------------------------------------------

Once you have received the new coins in your Coinomi wallet it is up to you what to do with them.
You can leave them in Coinomi, although this is not advised for larger amount as your phone
is probably not a very secure device. Or you can transfer them to another wallet or exchange.

.. image:: /images/coinomi-shapeshift-exchange.png
   :width: 450px
   :alt: Add Bitcoin Gold to Coinomi
   :align: center

Coinomi also has the option to exchange coins within the same wallet. For instance to exchange from
Bitcoin Cash to Bitcoin: open your Bitcoin Cash page and select 'ShapeShift' from the left menu.
You can now choose how many funds you would like to exchange, select 'Next' and enter your password
to proceed. Now your funds will be send to ShapeShift in the background and - this is a bit scary -
disappear from your wallet, it can take a while before the bitcoins show up.
