#!/usr/bin/env python3
"""Backup script: archives the project/ folder into backups/ with ISO timestamp."""

import argparse
import os
import zipfile
from datetime import datetime
from pathlib import Path


def create_backup(source_dir: str, backup_dir: str) -> str:
    """Archive *source_dir* into a timestamped zip inside *backup_dir*.

    Args:
        source_dir: Path to the folder to back up.
        backup_dir:  Path where the zip archive will be stored.

    Returns:
        Full path to the created zip archive.

    Raises:
        FileNotFoundError: If *source_dir* does not exist.
    """
    source = Path(source_dir).resolve()
    if not source.exists():
        raise FileNotFoundError(f"Source folder not found: {source}")

    dest = Path(backup_dir).resolve()
    os.makedirs(dest, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    archive_name = f"{timestamp}_Project_Backup.zip"
    archive_path = dest / archive_name

    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in source.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(source.parent)
                zf.write(file_path, arcname)

    return str(archive_path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Back up the project/ folder to backups/ as a timestamped zip."
    )
    parser.add_argument(
        "--source",
        default="project",
        help="Source folder to back up (default: project).",
    )
    parser.add_argument(
        "--backup-dir",
        default="backups",
        help="Destination folder for the zip archive (default: backups).",
    )
    args = parser.parse_args()

    archive = create_backup(args.source, args.backup_dir)
    print(f"Backup created: {archive}")


if __name__ == "__main__":
    main()
