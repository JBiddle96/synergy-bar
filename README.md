# Synergy Bar

A [tqdm](https://github.com/tqdm/tqdm) progress bar that narrates itself in corporate jargon while your code runs.

```
Circling back...: 43%|####3     | 43/100 [00:12<00:16,  3.51it/s]
```

## Install

```
pip install synergy-bar
```

## Usage

`SynergyBar` is a drop-in replacement for `tqdm` — wrap any iterable and it displays a random jargon phrase, updated on a timer rather than per-item:

```python
import time
from synergy_bar import SynergyBar

for item in SynergyBar(range(100)):
    time.sleep(0.1)
```

Extra keyword arguments:

- `interval` (float, default `1.0`) — seconds between message changes.
- `profile` (str, default `"general"`) — which phrase set to use. Built-in profiles: `general`, `defence`, `education`, `finance`, `health`, `retail`, `tourism`.
- `phrases` (list of str) — supply your own phrases instead of a built-in profile.

All other arguments and keyword arguments (`total`, `desc`, `unit`, etc.) are passed straight through to `tqdm`.

```python
from synergy_bar import SynergyBar

for item in SynergyBar(range(100), profile="finance", interval=0.5):
    ...
```

## License

MIT — see [LICENSE](LICENSE).
