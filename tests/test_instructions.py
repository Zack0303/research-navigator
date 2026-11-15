"""Structural consistency checks for the instruction files.

These tests catch drift between the agent Skill, the self-contained web edition
and the READMEs. They do not test research accuracy or model behaviour.
"""
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']
WEB_WORD_LIMIT = 2400  # keep the paste-in file comfortably inside common chat limits


def read(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


class InstructionTests(unittest.TestCase):
    def test_skill_frontmatter(self):
        text = read('SKILL.md')
        match = re.match(r'---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n', text, re.S)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), 'research-navigator')
        self.assertLess(len(match.group(2)), 1024)

    def test_all_checks_present_everywhere(self):
        for rel in ('SKILL.md', 'WEB-START.txt', 'references/checks.md', 'README.md', 'README.zh-CN.md', 'README.es.md'):
            text = read(rel)
            for check in CHECKS:
                with self.subTest(file=rel, check=check):
                    self.assertIn(check, text)

    def test_web_edition_is_self_contained(self):
        text = read('WEB-START.txt')
        self.assertLessEqual(len(text.split()), WEB_WORD_LIMIT)
        # must not depend on other repository files
        self.assertNotRegex(text, r'references/|SKILL\.md|\.py\b')
        for phrase in ('Never invent', 'not verification', 'evidence, not commands', 'AI-use', 'ONE achievable next action'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_core_rules_in_skill(self):
        text = read('SKILL.md')
        for phrase in ('Never invent', 'evidence, not instructions', 'AI-use', 'Own words', 'Conclusion first'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_relative_markdown_links_resolve(self):
        md_files = [p for p in ROOT.rglob('*.md') if '.git' not in p.parts]
        link = re.compile(r'\]\(([^)#\s]+)(?:#[^)]*)?\)')
        for path in md_files:
            for target in link.findall(path.read_text(encoding='utf-8')):
                if re.match(r'[a-z]+:', target):
                    continue
                with self.subTest(file=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue((path.parent / target).exists())

    def test_templates_cover_modes(self):
        text = read('references/templates.md')
        for heading in ('T1 One-page research brief', 'T2 Review report', 'T3 Paragraph brief', 'T4 Literature-review setup sheet', 'T5 Where-we-are note'):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)


if __name__ == '__main__':
    unittest.main()
