# perfectpower

累乗数の配列を生成するPythonコードと、これで実際に出力した累乗数のJSONデータになる予定です。


## perfectpower/lists/*.json

4以上＊＊＊以下の累乗数を10万余ずつ収録した＊個のJSONファイルです。各ファイル**n.json**には、n\*100000から順に約10万個の累乗数が収録されていて、次のようなデータ構造をしています。

    [
      {"a": 576, "gen": [{"b": 24, "e": 2}]},
      {"a": 625, "gen": [{"b": 5, "e": 4}, {"b": 25, "e": 2}]},
      {"a": 676, "gen": [{"b": 26, "e": 2}]},
      {"a": 729, "gen": [{"b": 3, "e": 6}, {"b": 9, "e": 3}, {"b": 27, "e": 2}]},
    ]

累乗数`"a"`を生成する1個以上の累乗表現オブジェクトが配列`"gen"`に収められています。累乗表現は複数あり得ます。上記の例なら、次のような累乗数と累乗表現を意味します。

- 576 = 24^2
- 625 = 5^4 = 25^2
- 676 = 26^2
- 729 = 3^6 = 9^3 = 27^2

なお、`"b"`は base（底）、`"e"`は exponent（指数）の頭文字です。


###　各ファイルの長さ

**files.json**に記載されている内容は、`"file"`（ファイルの名前）、`"begin"`（先頭の累乗数）、`"end"`（末尾の累乗数）、`"len"`（配列の長さ）、`"offset"`（先頭が何番目の累乗数か）を収めたオブジェクトを、累乗数が小さい順に収めた配列です。

    [
      {"file": "0.json", "begin": 4, "end": 9603804001, "len": 100200, "offset": 0},
      {"file": "96040.json", "begin": 9604000000, "end": 38808606001, "len": 100282, "offset": 100200},
    ]

`"offset"`は要するにそれ以下のファイルの`"len"`の合計値で、先頭の4(=2^2)を0番目としています。
