"""
SHACL Import Consistency Checker
Tests that imports in mobilityDCAT-AP SHACL files are correct and accessible
"""
from pathlib import Path
from rdflib import Graph, OWL, Namespace
from prettytable import PrettyTable
import sys

class ImportInspector:
    def __init__(self):
        self.visited = set()
        self.errors = []
        
    def check_file(self, url_or_path, depth=0):
        """Check a single file's imports"""
        indent = "  " * depth
        
        # Convert to string
        location = str(url_or_path)
        
        # Skip if already visited
        if location in self.visited:
            print(f"{indent}↩️  Already visited: {location}")
            return
        
        self.visited.add(location)
        
        print(f"{indent}📂 Checking: {location}")
        
        # Load graph
        g = Graph()
        try:
            if location.startswith("http"):
                g.parse(location, format="turtle")
            else:
                g.parse(location, format="turtle")
            print(f"{indent}   ✅ Loaded ({len(g)} triples)")
        except Exception as e:
            error = f"Failed to load {location}: {e}"
            self.errors.append(error)
            print(f"{indent}   ❌ {error}")
            return
        
        # Get imports
        imports = list(g.objects(predicate=OWL.imports))
        
        if imports:
            print(f"{indent}   📦 {len(imports)} imports found:")
            for imp in imports:
                print(f"{indent}      → {imp}")
                # Recursively check
                self.check_file(str(imp), depth + 1)
        else:
            print(f"{indent}   ℹ️  No imports")
    
    def check_consistency(self, basic_file, ranges_file):
        """Check consistency between basic and ranges files"""
        print("\n" + "=" * 80)
        print("IMPORT CONSISTENCY CHECK")
        print("=" * 80 + "\n")
        
        # Check basic file
        print("🔍 Checking BASIC file...")
        print("-" * 80)
        self.check_file(basic_file)
        
        print("\n" + "-" * 80)
        
        # Reset visited for ranges
        basic_visited = self.visited.copy()
        self.visited.clear()
        
        # Check ranges file
        print("\n🔍 Checking RANGES file...")
        print("-" * 80)
        self.check_file(ranges_file)
        
        ranges_visited = self.visited.copy()
        
        # Compare
        print("\n" + "=" * 80)
        print("COMPARISON")
        print("=" * 80 + "\n")
        
        # Common imports
        common = basic_visited & ranges_visited
        if common:
            print(f"✅ {len(common)} common imports:")
            for imp in sorted(common):
                print(f"   - {imp}")
        
        # Only in basic
        only_basic = basic_visited - ranges_visited
        if only_basic:
            print(f"\n📘 {len(only_basic)} only in BASIC:")
            for imp in sorted(only_basic):
                print(f"   - {imp}")
        
        # Only in ranges
        only_ranges = ranges_visited - basic_visited
        if only_ranges:
            print(f"\n📗 {len(only_ranges)} only in RANGES:")
            for imp in sorted(only_ranges):
                print(f"   - {imp}")
        
        # Report errors
        if self.errors:
            print("\n" + "=" * 80)
            print("❌ ERRORS FOUND")
            print("=" * 80)
            for error in self.errors:
                print(f"  • {error}")
            return False
        else:
            print("\n" + "=" * 80)
            print("✅ ALL IMPORTS ACCESSIBLE")
            print("=" * 80)
            return True
    
    def compare_with_expected(self, basic_file, ranges_file):
        """Compare actual imports with expected DCAT-AP pattern"""
        print("\n" + "=" * 80)
        print("EXPECTED vs ACTUAL IMPORTS")
        print("=" * 80 + "\n")
        
        # Expected imports
        expected = {
            "basic": {
                "https://semiceu.github.io/DCAT-AP/releases/3.0.1/shacl/dcat-ap-SHACL.ttl",
                "https://w3id.org/mobilitydcat-ap/releases/1.1.0/mobilitydcat-ap_v1.1.0.ttl",
            },
            "ranges": {
                "https://semiceu.github.io/DCAT-AP/releases/3.0.1/shacl/ranges.ttl",
            }
        }
        
        # Load actual imports
        actual = {}
        for name, file in [("basic", basic_file), ("ranges", ranges_file)]:
            g = Graph()
            try:
                g.parse(file, format="turtle")
                actual[name] = set(str(imp) for imp in g.objects(predicate=OWL.imports))
            except Exception as e:
                print(f"❌ Failed to load {name}: {e}")
                return False
        
        # Create comparison table
        table = PrettyTable()
        table.field_names = ["File", "Expected", "Actual", "Status"]
        table.align = "l"
        
        all_correct = True
        
        for name in ["basic", "ranges"]:
            exp = expected[name]
            act = actual[name]
            
            # Check each expected import
            for imp in exp:
                if imp in act:
                    status = "✅ OK"
                else:
                    status = "❌ MISSING"
                    all_correct = False
                table.add_row([name.upper(), imp, "Present" if imp in act else "Missing", status])
            
            # Check for unexpected imports
            unexpected = act - exp
            for imp in unexpected:
                table.add_row([name.upper(), "-", imp, "⚠️  EXTRA"])
        
        print(table)
        
        return all_correct


def main():
    # Paths
    shacl_dir = Path(__file__).parent.parent
    basic_file = shacl_dir / "mobilitydcat-ap-shacl.ttl"
    ranges_file = shacl_dir / "mobilitydcat-ap-shacl-ranges.ttl"
    
    print("📁 SHACL Directory:", shacl_dir)
    print("📄 Basic file:", basic_file)
    print("📄 Ranges file:", ranges_file)
    print()
    
    # Check files exist
    if not basic_file.exists():
        print(f"❌ Basic file not found: {basic_file}")
        sys.exit(1)
    
    if not ranges_file.exists():
        print(f"❌ Ranges file not found: {ranges_file}")
        sys.exit(1)
    
    # Run checks
    inspector = ImportInspector()
    
    # Check consistency
    success = inspector.check_consistency(basic_file, ranges_file)
    
    # Compare with expected
    expected_ok = inspector.compare_with_expected(basic_file, ranges_file)
    
    # Final result
    print("\n" + "=" * 80)
    if success and expected_ok:
        print("✅ ALL CHECKS PASSED")
        sys.exit(0)
    else:
        print("❌ SOME CHECKS FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()