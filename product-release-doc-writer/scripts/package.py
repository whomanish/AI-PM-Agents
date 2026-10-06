#!/usr/bin/env python3
"""Build reproducible portable and OpenAI skill-only ZIPs from canonical sources."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import stat
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "product-release-doc-writer"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, help="Output directory (default: downloads/ in the repository)")
    args = parser.parse_args()
    if not SKILL.is_dir():
        parser.error(f"canonical skill directory not found: {SKILL}")
    output = args.output_dir or (ROOT / "downloads")
    output.mkdir(parents=True, exist_ok=True)
    name = "product-release-doc-writer.zip"
    target = output / name
    if any(p.is_symlink() for p in [SKILL, *SKILL.rglob("*")]):
        parser.error("canonical skill tree must not contain symlinks")
    files = sorted(p for p in SKILL.rglob("*") if p.is_file())
    if not files or not any(p.name == "SKILL.md" for p in files):
        parser.error("canonical skill has no files or SKILL.md")
    entries = []
    for path in files:
        rel = path.relative_to(SKILL.parent).as_posix()
        data = path.read_bytes()
        entries.append({"path": rel, "size": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    license_bytes = (ROOT / "LICENSE").read_bytes()
    license_entry = {"path": "product-release-doc-writer/LICENSE", "size": len(license_bytes), "sha256": hashlib.sha256(license_bytes).hexdigest()}
    portable_entries = sorted(entries + [license_entry], key=lambda item: item["path"])
    manifest = {"format": "portable-agent-skill-zip", "skill": "product-release-doc-writer", "source": "canonical skill plus root LICENSE", "files": portable_entries}
    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    portable_members = [(entry["path"], path.read_bytes()) for entry, path in zip(entries, files)]
    portable_members.append((license_entry["path"], license_bytes))
    portable_members.append(("product-release-doc-writer/MANIFEST.json", manifest_bytes))
    with zipfile.ZipFile(target, "w") as archive:
        for member, data in sorted(portable_members, key=lambda pair: pair[0]):
            info = zipfile.ZipInfo(member, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    manifest_path = output / "product-release-doc-writer.manifest.json"
    manifest_path.write_bytes(manifest_bytes)
    (output / "product-release-doc-writer.zip.sha256").write_text(f"{digest}  {name}\n", encoding="ascii")

    # OpenAI's official skill-only plugin layout is a generated metadata wrapper
    # around the same canonical files. No behavioral instructions are duplicated.
    plugin_metadata = ROOT / "plugin.json"
    plugin_manifest = json.loads(plugin_metadata.read_text(encoding="utf-8"))
    plugin_name = "product-release-doc-writer-openai-plugin.zip"
    plugin_target = output / plugin_name
    plugin_json_bytes = (json.dumps(plugin_manifest, indent=2) + "\n").encode()
    plugin_members = [("plugin.json", plugin_json_bytes), ("LICENSE", license_bytes)]
    plugin_members.extend(("skills/" + entry["path"], path.read_bytes()) for entry, path in zip(entries, files))
    with zipfile.ZipFile(plugin_target, "w") as archive:
        for member, data in sorted(plugin_members, key=lambda pair: pair[0]):
            plugin_info = zipfile.ZipInfo(member, date_time=(1980, 1, 1, 0, 0, 0))
            plugin_info.create_system = 3
            plugin_info.external_attr = (stat.S_IFREG | 0o644) << 16
            plugin_info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(plugin_info, data)
    plugin_digest = hashlib.sha256(plugin_target.read_bytes()).hexdigest()
    plugin_files = [{"path": "plugin.json", "size": len(plugin_json_bytes), "sha256": hashlib.sha256(plugin_json_bytes).hexdigest()}, {"path": "LICENSE", "size": len(license_bytes), "sha256": hashlib.sha256(license_bytes).hexdigest()}]
    plugin_files.extend({"path": "skills/" + item["path"], "size": item["size"], "sha256": item["sha256"]} for item in entries)
    plugin_files.sort(key=lambda item: item["path"])
    plugin_contents_manifest = {"format": "openai-agent-plugin-skill-only-zip", "plugin": plugin_manifest["name"], "source": "canonical skill plus plugin.json", "files": plugin_files}
    (output / "product-release-doc-writer-openai-plugin.manifest.json").write_text(json.dumps(plugin_contents_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (output / "product-release-doc-writer-openai-plugin.zip.sha256").write_text(f"{plugin_digest}  {plugin_name}\n", encoding="ascii")
    print(f"Portable ZIP: {target}\nSHA-256: {digest}\nPackage members: {len(portable_members)} (canonical skill files: {len(entries)}, plus LICENSE and MANIFEST.json)")
    print(f"OpenAI plugin ZIP: {plugin_target}\nSHA-256: {plugin_digest}\nPackage members: {len(plugin_members)} (canonical skill files: {len(entries)}, plus LICENSE and plugin.json)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
