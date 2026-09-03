TRANSLATION_PROMPT = """
You are a professional translator.

Translate the following text from {source_language} to {target_language}.

Source Language:
{source_language}

Target Language:
{target_language}

Text:
{text}

Instructions:
- Translate accurately.
- Preserve the meaning.
- Do not explain the translation.
- Do not add extra words.
- Return ONLY the translated text.
"""