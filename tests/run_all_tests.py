#!/usr/bin/env python3
"""
Test Runner for HRRR v2.2 Complete Test Suite

Runs both legacy and v2.2 test suites with comprehensive reporting.

Usage:
    python tests/run_all_tests.py
    python tests/run_all_tests.py --v22-only  # Run only v2.2 tests
    python tests/run_all_tests.py --legacy-only  # Run only legacy tests
"""
import sys
import argparse
from pathlib import Path

# Add project directory to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def run_legacy_tests():
    """Run legacy MetPy-free refactor tests"""
    print("🔧 Running Legacy Tests (MetPy-free refactor)")
    print("-" * 60)
    
    try:
        import test_metpy_free_refactor
        test_metpy_free_refactor.main()
        return True
    except Exception as e:
        print(f"❌ Legacy tests failed: {e}")
        return False

def run_v22_tests():
    """Run v2.2 comprehensive improvement tests"""
    print("🚀 Running v2.2 Comprehensive Tests")
    print("-" * 60)
    
    try:
        import test_v22_improvements
        return test_v22_improvements.run_comprehensive_tests()
    except Exception as e:
        print(f"❌ v2.2 tests failed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Run HRRR test suites')
    parser.add_argument('--v22-only', action='store_true', 
                       help='Run only v2.2 tests')
    parser.add_argument('--legacy-only', action='store_true',
                       help='Run only legacy tests')
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("HRRR Complete Test Suite Runner")
    print("=" * 80)
    
    results = []
    
    if not args.v22_only:
        print("\n")
        legacy_success = run_legacy_tests()
        results.append(("Legacy Tests", legacy_success))
    
    if not args.legacy_only:
        print("\n")
        v22_success = run_v22_tests()
        results.append(("v2.2 Tests", v22_success))
    
    # Summary
    print("\n" + "=" * 80)
    print("FINAL TEST RESULTS")
    print("=" * 80)
    
    all_passed = True
    for test_name, success in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{test_name:20} {status}")
        if not success:
            all_passed = False
    
    print("-" * 80)
    if all_passed:
        print("🎉 ALL TEST SUITES PASSED!")
        print("✨ HRRR v2.2 is ready for production use")
    else:
        print("⚠️  SOME TESTS FAILED")
        print("🔧 Please review failures before deployment")
    
    print("=" * 80)
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)