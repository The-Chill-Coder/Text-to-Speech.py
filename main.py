import asyncio
import edge_tts


async def main():
    tts = edge_tts.Communicate("""
For thousands of years, humanity has feared what lurks beneath the ocean's surface. And perhaps few creatures embody that fear more than the sperm whale.
A living leviathan capable of descending into eternal darkness... battling monsters in the abyss... and vanishing into depths humanity still barely understands.
Even now, somewhere far below the waves, a sperm whale is slipping through black water beyond the reach of sunlight, entering a realm where pressure crushes steel and mysteries still endure.
And perhaps that is what makes the ocean so terrifying.
Not the creatures we have discovered...
But the countless secrets we have not.
Until next time...
Stay curious.

    """,
                               voice = "en-GB-RyanNeural",
                                rate = "-20%",
                                pitch = "-10Hz"
                                )
    await tts.save("script.mp3")

asyncio.run(main())
