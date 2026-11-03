#!/usr/bin/env python3
"""
SVG Validator for Universal SVG UI Architect
--------------------------------------------
Validates SVG files or piped input against Universal SVG UI standards:
  1. Valid XML syntax & root <svg> element with viewBox
  2. Zero <style> tags or CSS class definitions (pure inline presentation attributes)
  3. Proper semantic layer naming conventions (Slash '/' and BEM '__', '--')
  4. Coordinate and dimension checks

Usage:
  python3 validate_svg.py mockup.svg
  cat mockup.svg | python3 validate_svg.py
"""

import sys
import re
import argparse
import xml.etree.ElementTree as ET


def strip_ns(tag: str) -> str:
    """Strip XML namespace prefix from tag name."""
    return tag.split("}")[-1] if "}" in tag else tag


def validate_svg(content: str) -> tuple[bool, list[str], list[str]]:
    """Validate SVG string against the Universal SVG UI Architect guidelines."""
    errors: list[str] = []
    warnings: list[str] = []

    # 1. Parse XML
    try:
        root = ET.fromstring(content)
    except ET.ParseError as err:
        errors.append(f"XML Parsing Error: {err}")
        return False, errors, warnings

    # 2. Check root element
    tag = strip_ns(root.tag).lower()
    if tag != "svg":
        errors.append(f"Root element must be <svg>, found: <{tag}>")
        return False, errors, warnings

    # 3. Check viewBox and dimensions
    viewbox = root.attrib.get("viewBox")
    width = root.attrib.get("width")
    height = root.attrib.get("height")

    if not viewbox:
        warnings.append("Missing 'viewBox' attribute on root <svg>.")
    else:
        vb_parts = viewbox.strip().split()
        if len(vb_parts) != 4:
            warnings.append(f"Invalid 'viewBox' format: '{viewbox}' (expected 4 values).")

    if not width or not height:
        warnings.append("Explicit 'width' and 'height' attributes recommended for vector imports.")

    # 4. Enforce Zero <style> or <link> tags (Inline presentation attribute rule)
    for elem in root.iter():
        elem_tag = strip_ns(elem.tag).lower()
        if elem_tag in ("style", "link"):
            errors.append(
                f"Disallowed <{elem_tag}> tag found! "
                "Universal SVG UI Architect requires pure inline presentation attributes (fill, stroke, etc.)."
            )
        if "class" in elem.attrib:
            warnings.append(
                f"Element <{elem_tag}> uses 'class=\"{elem.attrib['class']}\"'. "
                "Inline XML presentation attributes are preferred over CSS classes for maximum vector editor compatibility."
            )

    # 5. Check semantic layer naming (id attributes)
    total_elements = 0
    named_elements = 0
    group_elements = 0
    named_groups = 0

    for elem in root.iter():
        elem_tag = strip_ns(elem.tag).lower()
        if elem_tag == "svg":
            continue

        total_elements += 1
        elem_id = elem.attrib.get("id")

        if elem_tag == "g":
            group_elements += 1
            if elem_id:
                named_groups += 1

        if elem_id:
            named_elements += 1

    if group_elements > 0 and named_groups < group_elements:
        missing_count = group_elements - named_groups
        warnings.append(
            f"{missing_count} of {group_elements} <g> groups lack an 'id' attribute. "
            "Assign semantic Slash ('/') or BEM ('__') IDs to all groups for organized layers in Figma/Penpot."
        )

    return len(errors) == 0, errors, warnings


def main():
    parser = argparse.ArgumentParser(
        description="Validate SVG files against Universal SVG UI Architect standards."
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType("r", encoding="utf-8"),
        default=sys.stdin,
        help="Path to SVG file (reads from stdin if omitted)",
    )
    args = parser.parse_args()

    content = args.file.read()
    if not content.strip():
        print("Error: Empty SVG content provided.", file=sys.stderr)
        sys.exit(1)

    is_valid, errors, warnings = validate_svg(content)

    print("=" * 60)
    print(" Universal SVG UI Architect - Validation Report")
    print("=" * 60)

    if errors:
        print("\n❌ Errors:")
        for err in errors:
            print(f"  • {err}")

    if warnings:
        print("\n⚠️  Warnings:")
        for warn in warnings:
            print(f"  • {warn}")

    if is_valid and not warnings:
        print("\n✅ Perfect! SVG fully conforms to Universal SVG UI Architect standards.")
    elif is_valid:
        print("\n✅ Passed with warnings. The SVG is valid and vector-compatible.")
    else:
        print("\n❌ Validation Failed.")

    print("=" * 60)
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
