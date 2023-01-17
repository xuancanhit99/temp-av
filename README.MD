```bash
$ docker-compose up -d --build
```

```bash
$ docker-compose run --rm consumer sh
$ python consumer.py
```

```bash
 $ curl http://localhost:8000/add-job/hey
 {"send":"hey"}
```

```bash
 [x] Received b'hey'
hey there
 [x] Done
```

```bash
 $ curl http://localhost:8000/add-job/hello
 {"send":"hello"}
```

```bash
 [x] Received b'hello'
well hello there
 [x] Done
```
