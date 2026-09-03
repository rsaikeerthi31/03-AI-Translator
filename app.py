from langchain_ollama import ChatOllama
from prompts import TRANSLATION_PROMPT

# Load Local LLM
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

# Supported Languages
languages = {
    "1": "English",
    "2": "Telugu",
    "3": "Hindi",
    "4": "Tamil",
    "5": "French",
    "6": "German"
}


def display_languages():
    print("\nAvailable Languages:\n")
    for key, value in languages.items():
        print(f"{key}. {value}")


while True:

    print("\n" + "=" * 55)
    print("🌍 AI Translator")
    print("=" * 55)

    display_languages()

    source = input("\nChoose Source Language (1-6): ").strip()
    target = input("Choose Target Language (1-6): ").strip()

    # Validate language selection
    if source not in languages or target not in languages:
        print("\n❌ Invalid language selection. Please try again.")
        continue

    if source == target:
        print("\n❌ Source and Target languages cannot be the same.")
        continue

    text = input("\nEnter text to translate:\n").strip()

    if not text:
        print("\n❌ Text cannot be empty.")
        continue

    prompt = TRANSLATION_PROMPT.format(
        source_language=languages[source],
        target_language=languages[target],
        text=text
    )

    try:
        response = llm.invoke(prompt)

        print("\n" + "-" * 55)
        print("🌐 Translation Result")
        print("-" * 55)
        print(f"Source Language : {languages[source]}")
        print(f"Target Language : {languages[target]}")
        print("-" * 55)
        print(response.content.strip())
        print("-" * 55)

    except Exception as e:
        print("\n❌ Error:", e)

    again = input("\nTranslate another text? (y/n): ").strip().lower()

    if again != "y":
        print("\n👋 Thank you for using AI Translator!")
        break