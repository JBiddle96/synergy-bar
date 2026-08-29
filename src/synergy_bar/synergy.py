import random
import threading
from importlib import resources
from typing import Any

from tqdm import tqdm


def _available_profiles() -> list[str]:
    return sorted(
        p.name.removesuffix(".txt")
        for p in resources.files("synergy_bar.assets").iterdir()
        if p.name.endswith(".txt")
    )


def _load_phrases(profile: str = "general") -> list[str]:
    filename = f"{profile}.txt"
    try:
        text = (
            resources.files("synergy_bar.assets")
            .joinpath(filename)
            .read_text(encoding="utf-8")
        )
    except FileNotFoundError:
        available = ", ".join(_available_profiles())
        raise ValueError(
            f"Unknown profile {profile!r}. Available profiles: {available}"
        ) from None
    return [line.strip() for line in text.splitlines() if line.strip()]


class SynergyBar(tqdm):
    """A tqdm progress bar that makes your code 100% more aligned to stakeholder values."""

    DEFAULT_BAR_FORMAT = "{desc:<46} |{bar:20}| {percentage:3.0f}%"

    def __init__(
        self,
        *args: Any,
        phrases: list[str] | None = None,
        profile: str = "general",
        interval: float = 1.0,
        **kwargs: Any,
    ) -> None:
        self._phrases: list[str] = phrases or _load_phrases(profile)
        kwargs.setdefault("bar_format", self.DEFAULT_BAR_FORMAT)
        super().__init__(*args, **kwargs)
        self._stop_event: threading.Event = threading.Event()
        self._thread: threading.Thread = threading.Thread(
            target=self._narrate, args=(interval,), daemon=True
        )
        self._thread.start()

    def _narrate(self, interval: float) -> None:
        while not self._stop_event.is_set():
            self.set_description_str(random.choice(self._phrases))
            self._stop_event.wait(interval)

    def close(self) -> None:
        stop_event: threading.Event | None = getattr(self, "_stop_event", None)
        if stop_event is not None:
            stop_event.set()
        super().close()
