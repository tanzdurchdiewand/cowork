from python.helpers.api import ApiHandler, Request, Response
from python.helpers import settings, assemblyai_stt


class Transcribe(ApiHandler):
    async def process(self, input: dict, request: Request) -> dict | Response:
        audio = input.get("audio")
        ctxid = input.get("ctxid", "")

        if ctxid:
            context = self.use_context(ctxid)

        s = settings.get_settings()
        result = await assemblyai_stt.transcribe(
            audio_bytes_b64=audio,
            language=s.get("stt_language", ""),
        )
        return result
