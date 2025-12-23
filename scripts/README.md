# Admin Scripts

Reusable Python scripts for common administration tasks.

## Scripts

| Script | Description |
|--------|-------------|
| [copy_album.py](copy_album.py) | Copy audio files by album metadata to a destination directory |

---

## copy_album.py

Copy audio files belonging to a specific album using metadata (not filenames).

**Usage:**
```bash
copy_album.py <source_dir> <dest_dir> <album_name> [--dry-run] [--prefix]
```

**Options:**
- `--dry-run, -n` — Preview what would be copied without copying
- `--prefix, -p` — Add sequential number prefix (continues from existing files)

**Examples:**
```bash
# Preview files from an album
./copy_album.py "/mnt/music/Artist" "/mnt/playlists/genre" "Album Name" --dry-run

# Copy with numbered prefixes
./copy_album.py "/mnt/music/Artist" "/mnt/playlists/genre" "Album Name" --prefix
```

**Dependencies:** `mutagen` (for reading audio metadata)
