フォルダー構成の説明
実行ホスト：trial-es-future-01 & buzz-indexer-01
１：getTableRows.pyはbigqueryから指定したテーブルにあるレコード数を取得するスクリプト
２：bigquery-table-copy.pyはhtl-datastore-prodからhtl-backupへのコピー
３：blog-dss-stb1フォルダーはオンプレからbigqueryへデーター移行用一式
	auth_prod.json：認証 jsonファイル
	blog.json：bigqueryのキスーマファイル
	bigqueryTmp.yml：embulk用の設定ファイル
	bigqueryTmp.py：実行スクリプト
４：check-old-dataはオンプレから指定したテーブルにあるレコード数を取得するスクリプト

