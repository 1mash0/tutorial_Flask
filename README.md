## 仮想環境を(venv)を有効化
```bash
$ . .venv/bin/activate
```

## 仮想環境(venv)を無効化
```bash
$ deactivate
```

## デバッグモードで起動
`app.py`がある場合は以下
```bash
$ flask run --debug
```
`app.py`がない場合、もしくはファイルを指定して起動する場合は以下
```bash
$ flask --app hello run --debug
```