"""Expose fenced-code language names for a CSS-only code header."""

from __future__ import annotations

import html
import re

from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
from markdown.preprocessors import Preprocessor

OPENING_FENCE = re.compile(
    r"^(?P<fence>`{3,}|~{3,})[ \t]*(?:\{[ \t]*)?\.?(?P<language>[\w#+.-]+)"
)
HIGHLIGHT_DIV = re.compile(r'<div class="highlight">')

LANGUAGE_NAMES = {
    "bash": "Bash",
    "css": "CSS",
    "html": "HTML",
    "javascript": "JavaScript",
    "js": "JavaScript",
    "json": "JSON",
    "markdown": "Markdown",
    "md": "Markdown",
    "python": "Python",
    "py": "Python",
    "shell": "Shell",
    "sh": "Shell",
    "toml": "TOML",
    "typescript": "TypeScript",
    "ts": "TypeScript",
    "yaml": "YAML",
    "yml": "YAML",
}


class FenceLanguagePreprocessor(Preprocessor):
    """Remember language identifiers before fenced_code consumes them."""

    def __init__(self, md, extension: "CodeLanguageExtension"):
        super().__init__(md)
        self.extension = extension

    def run(self, lines: list[str]) -> list[str]:
        self.extension.languages.clear()
        closing_fence: str | None = None

        for line in lines:
            stripped = line.lstrip()
            if closing_fence is not None:
                if stripped.startswith(closing_fence):
                    closing_fence = None
                continue

            match = OPENING_FENCE.match(stripped)
            if match:
                fence = match.group("fence")
                closing_fence = fence[0] * len(fence)
                language = match.group("language")
                label = LANGUAGE_NAMES.get(language.lower(), language)
                self.extension.languages.append(label)

        return lines


class CodeLanguagePostprocessor(Postprocessor):
    """Attach the remembered label to each highlighted block."""

    def __init__(self, md, extension: "CodeLanguageExtension"):
        super().__init__(md)
        self.extension = extension

    def run(self, text: str) -> str:
        labels = iter(self.extension.languages)

        def add_label(match: re.Match[str]) -> str:
            label = next(labels, "Code")
            return f'<div class="highlight" data-language="{html.escape(label, quote=True)}">'

        return HIGHLIGHT_DIV.sub(add_label, text)


class CodeLanguageExtension(Extension):
    def __init__(self, **kwargs):
        self.languages: list[str] = []
        super().__init__(**kwargs)

    def extendMarkdown(self, md):  # noqa: N802 - Python-Markdown API
        md.registerExtension(self)
        md.preprocessors.register(
            FenceLanguagePreprocessor(md, self), "fence_language", 27
        )
        md.postprocessors.register(
            CodeLanguagePostprocessor(md, self), "code_language", 1
        )

    def reset(self):
        self.languages.clear()


def makeExtension(**kwargs):  # noqa: N802 - Python-Markdown API
    return CodeLanguageExtension(**kwargs)

