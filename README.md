# MTL

[MT-DNN](https://aclanthology.org/P19-1441/)を使用したマルチタスク学習のコードです。

## data_mctaco

MC-TACOのデータセット。

mctaco_train_yn.tsv, mctaco_test_yn.tsvが元のデータセット。

mctaco_train.tsv, mctaco_test.tsvはラベルのno, yesを0,1に変換したもの（こちらを使用）。

## evaluator

MC-TACOでの精度（Exact MatchとF1スコア）を求めるためのコード。

（MC-TACOはExact Matchという独自の評価指標を採用しているため自分で求める必要がある。）

## experiments

元のデータセットをMT-DNNのフォーマットに変形するためのymlファイルなど。

## predictions_json_to_txt.py

マルチタスク学習後に出力された予測ファイル（json）をtxtファイルに変形するコード。

MC-TACOで性能評価する際に使用。

## prepro_std.py

元のデータセットをMT-DNNのフォーマットに変形するコード。

## train.py

マルチタスク学習をするコード。

## 主なコマンド

元のデータセットをMT-DNNのフォーマットに変形するときの例：

`python prepro_std.py --model albert-xxlarge-v2 --root data_mctaco --task_def experiments/mctaco_task_def.yml`

`python prepro_std.py --model albert-xxlarge-v2 --root data_ranking --task_def experiments/cosmosqa_task_def.yml`

例えば上のコマンド実行すると、data_mctacoの下にalbert-xxlarge-v2というフォルダができる。

＊複数のデータをマルチタスク学習させる場合は。上記フォルダにデータをまとめる必要がある。
（mv data_cosmosqa/albert-xxlarge-v2/* data_mctaco/albert-xxlarge-v2/）

マルチタスク学習させるときの例：

`python train.py --data_dir data_mctaco/albert-xxlarge-v2 --task_def experiments/mctaco_task_def.yml --train_dataset mctaco,timebank,cosmosqa --test_dataset mctaco,timebank --init_checkpoint albert-xxlarge-v2 --batch_size 16 --optimizer adam --learning_rate 1e-5  --encoder_type 10 --epochs 30 --multi_gpu_on`

MC-TACOで性能評価するとき：

`python predictions_json_to_txt.py `

`python evaluator/evaluator.py eval --test_file dataset/test_9442.tsv --prediction_file yn_output/al_mc-co15000/yn_epoch_19.txt`

