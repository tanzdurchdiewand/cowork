import base64
import tempfile
import os

import assemblyai as aai

from python.helpers import settings
from python.helpers.print_style import PrintStyle


def _get_api_key() -> str:
    """Get AssemblyAI API key from settings."""
    s = settings.get_settings()
    key = s["api_keys"].get("assemblyai", "")
    if not key:
        key = os.environ.get("API_KEY_ASSEMBLYAI", "")
    return key


async def transcribe(audio_bytes_b64: str, language: str = "") -> dict:
    """
    Transcribe audio using AssemblyAI REST API.

    Args:
        audio_bytes_b64: Base64-encoded WAV audio data
        language: Language code (e.g. 'en', 'de'). Empty for auto-detect.

    Returns:
        dict with 'text' key containing the transcription
    """
    api_key = _get_api_key()
    if not api_key:
        raise ValueError(
            "AssemblyAI API key not configured. "
            "Set it in Settings > API Keys."
        )

    aai.settings.api_key = api_key

    # Decode base64 audio to temp file
    audio_bytes = base64.b64decode(audio_bytes_b64)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(audio_bytes)
        temp_path = f.name

    try:
        config = aai.TranscriptionConfig(
            language_code=language if language else None,
        )

        transcriber = aai.Transcriber(config=config)
        transcript = transcriber.transcribe(temp_path)

        if transcript.status == aai.TranscriptStatus.error:
            raise RuntimeError(f"AssemblyAI error: {transcript.error}")

        return {"text": transcript.text or ""}
    finally:
        try:
            os.remove(temp_path)
        except Exception:
            pass
