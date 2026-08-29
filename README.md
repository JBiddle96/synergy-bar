# SynergyBar

Is your Python code lacking corporate alignment?

Do you feel your pursuit of stakeholder value waning? 

Does management understand how committed your code is to client outcomes?

If you answered yes to these questions, `SynergyBar` is here to reorient you back to your north star!
Simply wrap your loops in `SynergyBar` and watch as your code instantly becomes more outcome-focussed, collaboration-minded, and priority-aligned.

## Install

```
pip install synergy-bar
```

## Usage

`SynergyBar` is a drop-in replacement for `tqdm` — wrap any iterable and it displays a random message updated on a timer:

```python
import time
from synergy_bar import SynergyBar

for item in SynergyBar(range(100)):
    time.sleep(0.1)
```

Extra keyword arguments:

- `interval` (float, default `1.0`) — seconds between message changes.
- `profile` (str, default `"general"`) — which phrase set to use. Current businesses include: `general`, `defence`, `education`, `finance`, `health`, `retail`, `tourism`.
- `phrases` (list of str) — supply your own dynamic phrases to add that personal touch.

All other arguments and keyword arguments are passed straight through to `tqdm`.

```python
from synergy_bar import SynergyBar

for item in SynergyBar(range(100), profile="finance", interval=0.5):
    ...
```

## License

MIT — see [LICENSE](LICENSE).

## Contributing

This is obviously just a bit of fun, but please feel free to add additional phrases/profiles. You never know who might urgently need to demonstrate their corporate allegiance.