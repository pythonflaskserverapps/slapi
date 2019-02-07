# Shadow lichess API

Lichess API like functions that are not part of the official API.

## Login

```python
import slapi

lila2 = slapi.login("username", "password")
```

## Join tourney

```python
import slapi

slapi.jointourney("tourneyid", slapi.login("username", "password"))
```

## Talk tourney chat

```python
import slapi

slapi.talktourneychat("tourneyid", slapi.login("username", "password"), "message")
```
