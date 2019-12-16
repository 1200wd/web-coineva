Crypto Administration Part 1
============================

:date: 2019-11-19 21:16
:modified: 2019-11-19 23:15
:tags: tax, administration, crypto, cryptocurrency, wallets, bitcoinlib, bitcoin
:category: BitcoinLib
:slug: crypto-tax-administration-1
:authors: Lennart Jongeneel
:summary: Setting up a basic cryptocurrency administration with python Bitcoinlib
:language: en


.. :slug: crypto-tax-administration-1:

When you are using cryptocurrency, no matter in what jurisdiction you're in, sooner or later you will have to set up
a decent administration to comply with your tax obligations. Unfortunately not a lot of accounting software supports crypto.
And furthermore most exchanges and wallets miss basic overviews and export functionality.

With some help of the `Python Bitcoin library <{filename}/python-bitcoin-library.rst>`_ I will show some tricks
to help you set up a crypto administration. In this article we write some code to export wallets and transactions.

.. image:: /images/bitcoin-tax.png
   :width: 824px
   :alt: Pay bitcoin taxes!
   :align: center

Setup readonly wallet
---------------------

If you have the public master key or public account key, you can use that key to setup a readonly wallet with
bitcoinlib. The wallet below uses the bitcoin testnet3 network, but you can also specify the bitcoin, litecoin or dash
network.

.. code-block:: python

    from bitcoinlib.wallets import wallet_create_or_open
    wif_pub = \
    'vpub5YZfEsEFSSDQ9tujabYZoEcwpiFhx7Yzeto99E8sy4F2j6tw9zMnJU6F3grzxKDeEJ6MsKHeoMkxB6hUBnWJKhGy7ZVcT3ZmjjRfDv4hNwe'
    w = wallet_create_or_open('Shopping Wallet', wif_pub)
    w.scan(scan_gap_limit=1)
    w.info()

This will setup the wallet, generate keys and download transactions from various bitcoin service providers. The
wallet's info() method shows the addresses and transactions.

.. code-block:: python

    === WALLET ===
     ID                             1
     Name                           Shopping Wallet
     Owner
     Scheme                         bip32
     Multisig                       False
     Witness type                   segwit
     Main network                   testnet
     Latest update                  2019-11-19 22:18:43.260711

    = Wallet Master Key =
     ID                             1
     Private                        False
     Depth                          3

    - NETWORK: testnet -
    - - Keys
        5 M/0/2                        tb1q4f479gwsp900wl9l8g2tf5007x2xz9qdn7mtjw    address index 2                     0.00010000 TBTC
        6 M/0/3                        tb1q8ltg9f73tm26w7fz7l3qsujlhktnjancpxkffd    address index 3                     0.00011700 TBTC
        7 M/0/4                        tb1qsqhgtwrju08gglmf6gvajvffwxhjh8vzvnykqx    address index 4                     0.00000000 TBTC
       18 M/1/9                        tb1qsjddg0rd54z450kz00xm0nfl44qvewfqa82xsl    address index 9                     0.00287950 TBTC
       19 M/1/10                       tb1qjazjs9tm7xvckmhdn65fcy2dtsjh89cceer7hq    address index 10                    0.00105173 TBTC
       20 M/1/11                       tb1qda0nxl7sgyrwrje9lvkqh30zfs9uudnwnlrsdk    address index 11                    0.00000000 TBTC

    - - Transactions Account 0 (27)
    7722a3c7bd0934522767564943e92a22caaca69e05eec9fbce23fe0a98f044f0 tb1qn36t5vw5ddr7mqukhgvem2wkj9hwjlymtw8j5g       40       1000000
    00c76570c0eb91dfd3c644f6321db4de8e0983d2d0528276abeb08aaae9979a8 tb1q7fm9fvs62q76vgk5q998a35jyhpusprvm6j3w4       39       1000000
    9fbc417ea3bcd8bd076bbac7a481dc7852c8e168173c70955a97e830cd93fab4 tb1q4f479gwsp900wl9l8g2tf5007x2xz9qdn7mtjw       37         10000 U
    eff479895812039b2f4bcea508989bd3498df1595afc028570323a79f21d8693 tb1q8ltg9f73tm26w7fz7l3qsujlhktnjancpxkffd       37          7700 U
    7af39e591a11962cedf6f433f657670d5f0335663788035d9dbe8c0cb7209fb4 tb1q8ltg9f73tm26w7fz7l3qsujlhktnjancpxkffd       37          4000 U
    913011f2fab73c230131501570a9f9d2ada5569fe79c9af0268947c9ddf0c2d2 tb1qn36t5vw5ddr7mqukhgvem2wkj9hwjlymtw8j5g       36      -1000000
    913011f2fab73c230131501570a9f9d2ada5569fe79c9af0268947c9ddf0c2d2 tb1q3l7cfqfx2alnkey9slkf5r8gtecd3k2e033juk       36        958366
    d3a43c327b25b884191ed1aefb39f67463d2d0a61ba0485dfeef1afb26cb8261 tb1q3l7cfqfx2alnkey9slkf5r8gtecd3k2e033juk       36       -958366
    d3a43c327b25b884191ed1aefb39f67463d2d0a61ba0485dfeef1afb26cb8261 tb1qr59yyur6n7xy6n7wrm8va9wt754kjhhmdkdtga       36        935681
    cedd18dc60a87fd39a2c8b4ad6b15442b5a53faf5363bca18a36a305294a3f0f tb1qr59yyur6n7xy6n7wrm8va9wt754kjhhmdkdtga       36       -935681
    cedd18dc60a87fd39a2c8b4ad6b15442b5a53faf5363bca18a36a305294a3f0f tb1qr4t5k0p57evw4dayuvq973cqapwprr5l8cur7q       36        897986
    8b7ada2e6acd6619a080b25991f5d9408ee0b42a6a1ecc0eea304c4345a244b4 tb1qr4t5k0p57evw4dayuvq973cqapwprr5l8cur7q       36       -897986
    8b7ada2e6acd6619a080b25991f5d9408ee0b42a6a1ecc0eea304c4345a244b4 tb1qxlqxgz62x9j8r6uhz6puckrfuzmgd5k60fp7rq       36        861808
    80333162a87bc8e088eaa54f1f6718c0b7caa72a29a2dfe15a8233110f01612d tb1q7fm9fvs62q76vgk5q998a35jyhpusprvm6j3w4       33      -1000000
    80333162a87bc8e088eaa54f1f6718c0b7caa72a29a2dfe15a8233110f01612d tb1qqt5kj0jus0ud36d90d48ecp2593tx9tt6zze6a       33        696456
    449432de51fbe0b5b52a7234b2c860229ca3995888e87dd541a7885211838cc8 tb1qxlqxgz62x9j8r6uhz6puckrfuzmgd5k60fp7rq       33       -861808
    449432de51fbe0b5b52a7234b2c860229ca3995888e87dd541a7885211838cc8 tb1q868k6nepnmrm5tehc68p5km3dzk8neyag0ph6c       33        399125
    9a22ec2e22518678cd6bf4ca88e23c3b7480482be579479ee6db49fbe53f42f7 tb1q868k6nepnmrm5tehc68p5km3dzk8neyag0ph6c       33       -399125
    9a22ec2e22518678cd6bf4ca88e23c3b7480482be579479ee6db49fbe53f42f7 tb1qsuyry7q0sf24pdhrzfl32f0zlg4h2dgr963wcy       33        147415
    796f4c1eec2a242508bcb75b1c57920597d376e381289804255d51d9e8c3b336 tb1qsuyry7q0sf24pdhrzfl32f0zlg4h2dgr963wcy       33       -147415
    796f4c1eec2a242508bcb75b1c57920597d376e381289804255d51d9e8c3b336 tb1q36wljxt3zfxaqe727vjp7lwvtrtpm4lvk9067s       33        121692
    0335d2d56ac5861f8854c7539a9ffcbedc86c274a1603c605b5690a17968ba2f tb1qqt5kj0jus0ud36d90d48ecp2593tx9tt6zze6a       33       -696456
    0335d2d56ac5861f8854c7539a9ffcbedc86c274a1603c605b5690a17968ba2f tb1qjpnl7236ltsm9jy3k9vhsc8fyw4xpwscxxd8np       33        575090
    d3f512ad2ee829cdb8365adfee8afe73700dd2be8706b5542de302bab448df4f tb1qjpnl7236ltsm9jy3k9vhsc8fyw4xpwscxxd8np       26       -575090
    d3f512ad2ee829cdb8365adfee8afe73700dd2be8706b5542de302bab448df4f tb1qsjddg0rd54z450kz00xm0nfl44qvewfqa82xsl       26        287950 U
    5714845c10f0cdf4f4767ebb5b00a05fc8428d4c1a35c4f2f11779353193a8f3 tb1q36wljxt3zfxaqe727vjp7lwvtrtpm4lvk9067s       25       -121692
    5714845c10f0cdf4f4767ebb5b00a05fc8428d4c1a35c4f2f11779353193a8f3 tb1qjazjs9tm7xvckmhdn65fcy2dtsjh89cceer7hq       25        105173 U

    = Balance Totals (includes unconfirmed) =
    testnet              (Account 0)               0.00414823 TBTC

Now the only thing left to do is export the transactions, for example in CSV format.


Export transactions
-------------------

The python code below exports all incoming and outgoing transactions.

.. code-block:: python

    for t in w.transactions():
        # Export this transaction as list of tuples in the following format:
        #   (in/out, transaction_hash, transaction_date, address, value)
        te = t.export()

        # Loop through all transaction inputs and outputs
        for tei in te:
            # Create string with  list of inputs addresses for incoming transactions, and outputs addresses for outgoing txs
            addr_list = tei[3] if isinstance(tei[3], list) else [tei[3]]

            # Print CSV string to standard output
            print("%s,%s,%s,:%d,%d,%s" % (tei[0], tei[1], tei[2].strftime("%Y-%m-%d %H:%M:%S"), tei[4], cumulative_value,
                                          ";".join(list(set(addr_list)))))

This creates a list of comma separated fields with the transaction info of your wallet.

.. code-block:: python

    in,7722a3c7bd0934522767564943e92a22caaca69e05eec9fbce23fe0a98f044f0,2019-11-19 13:37:10,:1000000,2NDkRVM4VAbrEoJtafq6pkV4hDQBBbsnAgA;2MzRww85sARtDjHJ7QPUL1BdAx8y1Y1d3be
    in,00c76570c0eb91dfd3c644f6321db4de8e0983d2d0528276abeb08aaae9979a8,2019-11-19 13:56:32,:1000000,2NDBrFwt5J9JtvtEJGrbR1x3HMwY7eYQFXM
    in,9fbc417ea3bcd8bd076bbac7a481dc7852c8e168173c70955a97e830cd93fab4,2019-11-19 14:23:35,:10000,
    in,eff479895812039b2f4bcea508989bd3498df1595afc028570323a79f21d8693,2019-11-19 14:23:35,:7700,2NGAfMrvWZBnUx6wu3SMwRArBmMyNV9xXB9
    in,7af39e591a11962cedf6f433f657670d5f0335663788035d9dbe8c0cb7209fb4,2019-11-19 14:23:35,:4000,2N5BVu3mnXieaREwFHVE4RKVBUTT79GFugx
    out,913011f2fab73c230131501570a9f9d2ada5569fe79c9af0268947c9ddf0c2d2,2019-11-19 14:42:09,:41283,mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt
    out,d3a43c327b25b884191ed1aefb39f67463d2d0a61ba0485dfeef1afb26cb8261,2019-11-19 14:42:09,:21645,mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB
    out,cedd18dc60a87fd39a2c8b4ad6b15442b5a53faf5363bca18a36a305294a3f0f,2019-11-19 14:42:09,:36655,n2eMqTT929pb1RDNuqEnxdaLau1rxy3efi
    out,8b7ada2e6acd6619a080b25991f5d9408ee0b42a6a1ecc0eea304c4345a244b4,2019-11-19 14:42:09,:35153,2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE
    out,80333162a87bc8e088eaa54f1f6718c0b7caa72a29a2dfe15a8233110f01612d,2019-11-19 15:25:01,:302642,2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE
    out,449432de51fbe0b5b52a7234b2c860229ca3995888e87dd541a7885211838cc8,2019-11-19 15:25:01,:462332,mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt
    out,9a22ec2e22518678cd6bf4ca88e23c3b7480482be579479ee6db49fbe53f42f7,2019-11-19 15:25:01,:250795,mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB
    out,796f4c1eec2a242508bcb75b1c57920597d376e381289804255d51d9e8c3b336,2019-11-19 15:25:01,:25579,n2eMqTT929pb1RDNuqEnxdaLau1rxy3efi
    out,0335d2d56ac5861f8854c7539a9ffcbedc86c274a1603c605b5690a17968ba2f,2019-11-19 15:25:01,:120464,2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE
    out,d3f512ad2ee829cdb8365adfee8afe73700dd2be8706b5542de302bab448df4f,2019-11-19 16:50:01,:286279,2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE
    out,5714845c10f0cdf4f4767ebb5b00a05fc8428d4c1a35c4f2f11779353193a8f3,2019-11-19 16:51:31,:16375,mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB

You can now easily import this CSV data into a spreadsheet or your administration software.


Export transactions - add cumulative info
-----------------------------------------

Of course you also need totals per year, month, week, etc. Add a cumulative field to the export to keep track of the
wallet totals.

.. code-block:: python

    cumulative_value = 0
    for t in w.transactions():
        # Export this transaction as list of tuples in the following format:
        #   (in/out, transaction_hash, transaction_date, address, value)
        te = t.export()

        # Deduct fee from cumulative value if this is an outgoing transaction
        if te[0][0] == 'out':
            cumulative_value -= t.fee

        # Loop through all transaction inputs and outputs
        for tei in te:
            # Create string with  list of inputs addresses for incoming transactions, and outputs addresses for outgoing txs
            addr_list = tei[3] if isinstance(tei[3], list) else [tei[3]]

            if tei[0] == 'in':
                cumulative_value += tei[4]
            else:
                cumulative_value -= tei[4]

            # Print CSV string to standard output
            print("%s,%s,%s,:%d,%d,%s" % (tei[0], tei[1], tei[2].strftime("%Y-%m-%d %H:%M:%S"), tei[4], cumulative_value,
                                          ";".join(list(set(addr_list)))))

Which results in this CSV output:

.. code-block:: python

    in,7722a3c7bd0934522767564943e92a22caaca69e05eec9fbce23fe0a98f044f0,2019-11-19 13:37:10,:1000000,1000000,2MzRww85sARtDjHJ7QPUL1BdAx8y1Y1d3be;2NDkRVM4VAbrEoJtafq6pkV4hDQBBbsnAgA
    in,00c76570c0eb91dfd3c644f6321db4de8e0983d2d0528276abeb08aaae9979a8,2019-11-19 13:56:32,:1000000,2000000,2NDBrFwt5J9JtvtEJGrbR1x3HMwY7eYQFXM
    in,9fbc417ea3bcd8bd076bbac7a481dc7852c8e168173c70955a97e830cd93fab4,2019-11-19 14:23:35,:10000,2010000,
    in,eff479895812039b2f4bcea508989bd3498df1595afc028570323a79f21d8693,2019-11-19 14:23:35,:7700,2017700,2NGAfMrvWZBnUx6wu3SMwRArBmMyNV9xXB9
    in,7af39e591a11962cedf6f433f657670d5f0335663788035d9dbe8c0cb7209fb4,2019-11-19 14:23:35,:4000,2021700,2N5BVu3mnXieaREwFHVE4RKVBUTT79GFugx
    out,913011f2fab73c230131501570a9f9d2ada5569fe79c9af0268947c9ddf0c2d2,2019-11-19 14:42:09,:41283,1980066,mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt
    out,d3a43c327b25b884191ed1aefb39f67463d2d0a61ba0485dfeef1afb26cb8261,2019-11-19 14:42:09,:21645,1957381,mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB
    out,cedd18dc60a87fd39a2c8b4ad6b15442b5a53faf5363bca18a36a305294a3f0f,2019-11-19 14:42:09,:36655,1919686,n2eMqTT929pb1RDNuqEnxdaLau1rxy3efi
    out,8b7ada2e6acd6619a080b25991f5d9408ee0b42a6a1ecc0eea304c4345a244b4,2019-11-19 14:42:09,:35153,1883508,2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE
    out,80333162a87bc8e088eaa54f1f6718c0b7caa72a29a2dfe15a8233110f01612d,2019-11-19 15:25:01,:302642,1579964,2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE
    out,449432de51fbe0b5b52a7234b2c860229ca3995888e87dd541a7885211838cc8,2019-11-19 15:25:01,:462332,1117281,mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt
    out,9a22ec2e22518678cd6bf4ca88e23c3b7480482be579479ee6db49fbe53f42f7,2019-11-19 15:25:01,:250795,865571,mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB
    out,796f4c1eec2a242508bcb75b1c57920597d376e381289804255d51d9e8c3b336,2019-11-19 15:25:01,:25579,839848,n2eMqTT929pb1RDNuqEnxdaLau1rxy3efi
    out,0335d2d56ac5861f8854c7539a9ffcbedc86c274a1603c605b5690a17968ba2f,2019-11-19 15:25:01,:120464,718482,2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE
    out,d3f512ad2ee829cdb8365adfee8afe73700dd2be8706b5542de302bab448df4f,2019-11-19 16:50:01,:286279,431342,2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE
    out,5714845c10f0cdf4f4767ebb5b00a05fc8428d4c1a35c4f2f11779353193a8f3,2019-11-19 16:51:31,:16375,414823,mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB
