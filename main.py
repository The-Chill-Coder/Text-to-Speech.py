import asyncio
import edge_tts


async def main():
    tts = edge_tts.Communicate("""
    Enter Text here for audio

    """,
                               voice = "en-GB-RyanNeural",
                                #rate = "-20%",
                                #pitch = "-10Hz"
                                )
    await tts.save("audio.mp3")

asyncio.run(main())
