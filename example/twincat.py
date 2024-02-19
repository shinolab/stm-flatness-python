import asyncio

from samples import runner  # type: ignore[import,import-not-found]

from pyautd3 import AUTD3, Controller
from pyautd3.link.twincat import TwinCAT


async def main() -> None:
    with await Controller.builder().add_device(AUTD3([0.0, 0.0, 0.0])).open_async(TwinCAT.builder()) as autd:
        await runner.run(autd)


if __name__ == "__main__":
    asyncio.run(main())
