
"""
SHACL Validation Script for mobilityDCAT-AP
"""
from pathlib import Path
from pyshacl import validate
from rdflib import Graph
import sys

class SHACLValidator:
    def __init__(self, shacl_dir: Path, examples_dir: Path):
        self.shacl_dir = shacl_dir
        self.examples_dir = examples_dir
        
    def load_shapes(self, include_ranges=True):
        """Load SHACL shapes (basic + optionally ranges)"""
        shapes = Graph()
        
        # Load basic shapes
        basic_file = self.shacl_dir / "mobilitydcat-ap-shacl.ttl"
        print(f"📂 Loading basic shapes: {basic_file}")
        shapes.parse(basic_file, format="turtle")
        
        # Load ranges if requested
        if include_ranges:
            ranges_file = self.shacl_dir / "mobilitydcat-ap-shacl-ranges.ttl"
            if ranges_file.exists():
                print(f"📂 Loading ranges: {ranges_file}")
                shapes.parse(ranges_file, format="turtle")
            else:
                print(f"⚠️  Ranges file not found: {ranges_file}")
        
        print(f"✅ Loaded {len(shapes)} triples in shapes graph\n")
        return shapes
    
    def load_data(self, data_file: Path):
        """Load data graph to validate"""
        data = Graph()
        print(f"📂 Loading data: {data_file}")
        data.parse(data_file, format="turtle")
        print(f"✅ Loaded {len(data)} triples in data graph\n")
        return data
    
    def validate(self, data_file: Path, include_ranges=True):
        """Validate data against shapes"""
        print("=" * 70)
        print(f"VALIDATING: {data_file.name}")
        print("=" * 70 + "\n")
        
        shapes = self.load_shapes(include_ranges)
        data = self.load_data(data_file)
        
        print("🔍 Running validation...\n")
        
        conforms, results_graph, results_text = validate(
            data,
            shacl_graph=shapes,
            inference='rdfs',
            abort_on_first=False,
        )
        
        print("=" * 70)
        print(f"RESULT: {'✅ VALID' if conforms else '❌ INVALID'}")
        print("=" * 70 + "\n")
        
        if not conforms:
            print("VALIDATION REPORT:")
            print("-" * 70)
            print(results_text)
        
        return conforms, results_text
    
    def validate_all(self, include_ranges=True):
        """Validate all example files"""
        if not self.examples_dir.exists():
            print(f"❌ Examples directory not found: {self.examples_dir}")
            return
        
        example_files = list(self.examples_dir.glob("*.ttl"))
        
        if not example_files:
            print(f"⚠️  No .ttl files found in {self.examples_dir}")
            return
        
        print(f"\n🎯 Found {len(example_files)} example files\n")
        
        results = {}
        for example in example_files:
            conforms, report = self.validate(example, include_ranges)
            results[example.name] = conforms
            print("\n")
        
        # Summary
        print("=" * 70)
        print("SUMMARY")
        print("=" * 70)
        for filename, conforms in results.items():
            status = "✅ VALID" if conforms else "❌ INVALID"
            print(f"{status:12} {filename}")
        
        total = len(results)
        valid = sum(results.values())
        print(f"\nTotal: {valid}/{total} valid")
        
        return results


def main():
    # Paths relative to project root
    project_root = Path(__file__).parent.parent.parent.parent
    shacl_dir = project_root / "shacl"
    examples_dir = project_root.parent / "examples"
    
    print(f"Project root: {project_root}")
    print(f"SHACL dir: {shacl_dir}")
    print(f"Examples dir: {examples_dir}\n")
    
    validator = SHACLValidator(shacl_dir, examples_dir)
    
    # Check if specific file provided
    if len(sys.argv) > 1:
        data_file = Path(sys.argv[1])
        validator.validate(data_file, include_ranges=True)
    else:
        # Validate all examples
        validator.validate_all(include_ranges=True)


if __name__ == "__main__":
    main()
