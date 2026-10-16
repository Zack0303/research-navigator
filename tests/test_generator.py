import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('generator', ROOT / 'scripts/generate_scholar.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class GeneratorTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'examples/scholar-input.json').read_text())
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.out = Path(self.temp.name) / 'skill'

    def test_reusable_bundle_and_traceability(self):
        module.generate(self.data, self.out)
        self.assertEqual({p.name for p in self.out.iterdir()}, {'SKILL.md', 'research-profile.md', 'methodology.md', 'sources.md'})
        self.assertIn('[S1]', (self.out / 'methodology.md').read_text())
        self.assertIn(self.data['sources'][0]['url'], (self.out / 'sources.md').read_text())
        self.assertIn('Synthetic demonstration', (self.out / 'SKILL.md').read_text())

    def test_reject_unverified_identity_source_and_broken_citation(self):
        variants = []
        for field in ('identity_confirmed',):
            d = copy.deepcopy(self.data); d[field] = False; variants.append(d)
        d = copy.deepcopy(self.data); d['sources'][0]['inspected'] = False; variants.append(d)
        d = copy.deepcopy(self.data); d['approaches'][0]['source_ids'] = ['missing']; variants.append(d)
        d = copy.deepcopy(self.data); d['sources'][0]['evidence'] = ''; variants.append(d)
        d = copy.deepcopy(self.data); d['slug'] = '../../escape'; variants.append(d)
        d = copy.deepcopy(self.data); d['sources'][0]['url'] = 'file:///private/source'; variants.append(d)
        d = copy.deepcopy(self.data); d['sources'][0]['checked'] = '2999-01-01'; variants.append(d)
        for data in variants:
            with self.subTest(data=data), self.assertRaises(ValueError):
                module.generate(data, self.out)
            self.assertFalse(self.out.exists())

    def test_preserve_existing_output(self):
        self.out.mkdir(); marker = self.out / 'student-work'; marker.write_text('keep')
        with self.assertRaises(ValueError):
            module.generate(self.data, self.out)
        self.assertEqual(marker.read_text(), 'keep')

if __name__ == '__main__':
    unittest.main()
