from __future__ import annotations

import argparse
import sys

from tony_x.core.self_test import run_self_test


def main() -> int:
    parser = argparse.ArgumentParser(description="TONY-X command line")
    parser.add_argument("--self-test", action="store_true", help="Run the built-in TONY-X self-test")
    args = parser.parse_args()

    if args.self_test:
        results = run_self_test()
        print("TONY-X SELF TEST")
        print("=" * 40)
        for key, value in results.items():
            print(f"{key}: {value['status']} - {value['details']}")
        return 0 if all(item["status"] == "PASS" for item in results.values()) else 1

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
